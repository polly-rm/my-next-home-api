# Generated by Django 4.1.7 on 2023-03-14 21:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='first_name',
            new_name='firstName',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='last_name',
            new_name='lastName',
        ),
    ]
