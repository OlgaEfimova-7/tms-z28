from django import forms
from django.http import HttpResponse
from django.shortcuts import redirect
from django.views import View
from django.template import loader, context

from restaurant.forms import ChangeDeliveryForm
from restaurant.models import Delivery, Dish, Foodstuff, Order, Waiter


class MainPageView(View):

    def get_main_page(request):
        template = loader.get_template('main_page.html')
        return HttpResponse(template.render({}, request))


class DeliveryPageView(View):
    def get_delivery_page(request):
        template = loader.get_template('delivery.html')
        return HttpResponse(template.render({'delivery': Delivery.objects.all()}, request))

    def get_delivery_by_id(request, value):
        template = loader.get_template('delivery_by_id.html')
        return HttpResponse(template.render({'delivery': Delivery.objects.get(id=value)}, request))

    def delivery_delete(request, value):
        Delivery.objects.filter(id=value).delete()
        return redirect('http://127.0.0.1:8000/delivery/')

    def delivery_change_value(request, value):
        template = loader.get_template('delivery_change.html')
        return HttpResponse(template.render({'delivery': Delivery.objects.get(id=value)}, request))

    def delivery_change_success(request, value):
        delivery = Delivery.objects.get(id=value)
        saved_supplier = request.POST.get('supplier')
        saved_date = request.POST.get('delivery_date')
        saved_cost = request.POST.get('cost_of_delivery')
        delivery.supplier = saved_supplier
        delivery.delivery_date = saved_date
        delivery.cost_of_delivery = saved_cost
        delivery.save()
        return redirect(f'http://127.0.0.1:8000/delivery/{value}')


class DishPageView(View):
    def get_dish_page(request):
        template = loader.get_template('dish.html')
        return HttpResponse(template.render({'dish': Dish.objects.all()}, request))

    def get_dish_by_id(request, value):
        template = loader.get_template('dish-by_id.html')
        return HttpResponse(template.render({'dish': Dish.objects.get(id=value)}, request))

    def dish_delete(request, value):
        Dish.objects.filter(id=value).delete()
        return redirect('http://127.0.0.1:8000/dish/')

    def dish_change_value(request, value):
        template = loader.get_template('dish_change.html')
        return HttpResponse(template.render({'dish': Dish.objects.get(id=value)}, request))

    def dish_change_success(request, value):
        dish = Dish.objects.get(id=value)
        saved_dish = request.POST.get('dish')
        saved_price = request.POST.get('price')
        saved_weight = request.POST.get('weight')
        dish.dish = saved_dish
        dish.price = saved_price
        dish.weight_grams = saved_weight
        dish.save()
        return redirect(f'http://127.0.0.1:8000/dish/{value}')


class FoodstuffPageView(View):
    def get_foodstuff_page(request):
        template = loader.get_template('foodstuff.html')
        return HttpResponse(template.render({'foodstuff': Foodstuff.objects.all()}, request))

    def get_foodstuff_by_id(request, value):
        template = loader.get_template('foodstuff_by_id.html')
        return HttpResponse(template.render({'foodstuff': Foodstuff.objects.get(id=value)}, request))

    def foodstuff_delete(request, value):
        Foodstuff.objects.filter(id=value).delete()
        return redirect('http://127.0.0.1:8000/foodstuff/')

    def foodstuff_change_value(request, value):
        template = loader.get_template('foodstuff_change.html')
        return HttpResponse(template.render({'foodstuff': Foodstuff.objects.get(id=value)}, request))

    def foodstuff_change_success(request, value):
        foodstuff = Foodstuff.objects.get(id=value)
        saved_name_of_foodstuff = request.POST.get('name_of_foodstuff')
        saved_category = request.POST.get('category')
        foodstuff.name_of_foodstuff = saved_name_of_foodstuff
        foodstuff.category = saved_category
        foodstuff.save()
        return redirect(f'http://127.0.0.1:8000/foodstuff/{value}')


class OrderPageView(View):
    def get_order_page(request):
        template = loader.get_template('order.html')
        return HttpResponse(template.render({'order': Order.objects.all()}, request))

    def get_order_by_id(request, value):
        template = loader.get_template('order_by_id.html')
        return HttpResponse(template.render({'order': Order.objects.get(id=value)}, request))

    def order_delete(request, value):
        Order.objects.filter(id=value).delete()
        return redirect('http://127.0.0.1:8000/order/')

    def order_change_value(request, value):
        template = loader.get_template('order_change.html')
        return HttpResponse(template.render({'order': Order.objects.get(id=value)}, request))

    def order_change_success(request, value):
        order = Order.objects.get(id=value)
        saved_order_date = request.POST.get('order_date')
        saved_time_of_order = request.POST.get('time_of_order')
        saved_price = request.POST.get('order_price')
        saved_waiter_id = request.POST.get('waiter_id')
        saved_sqa = request.POST.get('service_quality_assessment')
        order.order_date = saved_order_date
        order.time_of_order = saved_time_of_order
        order.order_price = saved_price
        order.waiter_id = saved_waiter_id
        order.service_quality_assessment = saved_sqa
        order.save()
        return redirect(f'http://127.0.0.1:8000/order/{value}')


class WaiterPageView(View):
    def get_waiter_page(request):
        template = loader.get_template('waiter.html')
        return HttpResponse(template.render({'waiter': Waiter.objects.all()}, request))

    def get_waiter_by_id(request, value):
        template = loader.get_template('waiter_by_id.html')
        return HttpResponse(template.render({'waiter': Waiter.objects.get(id=value)}, request))

    def waiter_delete(request, value):
        Waiter.objects.filter(id=value).delete()
        return redirect('http://127.0.0.1:8000/waiter/')

    def waiter_change_value(request, value):
        template = loader.get_template('waiter_change.html')
        return HttpResponse(template.render({'waiter': Waiter.objects.get(id=value)}, request))

    def waiter_change_success(request, value):
        waiter = Waiter.objects.get(id=value)
        saved_first_nane = request.POST.get('first_name')
        saved_last_name = request.POST.get('last_name')
        saved_email = request.POST.get('email')
        saved_address = request.POST.get('address')
        saved_salary = request.POST.get('salary')
        saved_work_experience = request.POST.get('work_experience')
        waiter.first_name = saved_first_nane
        waiter.last_name = saved_last_name
        waiter.email = saved_email
        waiter.address = saved_address
        waiter.salary = saved_salary
        waiter.work_experience = saved_work_experience
        waiter.save()
        return redirect(f'http://127.0.0.1:8000/waiter/{value}')


# class DeliveryForm(forms.Form):
#     supplier = forms.CharField()
#     cost_of_delivery = forms.CharField()
#     delivery_date = forms.CharField()
