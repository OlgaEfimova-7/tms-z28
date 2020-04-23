from django.db import models
# from restaurant.wsgi import get_wsgi_application
# application = get_wsgi_application()
from django.forms import ModelForm


class Order(models.Model):
    order_date = models.DateField()
    time_of_order = models.TimeField(default=None)
    waiter = models.ForeignKey('Waiter', on_delete=models.CASCADE)
    order_price = models.DecimalField(max_digits=10, decimal_places=2)
    service_quality_assessment = models.IntegerField(default=None)


class Waiter(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    work_experience = models.DecimalField(max_digits=4, decimal_places=1)


class Dish(models.Model):
    dish = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10,  decimal_places=2)
    weight_grams = models.IntegerField()
    orders = models.ManyToManyField(Order)


class Foodstuff(models.Model):
    name_of_foodstuff = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    dishes = models.ManyToManyField(Dish)


class Delivery(models.Model):
    delivery_date = models.DateField()
    supplier = models.CharField(max_length=100)
    cost_of_delivery = models.DecimalField(max_digits=10, decimal_places=2)
    delivery_on_time = models.BooleanField()
    foodstuffs = models.ManyToManyField(Foodstuff)




