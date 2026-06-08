from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Users(models.Model):
    fullname=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    phone=models.CharField(max_length=50, default="")
    biopic=models.CharField(max_length=50, default="")
    AUTHUSER=models.OneToOneField(User,on_delete=models.CASCADE)

class Blog(models.Model):
    title=models.CharField(max_length=50)
    content=models.CharField(max_length=200)
    image=models.CharField(max_length=50, default="")
    status=models.CharField(max_length=20)
    USER=models.ForeignKey(Users,on_delete=models.CASCADE)

class comment(models.Model):
    BLOG=models.ForeignKey(Blog,on_delete=models.CASCADE)
    USER=models.ForeignKey(Users,on_delete=models.CASCADE)
    comment=models.CharField(max_length=200)