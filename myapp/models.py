# myapp/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):

    phone_number = models.CharField(max_length=15)
    pin = models.CharField(max_length=6)
    
    def __str__(self):
        return self.username
