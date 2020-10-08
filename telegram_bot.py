import re
import time
from datetime import datetime, timedelta, date
from threading import Thread

import schedule as schedule
import telebot

from analytics import is_float, analyze_value_of_stocks, calculate_set_of_stock_price_delta, \
    calculate_set_of_stock_price_delta_of_several_companies, draw_graphics, create_list_of_data_from_several_lists, \
    create_set_of_data_subject_to_no_data_for_some_dates, get_list_of_decoded_companies_and_stocks, \
    get_list_of_aggregated_companies_and_stocks
from db import add_stock_information, add_user, get_user, change_frequency, get_stock_information_from_db \
    , get_frequency_and_chat_id, get_stock_information_about_specific_company, add_sold_stock_information, \
    get_sold_stock_information_from_db, get_sold_stock_information_about_specific_company
from functions_datetime import convert_UTC_to_local_time, is_second_date_bigger_then_first
from hash_and_coding import coding_str, decoding_str
from requests_of_inf_about_stock_market import get_stock_information, get_set_of_stock_prices


telegram_token = 'my_token'
telegram_bot = telebot.TeleBot(telegram_token)
welcome_text_message = 'Привет, меня зовут StockBot. Я помогу тебе следить за стоимостью твоих акций.Одно условие - ' \
               'акции Американских компаний\n\n'
commands_description_message = 'Ты можешь использовать следующие команды:\n\n' \
               '/set - записать информацию об имеющихся акциях. Введенные сведения должны ' \
               'содержать:\n- тикер компании (уникальное название компании на бирже);\n- количество акций;' \
               '\n- общую стоимость вложений в акции;\n' \
               '- валюту(BYN/USD/EUR/RUB);\n- частоту рассылки (1 - ежедневно; 2 - раз в неделю (понедельник); ' \
               '3 - раз в месяц (первое число месяца)). Сведения разделяются знаком " - ":\n ' \
               'ABC - 2 - 1000.01 - USD\n' \
               'Данная запись будет означать, что ты имеешь 2-е акции компании "ABC" на общую стоимость 1000 USD.\n\n' \
               '/change_frequency - изменить частоту рассылки информации о стоимости твоих акций\n' \
               '1 - ежедневно;\n2 - раз в неделю (понедельник);\n3 - раз в месяц (первое число месяца);\n\n' \
               '/set_sold_stocks - записать информацию о проданных акциях.' \
               'Введенные сведения должны содержать:\n- тикер компании (уникальное название компании на бирже);' \
               '\n- количество проданных акций;\n- общую стоимость продажи акций;\n-валюту(BYN/USD/EUR/RUB).\n' \
               'Сведения разделяются знаком " - ":\nABC - 2 - 1000.01 - USD\n\n' \
               '/get - получить информацию о прибыле/убытке, полученную как разность между текущей стоимости акций и' \
               ' инвестированной суммой\n\n' \
               '/get_graphic - получить график дельты (прибыли/убытка) от стоимости акций по сравнению со ' \
               'стоимостью покупки акций\n' \
               'Для этого необходимо ввести данные в следующем порядке (каждый пункт вводится с новой строки):\n' \
               '1. Дата начала периода (вида 2020-07-01)\n' \
               '2. Дата окончания периода (вида 2020-08-01)\n' \
               '3. Период агрегации данных:\n D - дни;\n W - недели;\n M - месяцы.\n' \
               '4. Тикер/тикеры компании/компаний (разделителем должна быть ","\n\n' \
               '/help - получить информацию о всех возможных командах\n\n\n'
start_to_use_text_message = 'Теперь введи команду /set -> введи данные об акциях \n\nПоехали!!!'


@telegram_bot.message_handler(commands=['start'])
def start_message(message):
    telegram_bot.send_message(message.chat.id, f'{welcome_text_message}{commands_description_message}{start_to_use_text_message}')


@telegram_bot.message_handler(commands=['help'])
def help_message(message):
    telegram_bot.send_message(message.chat.id, commands_description_message)


@telegram_bot.message_handler(commands=['set'])
def set_message(message):
    sent = telegram_bot.send_message(message.chat.id, 'Введенные сведения должны содержать:\n- тикер компании '
                                                      '(уникальное название компании на бирже);'
                                                      '\n- количество акций;\n- общую стоимость вложений в акции;\n'
                                                      '-валюту(BYN/USD/EUR/RUB).\n'
                                                      'Сведения разделяются знаком " - ":\nABC - 2 - 1000.01 - USD\n')
    telegram_bot.register_next_step_handler(sent, save_stock_information_into_db)


def if_amount_of_elems_in_record_is_4(list_of_all_stocks_without_spaces):
    for i in range(len(list_of_all_stocks_without_spaces)):
        if len(list_of_all_stocks_without_spaces[i]) == 4:
            continue
        else:
            return False


def if_tickers_of_companies_are_correct(list_of_all_stocks_without_spaces):
    for i in list_of_all_stocks_without_spaces:
        company_ticker = i[0]
        if get_stock_information(company_ticker) == {}:
            return False


def if_amount_of_company_stocks_is_number(list_of_all_stocks_without_spaces):
    for i in list_of_all_stocks_without_spaces:
        amount_of_stocks = i[1]
        if amount_of_stocks.isdigit() is False:
            return False


def if_sum_of_investments_is_number(list_of_all_stocks_without_spaces):
    for i in list_of_all_stocks_without_spaces:
        sum_of_investments = i[2]
        if is_float(sum_of_investments) is False:
            return False


def if_currency_is_correct(list_of_all_stocks_without_spaces):
    for i in list_of_all_stocks_without_spaces:
        currency = i[3]
        if currency not in ('BYN', 'USD', 'EUR', 'RUB'):
            return False


def validation_of_stock_information(list_of_all_stocks_without_spaces, chat_id, message, function):
    if if_amount_of_elems_in_record_is_4(list_of_all_stocks_without_spaces) is False:
        telegram_bot.send_message(chat_id, 'Информация внесена неверно. Попробуй еще раз')
        function(message)
    elif if_tickers_of_companies_are_correct(list_of_all_stocks_without_spaces) is False:
        telegram_bot.send_message(chat_id, 'Компания введена неверно (необходим тикер компании). '
                                                   'Попробуй еще раз')
        function(message)
    elif if_amount_of_company_stocks_is_number(list_of_all_stocks_without_spaces) is False:
        telegram_bot.send_message(chat_id, 'Информация о количестве акций внесена неверно. Попробуй еще раз')
        function(message)
    elif if_sum_of_investments_is_number(list_of_all_stocks_without_spaces) is False:
        telegram_bot.send_message(chat_id, 'Информация о сумме инвестиций внесена неверно. Попробуй еще раз')
        function(message)
    elif if_currency_is_correct(list_of_all_stocks_without_spaces) is False:
        telegram_bot.send_message(chat_id, 'Информация о валюте внесена неверно. Попробуй еще раз')
        function(message)
    else:
        return list_of_all_stocks_without_spaces


@telegram_bot.message_handler(commands=['set_sold_stocks'])
def set_sold_stocks_message(message):
    sent = telegram_bot.send_message(message.chat.id, 'Введенные сведения должны содержать:\n- тикер компании '
                                                      '(уникальное название компании на бирже);'
                                                      '\n- количество проданных акций;'
                                                      '\n- общую стоимость продажи акций;\n'
                                                      '-валюту(BYN/USD/EUR/RUB).\n'
                                                      'Сведения разделяются знаком " - ":\nABC - 2 - 1000.01 - USD\n')
    telegram_bot.register_next_step_handler(sent, save_sold_stocks_information)


def save_stock_information_into_db(message):
    list_of_all_stocks_with_spaces = [(i.split('-')) for i in message.text.split('\n')]
    list_of_all_stocks_without_spaces = [[i.strip() for i in j] for j in list_of_all_stocks_with_spaces]
    chat_id = message.chat.id
    valid_list_of_data = validation_of_stock_information(list_of_all_stocks_without_spaces, chat_id, message,
                                                         set_message)
    if valid_list_of_data is not None:
        telegram_bot.send_message(message.chat.id, 'Информация внесена корректно')
        user_id = 0
        if get_user(coding_str(str(message.chat.id))) == []:
            add_user(coding_str(str(message.chat.id)),  0)
            user_id = get_user(coding_str(str(message.chat.id)))[0][0]
            change_frequency_message(message)
        else:
            user_id = get_user(coding_str(str(message.chat.id)))[0][0]
            telegram_bot.send_message(message.chat.id, 'Теперь можешь воспользоваться командами /get, /get_graphic, '
                                                       'или вызови команду /help, чтобы просмотреть список всех команд')
        for i in valid_list_of_data:
            coded_company = coding_str(i[0])
            coded_amount_of_stocks = coding_str(str(i[1]))
            coded_sum_of_investments = coding_str(str(i[2]))
            coded_currency = coding_str(i[3])
            add_stock_information(coded_company, coded_amount_of_stocks, coded_sum_of_investments, coded_currency, user_id)




def save_sold_stocks_information(message):
    user = get_user(coding_str(str(message.chat.id)))
    if user == []:
        telegram_bot.send_message(message.chat.id, 'Не внесена информация о приобретенных акциях. Воспользуйся '
                                                   'командой /set')
    list_of_all_stocks_with_spaces = [(i.split('-')) for i in message.text.split('\n')]
    list_of_all_stocks_without_spaces = [[i.strip() for i in j] for j in list_of_all_stocks_with_spaces]
    chat_id = message.chat.id
    valid_list_of_data = validation_of_stock_information(list_of_all_stocks_without_spaces, chat_id, message,
                                                         set_sold_stocks_message)
    if valid_list_of_data is not None:
        telegram_bot.send_message(message.chat.id, 'Информация внесена корректно')
        user_id = get_user(coding_str(str(message.chat.id)))[0][0]
        telegram_bot.send_message(message.chat.id, 'Теперь можешь воспользоваться командами /get, /get_graphic, '
                                                   'или вызови команду /help, чтобы просмотреть список всех команд')
        for i in valid_list_of_data:
            coded_company = coding_str(i[0])
            coded_amount_of_stocks = coding_str(str(i[1]))
            coded_sum_of_investments = coding_str(str(i[2]))
            coded_currency = coding_str(i[3])
            add_sold_stock_information(coded_company, coded_amount_of_stocks, coded_sum_of_investments, coded_currency,
                                       user_id)


@telegram_bot.message_handler(commands=['change_frequency'])
def change_frequency_message(message):
    user = get_user(coding_str(str(message.chat.id)))
    if user == []:
        telegram_bot.send_message(message.chat.id, 'Для начало необходимо внести информацию об акциях. '
                                                   'Используй комманду /set')
    else:
        sent = telegram_bot.send_message(message.chat.id, 'Выбери частоту рассылки:\n\n1 - ежедневно;'
                                                          '\n2 - раз в неделю (понедельник);\n'
                                                          '3 - раз в месяц (первое число месяца);')
        telegram_bot.register_next_step_handler(sent, validation_of_frequency)


def validation_of_frequency(message):
    if message.text in ['1', '2', '3']:
        telegram_bot.send_message(message.chat.id, 'Спасибо!\n\nТеперь можешь воспользоваться командами /get, '
                                                   '/get_graphic, или вызови команду /help, чтобы просмотреть список '
                                                   'всех команд')
        change_frequency(int(message.text), get_user(coding_str(str(message.chat.id)))[0][0])
        return message.text
    else:
        telegram_bot.send_message(message.chat.id, 'Введена неверная частота. Попробуй еще раз!')
        change_frequency_message(message)


@telegram_bot.message_handler(commands=['get'])
def send_information(message):
    if type(message) is telebot.types.Message:
        user = get_user(coding_str(str(message.chat.id)))
        if user == []:
            telegram_bot.send_message(message.chat.id, 'Для начало необходимо внести информацию об акциях. '
                                                           'Используй комманду /set')
        else:
            user_id = get_user(coding_str(str(message.chat.id)))[0][0]
            list_of_coded_stock_information_from_db = get_stock_information_from_db(user_id)
            decoded_list = get_list_of_decoded_companies_and_stocks(list_of_coded_stock_information_from_db)
            aggregated_list = get_list_of_aggregated_companies_and_stocks(decoded_list)
            list_of_coded_sold_stocks_from_db = get_sold_stock_information_from_db(user_id)
            if not list_of_coded_sold_stocks_from_db:
                response = analyze_value_of_stocks(aggregated_list)
                telegram_bot.send_message(message.chat.id, response)
            else:
                decoded_sold_list = get_list_of_decoded_companies_and_stocks(list_of_coded_sold_stocks_from_db)
                aggregated_sold_list = get_list_of_aggregated_companies_and_stocks(decoded_sold_list)
                response = analyze_value_of_stocks(aggregated_list, aggregated_sold_list)
                telegram_bot.send_message(message.chat.id, response)
    else:
        user_id = get_user(message)[0][0]
        list_of_coded_stock_information_from_db = get_stock_information_from_db(user_id)
        decoded_list = get_list_of_decoded_companies_and_stocks(list_of_coded_stock_information_from_db)
        aggregated_list = get_list_of_aggregated_companies_and_stocks(decoded_list)
        list_of_coded_sold_stocks_from_db = get_sold_stock_information_from_db(user_id)
        if not list_of_coded_sold_stocks_from_db:
            response = analyze_value_of_stocks(aggregated_list)
            telegram_bot.send_message(int(decoding_str(message)), response)
        else:
            decoded_sold_list = get_list_of_decoded_companies_and_stocks(list_of_coded_sold_stocks_from_db)
            aggregated_sold_list = get_list_of_aggregated_companies_and_stocks(decoded_sold_list)
            response = analyze_value_of_stocks(aggregated_list, aggregated_sold_list)
            telegram_bot.send_message(int(decoding_str(message)), response)


@telegram_bot.message_handler(commands=['get_graphic'])
def send_message_for_getting_graphic(message):
    user = get_user(coding_str(str(message.chat.id)))
    if user == []:
        telegram_bot.send_message(message.chat.id, 'Для начало необходимо внести информацию об акциях. '
                                                   'Используй комманду /set')
    else:
        sent = telegram_bot.send_message(message.chat.id, 'Введи данные в следующем порядке (каждый пункт вводится '
                                                          'с новой строки):\n'
                                                          '1. Дата начала периода (вида 2020-07-01)\n'
                                                          '2. Дата окончания периода (вида 2020-08-01)\n'
                                                          '3. Период агрегации данных:\n D - дни;\n W - недели;'
                                                          '\n M - месяцы.\n'
                                                          '4. Тикер/тикеры компании/компаний (разделителем должна быть ","'
                                                          '\n желатьельно не более 10 компаний'
                                                          '\n\nВид введенной информации:\n'
                                                          '2020-07-25\n'
                                                          '2020-08-01\n'
                                                          'D\n'
                                                          'ABC, CBA')
        telegram_bot.register_next_step_handler(sent, get_graphic_of_stock_delta)


def validation_of_date(date):
    if re.search(r'\d{4}-\d{2}-\d{2}', date) is not None and int(date[5:7]) < 13 and \
            int(date[8:]) < 31:
        return date
    else:
        return None


def validation_of_period_of_aggregation(period):
    if period in ['D', 'W', 'M']:
        return period
    else:
        return None


def get_graphic_of_stock_delta(message):
    global list_of_companies_without_spaces
    user_id = get_user(coding_str(str(message.chat.id)))[0][0]
    text_of_message = message.text
    # Create list of params from string splitting by \n
    list_of_params_from_text_message = text_of_message.split('\n')
    # Check and remove spaces from params
    list_of_information_for_validation_without_spaces = list(map(str.strip, list_of_params_from_text_message))
    flag = True
    if len(list_of_information_for_validation_without_spaces) == 4:
        # Create variables before their validation
        start_date = list_of_information_for_validation_without_spaces[0][-10:]
        finish_date = list_of_information_for_validation_without_spaces[1][-10:]
        period_of_aggregation = list_of_information_for_validation_without_spaces[2]
        companies = list_of_information_for_validation_without_spaces[3]
        list_of_companies = companies.split(',')
        list_of_companies_without_spaces = list(map(str.strip, list_of_companies))
    else:
        telegram_bot.send_message(message.chat.id, 'Введены не все необходимые данные')
        send_message_for_getting_graphic(message)
        flag = False
    if flag is True:
        validated_start_date = validation_of_date(start_date)
        validated_finish_date = validation_of_date(finish_date)
        validated_period_of_aggregation = validation_of_period_of_aggregation(period_of_aggregation)
        if validated_start_date is None:
            telegram_bot.send_message(message.chat.id, 'Неверно введена дата начала периода')
            send_message_for_getting_graphic(message)
            flag = False
        elif validated_finish_date is None:
            telegram_bot.send_message(message.chat.id, 'Неверно введена дата окончания периода')
            send_message_for_getting_graphic(message)
            flag = False
        elif validated_period_of_aggregation is None:
            telegram_bot.send_message(message.chat.id, 'Неверно введен период агрегации')
            send_message_for_getting_graphic(message)
            flag = False
        elif is_second_date_bigger_then_first(validated_start_date, validated_finish_date) is False:
            telegram_bot.send_message(message.chat.id, 'Дата окончания периода меньще даты начала периода')
            send_message_for_getting_graphic(message)
            flag = False
    if flag is True:
        for company in list_of_companies_without_spaces:
            if get_stock_information_about_specific_company(user_id, coding_str(company)) == []:
                telegram_bot.send_message(message.chat.id, f'Информация о компании {company} не была тобой указана.')
                send_message_for_getting_graphic(message)
                flag = False
                break
    if flag is True:
        telegram_bot.send_message(message.chat.id, f'Данные внесены верно. Идет процесс создания графика')
        list_of_data_sets = []
        list_of_date_sets = []
        for company in list_of_companies_without_spaces:
            set_of_market_prices_of_stocks, set_of_dates = get_set_of_stock_prices(start_date, finish_date, company,
                                                                                   period_of_aggregation)
            # Checking, if result of request function is None (when API exception appears) and informing user to get
            # request later
            if set_of_market_prices_of_stocks is None and set_of_dates is None:
                telegram_bot.send_message(message.chat.id, f'На данный момент сервер перегружен. Попробуй через минуту.'
                                                           f' Я пришлю тебе оповещение')
                time.sleep(60)
                send_message_for_getting_graphic(message)
                flag = False
                break
            list_of_data_sets.append(set_of_market_prices_of_stocks)
            list_of_date_sets.append(set_of_dates)
    if flag is True:
        final_list_of_dates = create_list_of_data_from_several_lists(list_of_date_sets)
        final_list_of_data_sets = create_set_of_data_subject_to_no_data_for_some_dates(list_of_data_sets,
                                                                                       list_of_date_sets,
                                                                                       final_list_of_dates)
        list_of_delta_sets_of_all_companies = []
        for index, company in enumerate(list_of_companies_without_spaces):
            set_of_coded_information_from_db = get_stock_information_about_specific_company(user_id, coding_str(company))
            set_of_decoded_information_about_stocks_of_company = get_list_of_decoded_companies_and_stocks(
                set_of_coded_information_from_db)
            set_of_aggregated_information_about_stocks_of_company = get_list_of_aggregated_companies_and_stocks(
                set_of_decoded_information_about_stocks_of_company)
            set_of_coded_sold_information_from_db = get_sold_stock_information_about_specific_company(user_id,
                                                                                            coding_str(company))
            if not set_of_coded_sold_information_from_db:
                initial_value_of_stocks = set_of_aggregated_information_about_stocks_of_company[0][2]
                amount_of_stocks = set_of_aggregated_information_about_stocks_of_company[0][1]
                list_of_delta_of_stock_prices = calculate_set_of_stock_price_delta(
                    initial_value_of_stocks, amount_of_stocks, final_list_of_data_sets[index])
                list_of_delta_sets_of_all_companies.append(list_of_delta_of_stock_prices)
            else:
                set_of_decoded_sold_information_about_stocks_of_company = get_list_of_decoded_companies_and_stocks(
                    set_of_coded_sold_information_from_db)
                set_of_aggregated_sold_information_about_stocks_of_company = get_list_of_aggregated_companies_and_stocks(
                    set_of_decoded_sold_information_about_stocks_of_company)
                initial_value_of_stocks = set_of_aggregated_information_about_stocks_of_company[0][2]
                amount_of_all_stocks = set_of_aggregated_information_about_stocks_of_company[0][1]
                cost_of_all_stocks = set_of_aggregated_sold_information_about_stocks_of_company[0][2]
                amount_of_sold_stocks = set_of_aggregated_sold_information_about_stocks_of_company[0][1]
                actual_amount_of_stocks = amount_of_all_stocks - amount_of_sold_stocks
                list_of_delta_of_stock_prices = calculate_set_of_stock_price_delta(
                    initial_value_of_stocks, actual_amount_of_stocks, final_list_of_data_sets[index],
                    cost_of_all_stocks)
                list_of_delta_sets_of_all_companies.append(list_of_delta_of_stock_prices)
        if len(list_of_companies_without_spaces) > 1:
            set_of_sum_of_deltas = calculate_set_of_stock_price_delta_of_several_companies(
                list_of_delta_sets_of_all_companies)
            list_of_delta_sets_of_all_companies.append(set_of_sum_of_deltas)
            list_of_companies_without_spaces.append('Суммарная дельта')
        final_list_of_dates_in_date_format = [convert_UTC_to_local_time(i) for i in final_list_of_dates]
        # list_of_dates = create_list_of_dates_between_start_and_final_date_without_vacations(start_date, finish_date)
        draw_graphics(list_of_delta_sets_of_all_companies, list_of_companies_without_spaces,
                                final_list_of_dates_in_date_format, message.chat.id)

        telegram_bot.send_photo(message.chat.id, photo=open(f'graphics/graph_{message.chat.id}.png', 'rb'))


def do_schedule():
    list_of_chat_id_and_frequencies = get_frequency_and_chat_id()
    for index_user_information, user_information in enumerate(list_of_chat_id_and_frequencies):
        time_for_sending = datetime.strptime('10:10:00', '%H:%M:%S') + timedelta(minutes=index_user_information)
        frequency = user_information[1]
        chat_id = user_information[0]
        if frequency == 1:
            schedule.every().day.at(f'{time_for_sending.hour}:{time_for_sending.minute}').\
                do(send_information, chat_id)
        elif frequency == 2:
            schedule.every().monday.at(f'{time_for_sending.hour}:{time_for_sending.minute}').\
                do(send_information, chat_id)
        elif frequency == 3:
            if date.today().day == 1:
                schedule.every().day().at(f'{time_for_sending.hour}:{time_for_sending.minute}').\
                    do(send_information, chat_id)

    while True:
        schedule.run_pending()
        time.sleep(5)


def main_loop():
    thread = Thread(target=do_schedule)
    thread.start()

    telegram_bot.polling(True)


if __name__ == '__main__':
    main_loop()






