from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

class Thing(models.Model):
    name = models.CharField(max_length=30, unique=True, blank=False)
    description = models.CharField(max_length=120, blank=True, unique=False)
    quantity = models.IntegerField(unique=False, validators=[MinValueValidator(0),MaxValueValidator(100)])
