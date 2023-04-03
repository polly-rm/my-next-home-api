from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MinLengthValidator
from django.db import models


class Property(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    title = models.CharField(
        max_length=20,
        validators=(
            MinLengthValidator(3),
        ),
    )
    price = models.FloatField(
        validators=(
            MinValueValidator(0),
        ),
    )
    imageUrl = models.URLField(
        max_length=200
    )
    city = models.CharField(
        max_length=20,
        validators=(
            MinLengthValidator(3),
        ),
    )
    address = models.CharField(
        max_length=50,
        validators=(
            MinLengthValidator(3),
        ),
    )
    description = models.TextField(
        validators=(
            MinLengthValidator(3),
        ),
    )
    type = models.CharField(
        max_length=20,
    )
    status = models.CharField(
        max_length=20,
    )
    floor  = models.IntegerField(
        validators=(
            MinValueValidator(0),
        ),
        blank=True,
        null=True,
    )
    storey  = models.IntegerField(
        validators=(
            MinValueValidator(0),
        ),
        blank=True,
        null=True,
    )
    area  = models.FloatField(
        validators=(
            MinValueValidator(0),
        ),
        blank=True,
        null=True,
    )
    yardArea  = models.FloatField(
        validators=(
            MinValueValidator(0),
        ),
        blank=True,
        null=True,
    )
    bedroom  = models.IntegerField(
        validators=(
            MinValueValidator(0),
        ),
        blank=True,
        null=True,
    )
    bathroom  = models.IntegerField(
        validators=(
            MinValueValidator(0),
        ),
        blank=True,
        null=True,
    )
    storage  = models.IntegerField(
        validators=(
            MinValueValidator(0),
        ),
        blank=True,
        null=True,
    )
    parking  = models.CharField(
        max_length=50,
        blank=True,
        null=True,
    )
    basement  = models.CharField(
        max_length=50,
        blank=True,
        null=True,
    )
    view = models.CharField(
        max_length=50,
        blank=True,
        null=True,
    )
    created_on = models.DateTimeField(
        auto_now_add=True
    )
    updated_on = models.DateTimeField(
        auto_now_add=True
    )
