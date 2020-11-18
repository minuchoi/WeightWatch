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





