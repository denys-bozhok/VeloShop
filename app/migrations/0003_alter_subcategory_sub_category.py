# Generated by Django 4.2.6 on 2023-10-14 18:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_subcategory_sub_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subcategory',
            name='sub_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app.subcategory'),
        ),
    ]
