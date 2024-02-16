from django.core import validators
from django.db import models

from accounts_users.models import AppUser


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

    def __str__(self):
        return self.name


class Topic(models.Model):

    name = models.CharField(
        validators=[
            validators.MinLengthValidator(2)
        ],
        null=False,
        blank=False
    )

    description = models.TextField(
        null=False,
        blank=False,
        max_length=350,
        validators=[
            validators.MinLengthValidator(3)
        ],
    )

    subject = models.ForeignKey(
        to='Subject',
        on_delete=models.CASCADE
    )

    user = models.ForeignKey(
        to=AppUser,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name


class Comment(models.Model):

    comment_text = models.CharField(
        max_length=350,
        validators=[
            validators.MinLengthValidator(2)
        ]
    )

    topic = models.ForeignKey(
        to='Topic',
        on_delete=models.CASCADE
    )

    user = models.ForeignKey(
        to=AppUser,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.comment_text
