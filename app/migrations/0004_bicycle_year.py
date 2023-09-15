# Generated by Django 4.2.3 on 2023-09-14 21:41

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_manufacturer_bicycle_price_helmet_price_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bicycle',
            name='year',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(2000)]),
        ),
    ]