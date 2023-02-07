from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Child(models.Model):
    name = models.CharField(max_length=200)
    about = models.CharField(max_length=500)
    is_onboarded = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return self.name
