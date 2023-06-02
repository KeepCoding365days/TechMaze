from django.db import models
from seller.models import Product
from Registration.models import seller_info,cust_info
from django.contrib.auth.models import User

class cart(models.Model):
    Products=models.ManyToManyField(Product)
    user=models.ForeignKey(User,on_delete=models.CASCADE)

class favourites(models.Model):
    Products=models.ManyToManyField(Product)
    user=models.ForeignKey(User,on_delete=models.CASCADE)

class Order(models.Model):
    Products=models.ManyToManyField(Product)
    Seller=models.ManyToManyField(seller_info)
    Price=models.IntegerField()
    Status=models.CharField(max_length=20)
    Payment_Method=models.CharField(max_length=20)
    cust_info=models.ForeignKey(cust_info,on_delete=models.CASCADE)
