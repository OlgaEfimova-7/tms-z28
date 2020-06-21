from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserConsumer(models.Model):
    MALE = 'М'
    FEMALE = 'Ж'
    GENDER = [('Мужской', 'М'), ('Женский', 'Ж')]
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
    city = models.CharField(max_length=100, default='')
    gender = models.CharField(max_length=7, choices=GENDER)
    age = models.IntegerField()

    # @receiver(post_save, sender=User)
    # def create_user_profile(sender, instance, created, **kwargs):
    #     if created:
    #         UserConsumer.objects.create(user=instance)
    #
    # @receiver(post_save, sender=User)
    # def save_user_profile(sender, instance, **kwargs):
    #     instance.profile.save()


class ItemsOfExpenditure(models.Model):
    item = models.CharField(max_length=100)


class SubtypeOfItem(models.Model):
    subtype = models.CharField(max_length=100)
    item_id = models.ForeignKey(ItemsOfExpenditure, on_delete=models.CASCADE)


class Keywords(models.Model):
    keyword = models.CharField(max_length=100)
    subtype_id = models.ForeignKey(SubtypeOfItem, on_delete=models.CASCADE)


class SphereOfBusiness(models.Model):
    sphere = models.CharField(max_length=100)


class InstitutionKeywords(models.Model):
    institution = models.CharField(max_length=100)
    sphere_id = models.ForeignKey(SphereOfBusiness, null=True, blank=True, on_delete=models.SET_NULL)


class Cheque(models.Model):
    date = models.DateTimeField(auto_now=False)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)
    user_id = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    name_of_institution = models.CharField(max_length=100)
    institution_id = models.ForeignKey(InstitutionKeywords, null=True, blank=True, on_delete=models.SET_NULL)


class ChequePositions(models.Model):
    position = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    cheque_id = models.ForeignKey(Cheque, null=True, blank=True, on_delete=models.SET_NULL)
    subtype_id = models.ForeignKey(SubtypeOfItem, null=True, blank=True, on_delete=models.SET_NULL)


class UserBusiness(models.Model):
    nickname = models.CharField(max_length=100)
    login = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100, unique=True)
    sphere_id = models.ForeignKey(SphereOfBusiness, null=True, blank=True, on_delete=models.SET_NULL)
