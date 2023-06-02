from django.db import models
from django.contrib.auth.models import User

class seller_info(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,unique=True)
    cnic=models.CharField(max_length=13,unique=True)
    address=models.CharField(max_length=50)
    phone=models.CharField(max_length=11,unique=True)

    def __str__(self):
        return f"Name:{self.user.username} cnic:{self.cnic}"

class cust_info(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,unique=True)
    address=models.CharField(max_length=50)
    phone=models.CharField(max_length=11,unique=True)
