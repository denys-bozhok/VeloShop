# Generated by Django 4.2.5 on 2023-09-20 10:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_bicycle_year'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(auto_created=True, editable=False, max_length=30)),
                ('name', models.CharField(max_length=20, unique=True)),
                ('image', models.FileField(upload_to='images/categories/')),
                ('description', models.TextField(blank=True, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.category')),
            ],
        ),
        migrations.AddField(
            model_name='bicycle',
            name='subcategory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app.subcategory'),
        ),
        migrations.AddField(
            model_name='helmet',
            name='subcategory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app.subcategory'),
        ),
        migrations.AddField(
            model_name='lighting',
            name='subcategory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app.subcategory'),
        ),
    ]
