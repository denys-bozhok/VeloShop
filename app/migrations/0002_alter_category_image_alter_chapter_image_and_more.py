# Generated by Django 4.2.5 on 2023-09-30 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.FileField(upload_to='images/icons/categories/'),
        ),
        migrations.AlterField(
            model_name='chapter',
            name='image',
            field=models.FileField(upload_to='images/icons/categories/'),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='image',
            field=models.FileField(upload_to='images/icons/categories/'),
        ),
    ]
