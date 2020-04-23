"""django_example URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from restaurant.views import MainPageView, DeliveryPageView, DishPageView, FoodstuffPageView, OrderPageView, \
    WaiterPageView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainPageView.get_main_page),
    path('delivery/', DeliveryPageView.get_delivery_page),
    path('delivery/<int:value>/', DeliveryPageView.get_delivery_by_id),
    path('delivery/<int:value>/delete', DeliveryPageView.delivery_delete),
    path('delivery/<int:value>/change', DeliveryPageView.delivery_change_value),
    path('delivery/<int:value>/change/success', DeliveryPageView.delivery_change_success),
    path('dish/', DishPageView.get_dish_page),
    path('dish/<int:value>/', DishPageView.get_dish_by_id),
    path('dish/<int:value>/delete', DishPageView.dish_delete),
    path('dish/<int:value>/change', DishPageView.dish_change_value),
    path('dish/<int:value>/change/success', DishPageView.dish_change_success),
    path('foodstuff/', FoodstuffPageView.get_foodstuff_page),
    path('foodstuff/<int:value>/', FoodstuffPageView.get_foodstuff_by_id),
    path('foodstuff/<int:value>/delete', FoodstuffPageView.foodstuff_delete),
    path('foodstuff/<int:value>/change', FoodstuffPageView.foodstuff_change_value),
    path('foodstuff/<int:value>/change/success', FoodstuffPageView.foodstuff_change_success),
    path('order/', OrderPageView.get_order_page),
    path('order/<int:value>/', OrderPageView.get_order_by_id),
    path('order/<int:value>/delete', OrderPageView.order_delete),
    path('order/<int:value>/change', OrderPageView.order_change_value),
    path('order/<int:value>/change/success', OrderPageView.order_change_success),
    path('waiter/', WaiterPageView.get_waiter_page),
    path('waiter/<int:value>/', WaiterPageView.get_waiter_by_id),
    path('waiter/<int:value>/delete', WaiterPageView.waiter_delete),
    path('waiter/<int:value>/change', WaiterPageView.waiter_change_value),
    path('waiter/<int:value>/change/success', WaiterPageView.waiter_change_success),
]
