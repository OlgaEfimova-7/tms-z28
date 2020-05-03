from rest_framework import serializers


class OrderSerializer(serializers.Serializer):
    order_date = serializers.DateField()
    time_of_order = serializers.TimeField()
    order_price = serializers.DecimalField(max_digits=10, decimal_places=2)
    waiter_id = serializers.IntegerField()
    service_quality_assessment = serializers.IntegerField()

    def update(self, instance, validated_data):
        instance.order_date = validated_data.get('order_date', instance.order_date)
        instance.time_of_order = validated_data.get('time_of_order', instance.time_of_order)
        instance.order_price = validated_data.get('order_price', instance.order_price)
        instance.waiter_id = validated_data.get('waiter_id', instance.waiter_id)
        instance.service_quality_assessment = validated_data.get('service_quality_assessment',
                                                                 instance.service_quality_assessment)
        instance.save()
        return instance


class WaiterSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=100)
    last_name = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    address = serializers.CharField(max_length=100)
    salary = serializers.DecimalField(max_digits=10, decimal_places=2)
    work_experience = serializers.DecimalField(max_digits=4, decimal_places=1)

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.address = validated_data.get('address', instance.address)
        instance.salary = validated_data.get('salary', instance.salary)
        instance.work_experience = validated_data.get('work_experience', instance.work_experience)
        instance.save()
        return instance


class DishSerializer(serializers.Serializer):
    dish = serializers.CharField(max_length=100)
    price = serializers.DecimalField(max_digits=10, decimal_places=2)
    weight_grams = serializers.IntegerField()

    def update(self, instance, validated_data):
        instance.dish = validated_data.get('dish', instance.dish)
        instance.price = validated_data.get('price', instance.price)
        instance.weight_grams = validated_data.get('weight_grams', instance.weight_grams)
        instance.save()
        return instance


class FoodstuffSerializer(serializers.Serializer):
    name_of_foodstuff = serializers.CharField(max_length=100)
    category = serializers.CharField(max_length=100)

    def update(self, instance, validated_data):
        instance.name_of_foodstuff = validated_data.get('name_of_foodstuff', instance.name_of_foodstuff)
        instance.category = validated_data.get('category', instance.category)
        instance.save()
        return instance


class DeliverySerializer(serializers.Serializer):
    delivery_date = serializers.DateField()
    supplier = serializers.CharField(max_length=100)
    cost_of_delivery = serializers.DecimalField(max_digits=10, decimal_places=2)

    def update(self, instance, validated_data):
        instance.delivery_date = validated_data.get('delivery_date', instance.delivery_date)
        instance.supplier = validated_data.get('supplier', instance.supplier)
        instance.cost_of_delivery = validated_data.get('cost_of_delivery', instance.cost_of_delivery)
        instance.save()
        return instance
