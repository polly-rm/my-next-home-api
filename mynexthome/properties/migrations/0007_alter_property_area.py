# Generated by Django 4.1.7 on 2023-03-16 13:32

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0006_alter_property_area'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='area',
            field=models.FloatField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
