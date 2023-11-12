from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

class Thing(models.Model):
    name = models.CharField(
        max_length=30,            # Maximum length of 30 characters
        unique=True,              # Name must be unique
        blank=False               # Name must not be blank
    )
    description = models.CharField(
        max_length=120,           # Maximum length of 120 characters
        unique=False,             # Description does not need to be unique
        blank=True                # Description can be blank
    )
    quantity = models.IntegerField(
        validators=[
            MinValueValidator(0),  # Minimum value of 0
            MaxValueValidator(100) # Maximum value of 100
        ],
        unique=False,              # Quantity does not need to be unique
        blank=False                # Quantity must not be blank
    )
