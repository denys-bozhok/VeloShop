# Generated by Django 4.2.5 on 2023-09-30 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manufacturer',
            name='image',
            field=models.FileField(upload_to='images/manufactirers/'),
        ),
    ]
