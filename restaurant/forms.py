from django.forms import ModelForm

from restaurant.models import Delivery, Dish, Foodstuff, Order, Waiter


class ChangeDeliveryForm(ModelForm):
    class Meta:
        model = Delivery
        exclude = ('supplier', 'cost_of_delivery', 'delivery_date')


class ChangeDishForm(ModelForm):
    class Meta:
        model = Dish
        exclude = ('dish', 'price', 'weight_grams')


class ChangeFoodstuffForm(ModelForm):
    class Meta:
        model = Foodstuff
        exclude = ('name_of_foodstuff', 'category')


class ChangeOrderForm(ModelForm):
    class Meta:
        model = Order
        exclude = ('order_date', 'time_of_order', 'order_price', 'waiter_id', 'service_quality_assessment')


class ChangeWaiterForm(ModelForm):
    class Meta:
        model = Waiter
        exclude = ('first_name', 'last_name', 'email', 'address', 'salary', 'work_experience')
