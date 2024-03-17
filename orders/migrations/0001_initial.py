# Generated by Django 5.0.3 on 2024-03-16 17:08

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_title', models.CharField(max_length=50)),
                ('quantity', models.IntegerField(max_length=5)),
                ('cost', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='OrderStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner_name', models.CharField(max_length=50)),
                ('owner_surname', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('city', models.CharField(max_length=30)),
                ('adress', models.CharField(max_length=300)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(blank=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('info', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='orders.orderinfo', unique=True)),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='orders.orderstatus')),
            ],
        ),
    ]