from django.db import models


# Create your models here.
class UserDetail(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
