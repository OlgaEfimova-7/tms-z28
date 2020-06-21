import json
from datetime import date, datetime, timedelta
from decimal import Decimal
from operator import itemgetter

from django.db import IntegrityError
from django.db.models import Sum, F, Count, Value, DateTimeField, CharField, Q
from django.db.models.functions import ExtractMonth, ExtractIsoYear, ExtractYear, Concat, ExtractWeek, ExtractDay, \
    Substr, Cast, TruncSecond
from django.http import HttpResponse, HttpResponseRedirect, QueryDict, JsonResponse
from django.contrib.auth.models import User
from django.shortcuts import render
from django.views import View
from django.template import loader

from personal_finance_management_app import serializers
from personal_finance_management_app.models import UserConsumer, ItemsOfExpenditure, SubtypeOfItem
from django.contrib.auth import authenticate, login
from personal_finance_management_app.forms import (RegistrationFormForConsumer,
                                                   LogInToPersonalAccountForm,
                                                   ChequeUploadForm)
from personal_finance_management_app.models import (ChequePositions,
                                                    Cheque,
                                                    InstitutionKeywords,
                                                    Keywords)
from personal_finance_management_app.image_reader import text_reader, cheque_parser
from personal_finance_management_app.return_float_type_for_json import my_default

class MainPageView(View):
    def render_main_page(request):
        template = loader.get_template('main_page.html')
        return HttpResponse(template.render({}, request))


class LogInToPersonalAccount(View):
    def log_in(request):
        template = loader.get_template('log_in_to_personal_account.html')
        if request.method == 'POST':
            form = LogInToPersonalAccountForm(request.POST)
            if form.is_valid():
                user = authenticate(request, username=form.cleaned_data['login'],
                                    password=form.cleaned_data['password'])
                if user is not None:
                    login(request, user)
                    return HttpResponseRedirect('/personal-account/')
                else:
                    text_message = 'Введены неверные данные'
                    return HttpResponse(template.render({'form': form, 'message': text_message}, request))
            # else:
            #     return HttpResponse('not')
        else:
            form = LogInToPersonalAccountForm()
        return HttpResponse(template.render({'form': form}, request))


class RegistrationForConsumer(View):
    def register(request):
        if request.method == 'POST':
            form = RegistrationFormForConsumer(request.POST)
            if form.is_valid():
                try:
                    user = User.objects.create_user(username=form.cleaned_data['login'],
                                                    password=form.cleaned_data['password'],
                                                    first_name=form.cleaned_data['name'],
                                                    email=form.cleaned_data['email'])
                except IntegrityError:
                    form = RegistrationFormForConsumer(request.POST)
                    template = loader.get_template('registration_form_consumers.html')
                    text_message_user_already_exists = 'Пользователь с таким логином уже существует!'
                    return HttpResponse(template.render({'form': form,
                                                         'text_user_already_exists': text_message_user_already_exists},
                                                        request))

                saved_user = User.objects.get(username=form.cleaned_data['login'])
                profile = UserConsumer.objects.create(gender=form.cleaned_data['gender'],
                                                      age=int(form.cleaned_data['age']),
                                                      city=form.cleaned_data['city'],
                                                      user_id=saved_user.id)

                template = loader.get_template('registration_page_success.html')
                return HttpResponse(template.render({}, request))
            else:
                return HttpResponse('Mistake')
        else:
            form = RegistrationFormForConsumer()
        template = loader.get_template('registration_form_consumers.html')
        return HttpResponse(template.render({'form': form}, request))


class RegistrationForBusiness(View):
    def register(request):
        template = loader.get_template('registration_form_business.html')
        return HttpResponse(template.render({}, request))


class PersonalAccount(View):
    def entering_to_personal_account(request):
        if request.user.is_authenticated:
            user = request.user
            template = loader.get_template('personal_account.html')
            return HttpResponse(template.render({'user': user}, request))
        else:
            return HttpResponseRedirect('/log-in/')


class WritingOfExpensesByCheque(View):
    def write_down_expenses(request):
        # global institution_keyword, list_of_keywords_parsed_products
        if request.user.is_authenticated:
            if request.method == 'POST':
                form = ChequeUploadForm(request.POST, request.FILES)
                if form.is_valid():
                    # files = request.FILES.getlist('cheque')
                    # get list of uploaded file names
                    files = request.FILES.getlist('cheque')
                    # create list of institutions from database
                    list_of_institutions_in_db = [i.institution for i in InstitutionKeywords.objects.all()]
                    # create list of products from database
                    list_of_products_in_db = [i.keyword for i in Keywords.objects.all()]
                    list_of_all_parsed_products = []
                    list_of_all_keywords_parsed_products = []
                    list_of_all_prices = []
                    time_and_date_of_cheque = 0
                    name_of_institution_in_cheque = 0
                    institution_keyword_final = 0
                    for cheque in files:
                        recognized_text = text_reader(cheque)
                        time_and_date, name_of_institution, list_of_parsed_products, list_of_prices, institution_keyword, \
                        list_of_keywords_parsed_products = \
                            cheque_parser(recognized_text, list_of_institutions_in_db, list_of_products_in_db)
                        for product in list_of_parsed_products:
                            list_of_all_parsed_products.append(product)
                        for keyword_product in list_of_keywords_parsed_products:
                            list_of_all_keywords_parsed_products.append(keyword_product)
                        for price in list_of_prices:
                            list_of_all_prices.append(price)
                        if time_and_date is not None:
                            time_and_date_of_cheque = time_and_date
                        if name_of_institution is not None:
                            name_of_institution_in_cheque = name_of_institution
                        if institution_keyword is not None:
                            institution_keyword_final = institution_keyword
                    template = loader.get_template('validation_of_cheque.html')
                    return HttpResponse(template.render({'time_and_date': time_and_date_of_cheque,
                                                         'name_of_institution': name_of_institution_in_cheque,
                                                         'list_of_parsed_products': list_of_all_parsed_products,
                                                         'list_of_prices': list_of_all_prices,
                                                         'institution_keyword': institution_keyword_final,
                                                         'list_of_all_keywords_parsed_products':
                                                             list_of_all_keywords_parsed_products}))
            else:
                form = ChequeUploadForm()
                template = loader.get_template('writing_of_expenses_by_cheque.html')
                return HttpResponse(template.render({'form': form}, request))
        else:
            return HttpResponseRedirect('/log-in/')

    def save_of_cheque(request):
        if request.user.is_authenticated:
            # get list of verified prices of cheque
            list_of_prices = request.POST.getlist('price')
            # get list of verified products of cheque
            list_of_products = request.POST.getlist('product')
            # get time and date of cheque
            time_and_date = request.POST['time_and_date']
            # get name of institution
            name_of_institution = request.POST['name_of_institution']
            # get keyword of institutions from data base
            keyword_of_institution = request.POST['institution_keyword']
            if keyword_of_institution == 0:
                keywords = InstitutionKeywords.objects.all()
                j = 0
                while j < len(keywords):
                    if keywords[j].institution in name_of_institution:
                        keyword_of_institution = keywords[j].institution
                    j += 1
            # get instance of institution with keyword (to get id of instance
            institution = InstitutionKeywords.objects.filter(institution=keyword_of_institution)
            # get list of keywords of products
            list_of_keywords_parsed_products = request.POST.getlist('keyword')
            keywords = Keywords.objects.all()
            while len(list_of_products) > len(list_of_keywords_parsed_products):
                i = 0
                len_of_list_of_keywords = len(list_of_keywords_parsed_products)
                product = list_of_products[len_of_list_of_keywords+i]
                j = 0
                while j < len(keywords):
                    if keywords[j].keyword in product:
                        list_of_keywords_parsed_products.append(keywords[j].keyword)
                    j += 1
                if len(list_of_keywords_parsed_products) == len_of_list_of_keywords:
                    list_of_keywords_parsed_products.append('прочее')
                i += 1
            for index_i, i in enumerate(list_of_products):
                k = 0
                while k < len(keywords):
                    if keywords[k].keyword in i.lower():
                        list_of_keywords_parsed_products.pop(index_i)
                        list_of_keywords_parsed_products.insert(index_i, keywords[k].keyword)
                    k += 1
            # count total cost of cheque
            total_cost = sum(float(price) for price in list(filter(None, list_of_prices)))
            # save common information from cheque in db (Cheque)
            if list(institution) == []:
                cheque = Cheque.objects.create(date=time_and_date,
                                               name_of_institution=name_of_institution,
                                               total_cost=total_cost, user_id_id=request.user.id,
                                               institution_id_id=None
                                               )
            else:
                cheque = Cheque.objects.create(date=time_and_date,
                                               name_of_institution=name_of_institution,
                                               total_cost=total_cost, user_id_id=request.user.id,
                                               institution_id_id=institution[0].id)
            # save information from cheque positions in db (ChequePositions)
            counter = 0
            for n in range(len(list_of_products)):
                product = Keywords.objects.get(keyword=list_of_keywords_parsed_products[counter])
                cheque_positions = ChequePositions.objects.create(position=list_of_products[counter],
                                                                  price=list_of_prices[counter],
                                                                  subtype_id_id=product.subtype_id_id,
                                                                  cheque_id_id=cheque.id)
                counter += 1
            template = loader.get_template('successful_saving_of_cheque.html')
            return HttpResponse(template.render({}, request))
        else:
            return HttpResponseRedirect('/log-in/')


class WritingOfExpensesManually(View):
    def write_down_expenses(request):
        if request.user.is_authenticated:
            list_of_items_of_expenditure = [item.subtype for item in SubtypeOfItem.objects.all()]
            if request.method == 'POST':
                # get list of institutions and their id from database
                institution_from_db = [institution.institution for institution in InstitutionKeywords.objects.all()]
                institution_id_from_db = [institution.id for institution in InstitutionKeywords.objects.all()]
                # get all information from template
                information_of_expenditure = request.POST
                # get chosen subtype of expenditure
                subtype = information_of_expenditure['items_of_expenditure']
                # get instance from database corresponding to chosen subtype
                subtype_from_db = SubtypeOfItem.objects.get(subtype=subtype)
                # get institution id
                institution_id_id = None
                for index_i, i in enumerate(institution_from_db):
                    if information_of_expenditure['institution'] == i:
                        institution_id_id = institution_id_from_db[index_i]
                        break
                # save information into database table Cheque
                cheque = Cheque.objects.create(date=information_of_expenditure['date_time'],
                                               total_cost=information_of_expenditure['price'],
                                               name_of_institution=information_of_expenditure['institution'],
                                               user_id_id=request.user.id,
                                               institution_id_id=institution_id_id)
                # save information into database table ChequePositions
                cheque_positions = ChequePositions.objects.create(position=
                                                                  information_of_expenditure['product_or_service'],
                                                                  cheque_id_id=cheque.id,
                                                                  price=information_of_expenditure['price'],
                                                                  subtype_id_id=subtype_from_db.id)
                template = loader.get_template('successful_saving_of_expenses.html')
                return HttpResponse(template.render({}, request))
            else:
                template = loader.get_template('writing_of_expenses_manually.html')
                return HttpResponse(template.render({'list_of_items_of_expenditure': list_of_items_of_expenditure},
                                                    request))
        else:
            return HttpResponseRedirect('/log-in/')


class StatisticPageViewForConsumer(View):
    def display_expense_structure(request):
        if request.user.is_authenticated and list(Cheque.objects.filter(user_id_id=request.user.id)) !=[]:
                template = loader.get_template('statistic_page_for_consumer.html')
                today = date.today()
                last_month = Cheque.objects.order_by('-date__month')[1].date.month

                information_from_db_about_structure_of_consumer_expenses_last_period = \
                    list(ChequePositions.objects.filter(cheque_id__user_id_id=request.user.id).\
                        filter(cheque_id__date__month=last_month).\
                        values('subtype_id__item_id__item').\
                        annotate(period=Cast(Concat(ExtractYear('cheque_id__date'), Value('-'),
                                                    ExtractMonth('cheque_id__date')), CharField()),
                                 costs=Sum('price')))
                for i in information_from_db_about_structure_of_consumer_expenses_last_period:
                    for key, value in i.items():
                        if key == 'period':
                            if len(key) == 6:
                                i[key] = f'{value[0:5]}0{value[-1]}'
                dictdata_structure_last_period = information_from_db_about_structure_of_consumer_expenses_last_period
                information_from_db_about_structure_of_consumer_expenses = list(ChequePositions.objects.filter\
                    (cheque_id__user_id_id=request.user.id).filter(cheque_id__date__month=today.month).
                    values('subtype_id__item_id__item').annotate(period=Cast(Concat(ExtractYear('cheque_id__date'), Value('-'),
                                                    ExtractMonth('cheque_id__date')), CharField()),
                                 costs=Sum('price')))
                for i in information_from_db_about_structure_of_consumer_expenses:
                    for key, value in i.items():
                        if key == 'period':
                            if len(key) == 6:
                                i[key] = f'{value[0:5]}0{value[-1]}'
                dictdata_structure = information_from_db_about_structure_of_consumer_expenses
                information_from_db_about_consumer_expenses_periods = list(ChequePositions.objects.
                                                                           filter(cheque_id__user_id_id=request.user.id).
                                                                           values(period=Cast(Concat(ExtractYear('cheque_id__date'), Value('-'),
                                                    ExtractMonth('cheque_id__date')), CharField())).
                                                                           annotate(costs=Sum('price')))
                for i in information_from_db_about_consumer_expenses_periods:
                    for key, value in i.items():
                        if key == 'period':
                            if len(key) == 6:
                                i[key] = f'{value[0:5]}0{value[-1]}'
                dictdata_periods = information_from_db_about_consumer_expenses_periods
                information_from_db_dates = Cheque.objects.filter(user_id_id=request.user.id).\
                    extra(select={'datestr': "to_char(date, 'YYYY-MM-DD HH24:MI:SS')"}).order_by('date').\
                    values_list('datestr').distinct()
                set_of_years = set()
                set_of_months_years = set()
                set_of_days_months_years = set()
                i = 0
                while i < len(information_from_db_dates):
                    set_of_years.add(information_from_db_dates[i][0][0:4])
                    set_of_months_years.add(information_from_db_dates[i][0][0:7])
                    set_of_days_months_years.add(information_from_db_dates[i][0][0:10])
                    i += 1
                return HttpResponse(template.render({'djangodict_structure': json.dumps(dictdata_structure, ensure_ascii=False, default=my_default),
                                                     'djangodict_structure_last_period': json.dumps(dictdata_structure_last_period, ensure_ascii=False, default=my_default),
                                                    'djangodict_periods': json.dumps(dictdata_periods, ensure_ascii=False, default=my_default),
                                                    'set_of_years': set_of_years, 'set_of_months_years': set_of_months_years, 'set_of_days_months_years': set_of_days_months_years},
                                                    request))
        elif request.user.is_authenticated and list(Cheque.objects.filter(user_id_id=request.user.id)) ==[]:
            template = loader.get_template('statistic_page_for_consumer_without_data.html')
            return HttpResponse(template.render({}, request))
        else:
            return HttpResponseRedirect('/log-in/')

    def display_periods(request):
        if request.is_ajax and request.method == 'POST':
            period = request.POST['period']
            information_from_db_about_consumer_expenses_periods = 0
            if period == 'years':
                information_from_db_about_consumer_expenses_periods = \
                    list(ChequePositions.objects.filter(cheque_id__user_id_id=request.user.id).
                         values(period=ExtractYear('cheque_id__date')).
                         annotate(costs=Sum('price')))
            elif period == 'months':
                information_from_db_about_consumer_expenses_periods = list(ChequePositions.objects.filter(
                    cheque_id__user_id_id=request.user.id).values(period=Cast(Concat(ExtractYear('cheque_id__date'), Value('-'),
                                                    ExtractMonth('cheque_id__date')), CharField())).
                                                                           annotate(costs=Sum('price')))
                for i in information_from_db_about_consumer_expenses_periods:
                    for key, value in i.items():
                        if key == 'period':
                            if len(key) == 6:
                                i[key] = f'{value[0:5]}0{value[-1]}'

            # elif period == 'weeks':
            #     information_from_db_about_consumer_expenses_periods = list(ChequePositions.objects.filter(
            #         cheque_id__user_id_id=request.user.id).order_by('cheque_id__date').values(period=Concat(ExtractWeek('cheque_id__date'),
            #                                                                     ExtractYear('cheque_id__date'))).
            #                                                                annotate(costs=Sum('price')))
            elif period == 'days':
                information_from_db_about_consumer_expenses_periods_doesnt_sorted = \
                    list(ChequePositions.objects.filter(cheque_id__user_id_id=request.user.id).
                         values(period=Cast(Concat(ExtractYear('cheque_id__date'), Value('-'),
                                                    ExtractMonth('cheque_id__date'), Value('-'),
                                                                         ExtractDay('cheque_id__date')), CharField())).
                         annotate(costs=Sum('price')))
                for i in information_from_db_about_consumer_expenses_periods_doesnt_sorted:
                    for key, value in i.items():
                        if key == 'period':
                            if len(value) == 8:
                                i[key] = f'{value[0:5]}0{value[5:7]}0{value[-1]}'
                            elif len(value) == 9 and value[6] == '-':
                                i[key] = f'{value[0:5]}0{value[5:]}'
                            elif len(value) == 9 and value[7] == '-':
                                i[key] = f'{value[0:8]}0{value[8:]}'
                information_from_db_about_consumer_expenses_periods = \
                    sorted(information_from_db_about_consumer_expenses_periods_doesnt_sorted, key=itemgetter('period'))
            return JsonResponse(information_from_db_about_consumer_expenses_periods, safe=False)

    def display_structure(request):
        if request.is_ajax and request.method == 'POST':
            period = request.POST['period']
            today = date.today()
            information_from_db_about_consumer_expenses_structure = 0
            if period == 'years':
                information_from_db_about_consumer_expenses_structure = \
                    list(ChequePositions.objects.filter(cheque_id__user_id_id=request.user.id).
                         filter(cheque_id__date__year=today.year).values('subtype_id__item_id__item').
                         annotate(costs=Sum('price'), period=(ExtractYear('cheque_id__date'))))

            elif period == 'months':
                information_from_db_about_consumer_expenses_structure = \
                    list(ChequePositions.objects.filter(cheque_id__user_id_id=request.user.id).
                         filter(cheque_id__date__month=today.month).values('subtype_id__item_id__item').
                         annotate(costs=Sum('price'), period=Cast(Concat(ExtractYear('cheque_id__date'), Value('-'),
                                                    ExtractMonth('cheque_id__date')), CharField())))
                for i in information_from_db_about_consumer_expenses_structure:
                    for key, value in i.items():
                        if key == 'period':
                            if len(key) == 6:
                                i[key] = f'{value[0:5]}0{value[-1]}'
            elif period == 'days':
                information_from_db_about_consumer_expenses_structure = \
                    list(ChequePositions.objects.filter(cheque_id__user_id_id=request.user.id).
                         filter(cheque_id__date__day=today.day).values('subtype_id__item_id__item').
                         annotate(costs=Sum('price'), period=Cast(Concat(ExtractYear('cheque_id__date'), Value('-'),
                                                    ExtractMonth('cheque_id__date'), Value('-'),
                                                                         ExtractDay('cheque_id__date')), CharField())))
                for i in information_from_db_about_consumer_expenses_structure:
                    for key, value in i.items():
                        if key == 'period':
                            if len(value) == 8:
                                i[key] = f'{value[0:5]}0{value[5:7]}0{value[-1]}'
                            elif len(value) == 9 and value[6] == '-':
                                i[key] = f'{value[0:5]}0{value[5:]}'
                            elif len(value) == 9 and value[7] == '-':
                                i[key] = f'{value[0:8]}0{value[8:]}'
            return JsonResponse(information_from_db_about_consumer_expenses_structure, safe=False)

    def display_structure_of_two_periods(request):
        if request.is_ajax and request.method == 'POST':
            information_from_html = request.POST
            if information_from_html['first_period'] == "years":
                information_from_db_about_structure_of_consumer_expenses_first_period = \
                    list(ChequePositions.objects.filter(cheque_id__user_id_id=request.user.id).
                         filter(cheque_id__date__year=information_from_html['first_date']).
                         values('subtype_id__item_id__item').annotate(costs=Sum('price'),
                                                                      period=ExtractYear('cheque_id__date')))
            elif information_from_html['first_period'] == "months":
                information_from_db_about_structure_of_consumer_expenses_first_period = \
                    list(ChequePositions.objects.filter(cheque_id__user_id_id=request.user.id).
                         filter(cheque_id__date__month=information_from_html['first_date'][5:],
                                cheque_id__date__year=information_from_html['first_date'][0:4]).
                         values('subtype_id__item_id__item').
                         annotate(costs=Sum('price'), period=Cast(Concat(ExtractYear('cheque_id__date'), Value('-'),
                                                    ExtractMonth('cheque_id__date')), CharField())))
                for i in information_from_db_about_structure_of_consumer_expenses_first_period:
                    for key, value in i.items():
                        if key == 'period':
                            if len(key) == 6:
                                i[key] = f'{value[0:5]}0{value[-1]}'
            elif information_from_html['first_period'] == "days":
                information_from_db_about_structure_of_consumer_expenses_first_period = \
                    list(ChequePositions.objects.filter(cheque_id__user_id_id=request.user.id).
                         filter(cheque_id__date__day=information_from_html['first_date'][8:],
                                cheque_id__date__month=information_from_html['first_date'][5:7],
                                cheque_id__date__year=information_from_html['first_date'][0:4]).
                         values('subtype_id__item_id__item').
                         annotate(costs=Sum('price'), period=Cast(Concat(ExtractYear('cheque_id__date'), Value('-'),
                                                    ExtractMonth('cheque_id__date'), Value('-'),
                                                                         ExtractDay('cheque_id__date')), CharField())))
                for i in information_from_db_about_structure_of_consumer_expenses_first_period:
                    for key, value in i.items():
                        if key == 'period':
                            if len(value) == 8:
                                i[key] = f'{value[0:5]}0{value[5:7]}0{value[-1]}'
                            elif len(value) == 9 and value[6] == '-':
                                i[key] = f'{value[0:5]}0{value[5:]}'
                            elif len(value) == 9 and value[7] == '-':
                                i[key] = f'{value[0:8]}0{value[8:]}'
            if information_from_html['second_period'] == "years":
                information_from_db_about_structure_of_consumer_expenses_second_period = \
                    list(ChequePositions.objects.filter(cheque_id__user_id_id=request.user.id).
                         filter(cheque_id__date__year=information_from_html['second_date']).
                         values('subtype_id__item_id__item').annotate(costs=Sum('price'),
                                                                      period=ExtractYear('cheque_id__date')))
            elif information_from_html['second_period'] == "months":
                information_from_db_about_structure_of_consumer_expenses_second_period = \
                    list(ChequePositions.objects.filter(cheque_id__user_id_id=request.user.id).
                         filter(cheque_id__date__month=information_from_html['second_date'][5:],
                                cheque_id__date__year=information_from_html['second_date'][0:4]).
                         values('subtype_id__item_id__item').annotate(costs=Sum('price'),
                                                                      period=Cast(Concat(ExtractYear('cheque_id__date'),
                                                                                         Value('-'),
                                                                                         ExtractMonth('cheque_id__date')),
                                                                                  CharField())))
                for i in information_from_db_about_structure_of_consumer_expenses_second_period:
                    for key, value in i.items():
                        if key == 'period':
                            if len(key) == 6:
                                i[key] = f'{value[0:5]}0{value[-1]}'
            elif information_from_html['second_period'] == "days":
                information_from_db_about_structure_of_consumer_expenses_second_period = \
                    list(ChequePositions.objects.filter(cheque_id__user_id_id=request.user.id).
                         filter(cheque_id__date__day=information_from_html['second_date'][8:],
                                cheque_id__date__month=information_from_html['second_date'][5:7],
                                cheque_id__date__year=information_from_html['second_date'][0:4]).
                         values('subtype_id__item_id__item').
                         annotate(costs=Sum('price'), period=Cast(Concat(ExtractYear('cheque_id__date'), Value('-'),
                                                    ExtractMonth('cheque_id__date'), Value('-'),
                                                                         ExtractDay('cheque_id__date')), CharField())))
                for i in information_from_db_about_structure_of_consumer_expenses_second_period:
                    for key, value in i.items():
                        if key == 'period':
                            if len(value) == 8:
                                i[key] = f'{value[0:5]}0{value[5:7]}0{value[-1]}'
                            elif len(value) == 9 and value[6] == '-':
                                i[key] = f'{value[0:5]}0{value[5:]}'
                            elif len(value) == 9 and value[7] == '-':
                                i[key] = f'{value[0:8]}0{value[8:]}'
            return JsonResponse({'structure_of_first_period': information_from_db_about_structure_of_consumer_expenses_first_period,
                                     'structure_of_second_period': information_from_db_about_structure_of_consumer_expenses_second_period},
                                    safe=False)

class StatisticPageViewForBusiness(View):
    def display_expense_structure(request):
        template = loader.get_template('statistic_page_for_consumer.html')
        return HttpResponse(template.render({'information': ChequePositions.objects.filter()}, request))

