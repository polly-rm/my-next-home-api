# Generated by Django 4.1.7 on 2023-04-18 22:43

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0013_alter_property_imageurl'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='area',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='property',
            name='yardArea',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]