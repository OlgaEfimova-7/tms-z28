import os
from django.db.models import Max, Avg, Count, Sum

from restaurant.models import Order, Waiter
# from django.db import connection
#
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'restaurant.settings')
#
#
# # waiter1 = Waiter.objects.all().annotate(Count('order'))
#
# waiter2 = Waiter.objects.annotate(avg_price=Avg('order__order_price'),
#                                   avg_assessment=Avg('order__service_quality_assessment'))
#
# for i in waiter2:
#     print(f'{i.id}) {i.first_name} --> {i.avg_price} --> {i.avg_assessment}')
# print(connection.queries)
#
#
# def waiter(value):
#     waiter1 = Waiter.objects.filter(id=value).annotate(avg_price=Avg('order__order_price'),
#                                                    avg_assessment=Avg('order__service_quality_assessment'))
#     for i in waiter1:
#         return f'{i.id}) {i.first_name} --> {i.avg_price} --> {i.avg_assessment}'
#
#
# print(waiter(7))
