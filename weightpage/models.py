from django.db import models


# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=30)

    def __str__(self):
        return self.username


class Weight(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    weight = models.FloatField(null=False)
    time = models.DateTimeField()


class SideBar(models.Model):
    title = models.CharField(max_length=30)
    icon = models.CharField(max_length=50)
    url = models.CharField(max_length=30, default="")

    def __str__(self):
        return self.title






