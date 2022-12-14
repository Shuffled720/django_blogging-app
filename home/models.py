from email.policy import default
from sqlite3 import Timestamp
from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now


# Create your models here.

class Contact(models.Model):
    sno= models.AutoField(primary_key=True)
    name=models.CharField(max_length=200)
    email=models.CharField(max_length=50)
    phone=models.CharField(max_length=13)
    content=models.TextField()
    timeStamp=models.DateTimeField(default=now)

    def __str__(self):
        return'Message from '+ self.name +' - '+ self.email


    



