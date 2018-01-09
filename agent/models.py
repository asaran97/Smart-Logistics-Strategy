from django.db import models
from django.contrib.auth.models import User
from hubdata.models import Hub
# Create your models here.


class agentMapping(models.Model):
    agent = models.ForeignKey(User,on_delete=models.CASCADE)
    hub = models.ForeignKey(Hub, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.agent.username
