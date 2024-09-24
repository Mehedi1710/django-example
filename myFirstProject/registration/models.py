from django.db import models


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=20, blank=True)
    profession = models.CharField(max_length=30)