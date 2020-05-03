import io
import json

from django import forms
from django.http import HttpResponse
from django.shortcuts import redirect
from django.views import View
from django.template import loader

from restaurant.serializers import (DeliverySerializer,
                                    FoodstuffSerializer,
                                    DishSerializer,
                                    WaiterSerializer,
                                    OrderSerializer)
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
        serializer = DeliverySerializer(delivery, data=request.POST)
        if serializer.is_valid():
            serializer.save()
            return redirect(f'http://127.0.0.1:8000/delivery/{value}')
        else:
            return HttpResponse('Information is not correct')


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
        serializer = DishSerializer(dish, data=request.POST)
        if serializer.is_valid():
            serializer.save()
            return redirect(f'http://127.0.0.1:8000/dish/{value}')
        else:
            return HttpResponse('Information is not correct')


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
        serializer = FoodstuffSerializer(foodstuff, data=request.POST)
        if serializer.is_valid():
            serializer.save()
            return redirect(f'http://127.0.0.1:8000/foodstuff/{value}')
        else:
            return HttpResponse('Information is not correct')


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
        serializer = OrderSerializer(order, data=request.POST)
        if serializer.is_valid():
            serializer.save()
            return redirect(f'http://127.0.0.1:8000/order/{value}')
        else:
            return HttpResponse('Information is not correct')


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
        serializer = WaiterSerializer(waiter, data=request.POST)
        if serializer.is_valid():
            serializer.save()
            return redirect(f'http://127.0.0.1:8000/waiter/{value}')
        else:
            return HttpResponse('Information is not correct')
