from django.core import validators
from django.db import models


class Subject(models.Model):
    name = models.CharField(
        validators=[
            validators.MinLengthValidator(2)
        ],
        null=False,
        blank=False
    )

    description = models.CharField(
        validators=[
            validators.MinLengthValidator(2)
        ],
        null=False,
        blank=False,
        default="This subject doesn't have a description yet."
    )


class Topic(models.Model):
    name = models.CharField(
        validators=[
            validators.MinLengthValidator(2)
        ],
        null=False,
        blank=False
    )

    subject = models.ForeignKey(
        to='Subject',
        on_delete=models.CASCADE
    )
