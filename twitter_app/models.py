from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Twitt(models.Model):
    content = models.CharField(max_length=140)
    creation_date = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User)

class Messages(models.Model):
    message = models.TextField()
    sender = models.ForeignKey(User, related_name='sender')
    reciever = models.ForeignKey(User, related_name='reciever')
    msg_date= models.DateTimeField(auto_now=True)
    readed =  models.BooleanField()