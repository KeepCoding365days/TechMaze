from django.db import models
from Registration.models import seller_info

# Create your models here.
class Product(models.Model):

    name=models.CharField(max_length=20)
    Description=models.CharField(max_length=200)
    Price=models.IntegerField()
    Seller=models.ForeignKey(seller_info,on_delete=models.CASCADE)
    img=models.ImageField(upload_to='images/')


