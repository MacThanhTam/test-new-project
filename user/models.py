from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomerUser(AbstractUser):
    phone_number = models.CharField(default='',max_length=20)
    address = models.CharField(max_length=200,default='')
