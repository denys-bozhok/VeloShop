# Generated by Django 4.2.5 on 2023-09-30 13:36

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import products.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bicycle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(auto_created=True, editable=False, max_length=30)),
                ('label', models.CharField(max_length=30)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField(blank=True, null=True)),
                ('article', models.CharField(max_length=30, unique=True)),
                ('rating', models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('value', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('image', models.FileField(blank=True, upload_to=products.models.products_filename_wrapper)),
                ('suspension', models.BooleanField(default=False)),
                ('year', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(2000)])),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app.category')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Characteristic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_color', models.CharField(max_length=10)),
                ('second_color', models.CharField(blank=True, max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Hamlet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(auto_created=True, editable=False, max_length=30)),
                ('label', models.CharField(max_length=30)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField(blank=True, null=True)),
                ('article', models.CharField(max_length=30, unique=True)),
                ('rating', models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('value', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('image', models.FileField(blank=True, upload_to=products.models.products_filename_wrapper)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app.category')),
                ('characteristics', models.ManyToManyField(blank=True, to='products.characteristic')),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='products.color')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(auto_created=True, editable=False, max_length=30)),
                ('name', models.CharField(max_length=20, unique=True)),
                ('image', models.FileField(upload_to='images/manufactirers/')),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_name', models.CharField(max_length=5)),
                ('minimal', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('maximal', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
            ],
        ),
        migrations.CreateModel(
            name='SuspensionTravel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('suspension_travel', models.FloatField(validators=[django.core.validators.MinValueValidator(0)])),
            ],
        ),
        migrations.CreateModel(
            name='Weight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.FloatField(validators=[django.core.validators.MinValueValidator(0)])),
            ],
        ),
        migrations.CreateModel(
            name='WheelSize',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.DecimalField(decimal_places=1, max_digits=7, unique=True, validators=[django.core.validators.MinValueValidator(6)])),
            ],
        ),
        migrations.CreateModel(
            name='Lighting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(auto_created=True, editable=False, max_length=30)),
                ('label', models.CharField(max_length=30)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField(blank=True, null=True)),
                ('article', models.CharField(max_length=30, unique=True)),
                ('rating', models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('value', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('image', models.FileField(blank=True, upload_to=products.models.products_filename_wrapper)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app.category')),
                ('characteristics', models.ManyToManyField(blank=True, to='products.characteristic')),
                ('manufacturer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='products.manufacturer')),
                ('subcategory', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app.subcategory')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='HamletGalery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article', models.CharField(auto_created=True, editable=False, max_length=30)),
                ('image', models.FileField(blank=True, upload_to=products.models.products_filename_wrapper)),
                ('product', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='products.hamlet')),
            ],
        ),
        migrations.AddField(
            model_name='hamlet',
            name='manufacturer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='products.manufacturer'),
        ),
        migrations.AddField(
            model_name='hamlet',
            name='size',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='products.size'),
        ),
        migrations.AddField(
            model_name='hamlet',
            name='subcategory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app.subcategory'),
        ),
        migrations.AddField(
            model_name='hamlet',
            name='weight',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='products.weight'),
        ),
        migrations.CreateModel(
            name='BicycleGalery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article', models.CharField(auto_created=True, editable=False, max_length=30)),
                ('image', models.FileField(blank=True, upload_to=products.models.products_filename_wrapper)),
                ('product', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='products.bicycle')),
            ],
        ),
        migrations.AddField(
            model_name='bicycle',
            name='characteristics',
            field=models.ManyToManyField(blank=True, to='products.characteristic'),
        ),
        migrations.AddField(
            model_name='bicycle',
            name='color',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='products.color'),
        ),
        migrations.AddField(
            model_name='bicycle',
            name='frame_material',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='products.material'),
        ),
        migrations.AddField(
            model_name='bicycle',
            name='frame_size',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='products.size'),
        ),
        migrations.AddField(
            model_name='bicycle',
            name='manufacturer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='products.manufacturer'),
        ),
        migrations.AddField(
            model_name='bicycle',
            name='subcategory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app.subcategory'),
        ),
        migrations.AddField(
            model_name='bicycle',
            name='suspension_travel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='products.suspensiontravel'),
        ),
        migrations.AddField(
            model_name='bicycle',
            name='weight',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='products.weight'),
        ),
        migrations.AddField(
            model_name='bicycle',
            name='wheel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='products.wheelsize'),
        ),
    ]