# Generated by Django 3.0.5 on 2020-04-19 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='service_quality_assessment',
            field=models.IntegerField(default=None),
        ),
        migrations.AddField(
            model_name='order',
            name='time_of_order',
            field=models.TimeField(default=None),
        ),
    ]
