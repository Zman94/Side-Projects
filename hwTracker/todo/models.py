from __future__ import unicode_literals
from django.db import models
from django.utils import timezone

class User(models.Model):
    username = models.CharField(max_length=100)
    pasword = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

# Create your models here.
