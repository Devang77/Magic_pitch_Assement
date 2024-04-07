from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    email=models.EmailField(max_length=254,null=True,blank=True)
    password=models.CharField(max_length=100,null=True,blank=True)
    referal_code=models.CharField(max_length=100,null=True,blank=True,unique=True)
    points=models.IntegerField(null=True,blank=True,default=0)
    referal_code_used=models.CharField(max_length=100,null=True,blank=True)
class Valid_token(models.Model):
    datetime = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    token = models.CharField(max_length=400,null=True,blank=True)
    userid = models.CharField(max_length=200,null=True,blank=True)