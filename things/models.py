from django.contrib.auth.models import User
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Thing(models.Model):
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='thing_groups',  # Unique related name
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='thing_user_permissions',  # Unique related name
    )
    name = models.CharField(max_length=30, blank=False, unique=True)
    description= models.CharField(max_length=120, blank=True, unique=False)
    quantity = models.IntegerField(
        validators=[
            MinValueValidator(0),  # Ensures quantity is not less than 0
            MaxValueValidator(100) # Ensures quantity is not more than 100
        ],
        blank=False,  # Ensures quantity is not left blank, this is the default and can be omitted
        null=False,   # Ensures quantity is not NULL in the database, this is the default and can be omitted
    )

