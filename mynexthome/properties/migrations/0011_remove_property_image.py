# Generated by Django 4.1.7 on 2023-03-19 13:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0010_property_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='property',
            name='image',
        ),
    ]