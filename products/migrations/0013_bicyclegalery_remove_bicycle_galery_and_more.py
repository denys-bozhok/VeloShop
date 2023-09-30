# Generated by Django 4.2.5 on 2023-09-30 02:58

from django.db import migrations, models
import django.db.models.deletion
import products.models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_remove_galery_product_bicycle_galery_helmet_galery_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='BicycleGalery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article', models.CharField(auto_created=True, editable=False, max_length=30)),
                ('image', models.FileField(blank=True, upload_to=products.models.products_filename_wrapper)),
            ],
        ),
        migrations.RemoveField(
            model_name='bicycle',
            name='galery',
        ),
        migrations.RemoveField(
            model_name='helmet',
            name='galery',
        ),
        migrations.RemoveField(
            model_name='lighting',
            name='galery',
        ),
        migrations.DeleteModel(
            name='Galery',
        ),
        migrations.AddField(
            model_name='bicyclegalery',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='products.bicycle'),
        ),
    ]
