from restaurant.serializers import (DeliverySerializer,
                                    FoodstuffSerializer,
                                    DishSerializer,
                                    WaiterSerializer,
                                    OrderSerializer)
from restaurant.models import Delivery, Dish, Foodstuff, Order, Waiter
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from restaurant.paginations import LargeResultsSetPagination


class DeliveryViewSet(viewsets.ModelViewSet):
    serializer_class = DeliverySerializer
    pagination_class = LargeResultsSetPagination
    queryset = Delivery.objects.all()

    def list(self, request):
        queryset = Delivery.objects.all()
        page = self.paginate_queryset(queryset)
        serializer = self.get_serializer(page, many=True)
        return self.get_paginated_response(serializer.data)

    def retrieve(self, request, pk):
        queryset = Delivery.objects.all()
        delivery = get_object_or_404(queryset, pk=pk)
        serializer = DeliverySerializer(delivery)
        return Response(serializer.data)


class DishViewSet(viewsets.ModelViewSet):
    serializer_class = DishSerializer
    pagination_class = LargeResultsSetPagination
    queryset = Dish.objects.all()

    def list(self, request):
        queryset = Dish.objects.all()
        page = self.paginate_queryset(queryset)
        serializer = self.get_serializer(page, many=True)
        return self.get_paginated_response(serializer.data)

    def retrieve(self, request, pk):
        queryset = Dish.objects.all()
        dish = get_object_or_404(queryset, pk=pk)
        serializer = DishSerializer(dish)
        return Response(serializer.data)


class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    pagination_class = LargeResultsSetPagination
    queryset = Order.objects.all()

    def list(self, request):
        queryset = Order.objects.all()
        page = self.paginate_queryset(queryset)
        serializer = self.get_serializer(page, many=True)
        return self.get_paginated_response(serializer.data)

    def retrieve(self, request, pk):
        queryset = Order.objects.all()
        order = get_object_or_404(queryset, pk=pk)
        serializer = OrderSerializer(order)
        return Response(serializer.data)


class FoodstuffViewSet(viewsets.ModelViewSet):
    queryset = Foodstuff.objects.all()
    serializer_class = FoodstuffSerializer
    pagination_class = LargeResultsSetPagination

    def list(self, request):
        queryset = Foodstuff.objects.all()
        page = self.paginate_queryset(queryset)
        serializer = self.get_serializer(page, many=True)
        return self.get_paginated_response(serializer.data)

    def retrieve(self, request, pk):
        queryset = Foodstuff.objects.all()
        foodstuff = get_object_or_404(queryset, pk=pk)
        serializer = FoodstuffSerializer(foodstuff)
        return Response(serializer.data)


class WaiterViewSet(viewsets.ModelViewSet):
    queryset = Waiter.objects.all()
    serializer_class = WaiterSerializer
    pagination_class = LargeResultsSetPagination

    def list(self, request):
        queryset = Waiter.objects.all()
        page = self.paginate_queryset(queryset)
        serializer = self.get_serializer(page, many=True)
        return self.get_paginated_response(serializer.data)

    def retrieve(self, request, pk):
        queryset = Waiter.objects.all()
        waiter = get_object_or_404(queryset, pk=pk)
        serializer = WaiterSerializer(waiter)
        return Response(serializer.data)
