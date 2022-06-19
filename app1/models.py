from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Client(models.Model):
    adress = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Users(models.Model):
    login = models.ForeignKey(User, on_delete=models.CASCADE)

class Trading_Pairs(models.Model):
    buy = models.CharField(max_length=100)
    sell = models.CharField(max_length=100)

