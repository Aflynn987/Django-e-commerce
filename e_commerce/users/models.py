from django.db import models
from django.contrib.auth.models import AbstractUser

class User(models.Model):
    """Custom user model with additional fields"""
    # Add any additional fields you want to the user model here
    full_name = models.CharField(max_length=255)
    date_of_birth = models.DateField(null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.username