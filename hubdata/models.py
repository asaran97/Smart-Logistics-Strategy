from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Hub(models.Model):
    name = models.CharField(max_length=20)
    lat = models.FloatField(default=0)
    long = models.FloatField(default=0)

    def __str__(self):
        return self.name


class orders(models.Model):
    product = models.IntegerField()
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.FloatField(default=0.0)
    lat = models.FloatField(default=0)
    long = models.FloatField(default=0)
    status = models.BooleanField(default=False)
    dstatus = models.BooleanField(default=False)
    email = models.EmailField(default="")
    hub = models.ForeignKey(Hub, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.product)
