from django.shortcuts import render
from .models import Product
from Registration.models import seller_info
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout,login
from ordering.models import Order
from django.http import HttpResponseRedirect
from django.urls import reverse

def index(request):
    if request.user.is_authenticated:
        if request.user.groups.last().name=="Sellers":
            return render(request,"SellerIndex.html",{})
        else:
            return HttpResponseRedirect(reverse('seller:AccessDenied'))
    else:
        return HttpResponseRedirect(reverse('registration:login'))
def not_authorized(request):
    return (request,"not_aauthorized.html",{})
def Add_Product(request):
    if request.method=="POST":
        name=request.POST.get("name")
        desc=request.POST.get("desc")
        Price=request.POST.get("price")
        obj=seller_info.objects.all()
        for i in obj:
            if i.user==request.user:
                seller=i

        img=request.FILES.get("img")
        img2=r"C:/Users/MMT/PycharmProjects/TechMaze/media"
        img2=img2+"/"

        obj=Product.objects.create(name=name,Description=desc,Price=Price,Seller=seller,img=img)
       # obj.img=img2+str(obj.img)
        #obj.save()
        return render(request,"Product_added.html",{})

    else:
        return render(request,"Add_Product.html",{})

def view_Orders(request):
    if request.user.is_authenticated:
        if request.user.groups.last().name=="Sellers":


            orders=Order.objects.all()
            seller=request.user
            obj=seller_info.objects.all()
            for i in obj:
                if i.user==seller:
                    seller=i
            if request.method=="POST":
                order_id=request.POST.get("OrderId")
                order=Order.objects.get(id=order_id)
                desc=request.POST.get("decision")
                order.Status=desc
                order.save()

                return render(request,"order_seller.html",{"orders":orders,"seller":seller})

            else:
                return render(request,"order_seller.html",{"orders":orders,"seller":seller})
        else:
            return HttpResponseRedirect(reverse('seller:AccessDenied'))

    else:
         return HttpResponseRedirect(reverse('registration:login'))



