from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator
from django.db import models


class Profile(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    firstName = models.CharField(
        max_length=20,
        validators=(
            MinLengthValidator(1),
        ),
    )
    lastName = models.CharField(
        max_length=20,
        validators=(
            MinLengthValidator(1),
        ),
    )
    facebook = models.URLField(
        max_length=200,
        blank=True,
        null=True,
    )
    email = models.CharField(
        max_length=200,
        blank=True,
        null=True,
    )
    website = models.URLField(
        max_length=200,
        blank=True,
        null=True,
    )
    phone = models.CharField(
        max_length=20,
        validators=(
            MinLengthValidator(10),
        ),
        blank=True,
        null=True,
    )
