from rest_framework import serializers

GENDER = (('Мужской', 'М'), ('Женский', 'Ж'))


class ConsumerUserRegistrationSerializer(serializers.Serializer):
    # id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    city = serializers.CharField(max_length=100)
    email = serializers.EmailField(max_length=254)
    gender = serializers.ChoiceField(choices=GENDER)
    age = serializers.IntegerField(min_value=0)
    login = serializers.CharField(max_length=100)
    password = serializers.CharField(max_length=100)

class BusinessUserRegistrationSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    nickname = serializers.CharField(max_length=100)
    login = serializers.CharField(max_length=100)
    password = serializers.CharField(max_length=100)
