from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    pass

class Room(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    location = models.CharField(max_length=200)
    # Add other fields as per your requirements like pictures of 
    # room,

    def __str__(self):
        return f"{self.title} in {self.location}"
