from django.shortcuts import render
from .models import cart,favourites,Order
from seller.models import Product
from Registration.models import cust_info,seller_info
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,logout,login
from django.http import HttpResponseRedirect
from django.urls import reverse

def index(request):
    return render(request,"home.html",{})


def home(request):
    if request.user.is_authenticated:
        carts=cart.objects.all()
        fvrts=favourites.objects.all()
        found=False
        found_f=False
        for i in carts:
            if i.user==request.user:
                user_cart=i
                found=True
        for i in fvrts:
            if i.user==request.user:
                user_fvrt=i
                found_f=True
        if not found:
            user_cart=cart.objects.create(user=request.user)
        if not found_f:
            user_fvrt=favourites.objects.create(user=request.user)
        obj=Product.objects.all()
        if request.method=="POST":
            prod=request.POST.get("prod_id")
            desc=request.POST.get("decision")
            prod=Product.objects.get(id=prod)
            if desc=="Add to Cart":
                user_cart.Products.add(prod)
                user_cart.save()
            elif desc=="Remove from Cart":
                user_cart.Products.remove(prod)
                user_cart.save()
            elif desc=="Add to Favourites":
                user_fvrt.Products.add(prod)
                user_fvrt.save()
            elif desc=="Remove from Favourites":
                user_fvrt.Products.remove(prod)
                user_fvrt.save()
            return render(request,"Index.html",{"obj":obj,"Prod_c":user_cart.Products,"Prod_f":user_fvrt.Products})

        else:
            return render(request,"Index.html",{"obj":obj,"Prod_c":user_cart.Products,"Prod_f":user_fvrt.Products})
    else:
        return HttpResponseRedirect(reverse('registration:login'))

def view_cart(request):
    if request.user.is_authenticated:
        obj=cart.objects.all()
        for i in obj:
            if i.user==request.user:
                cart_user=i



        if request.method=="POST":
            prod_id=request.POST.get("prod_id")
            desc=request.POST.get("decision")
            if desc=="Remove from Cart":
                obj=Product.objects.get(id=prod_id)
                cart_user.Products.remove(obj)
                cart_user.save()
            price=0
            for i in cart_user.Products.all():
                price+=i.Price

            return render(request,"view_cart.html",{"prods":cart_user.Products,"price":price})
        else:
            price=0
            for i in cart_user.Products.all():
                price+=i.Price
            return render(request,"view_cart.html",{"prods":cart_user.Products,"price":price})
    else:
        return HttpResponseRedirect(reverse('registration:login'))

def view_fvrts(request):
    if request.user.is_authenticated:
        obj=favourites.objects.all()
        for i in obj:
            if i.user==request.user:
                fvrt_user=i
        obj=cart.objects.all()
        for i in obj:
            if i.user==request.user:
                cart_user=i


        if request.method=="POST":
            prod_id=request.POST.get("prod_id")
            desc=request.POST.get("decision")
            if desc=="Remove from Favourites":
                obj=Product.objects.get(id=prod_id)
                fvrt_user.Products.remove(obj)
                fvrt_user.save()
            elif desc=="Add to Cart":
                obj=Product.objects.get(id=prod_id)
                cart_user.Products.add(obj)
                cart_user.save()
            return render(request,"view_fvrts.html",{"prods":fvrt_user.Products})
        else:
            return render(request,"view_fvrts.html",{"prods":fvrt_user.Products})
    else:
        return HttpResponseRedirect(reverse('registration:login'))

def checkout(request):
    if request.user.is_authenticated:
        carts=cart.objects.all()
        found_c=False

        for i in carts:
            if i.user==request.user:
                cart_user=i
                found_c=True
        if not found_c:
            cart_user=None

        info= cust_info.objects.all()
        found_i=False
        price=0
        prods=cart_user.Products.all()
        if cart_user is not None:
            for i in cart_user.Products.all():
                price=price+i.Price

        for i in info:
            if i.user== request.user:
                info_user=i
                found_i=True

        if not found_i:
            info_user=cust_info.objects.create(user=request.user,address="Update your address",phone="00000")
        if request.method=="POST":
            name=request.POST.get("name")
            phone=request.POST.get("phone")
            address=request.POST.get("address")

            info_user.user.first_name=name
            info_user.phone=phone
            info_user.address=address

            info_user.save()
            first=True

            payment_method=request.POST.get("payment_method")

            order=Order.objects.create(Price=price,Status="Placed",Payment_Method=payment_method,cust_info=info_user)
            order.Products.set(cart_user.Products.all())
            for i in prods:
                order.Seller.add(i.Seller)
            order.save()
            cart_user.Products.clear()
            return render(request,"Order_Placed.html",{})
        else:
            return render(request,"checkout.html",{"cart":cart_user,"info":info_user,"price":price})


    else:
        return HttpResponseRedirect(reverse('registration:login'))

def order_cust_view(request):
    if request.user.is_authenticated:
        obj=Order.objects.all()
        return render(request,"order_cust.html",{"obj":obj})
    else:
        return HttpResponseRedirect(reverse('registration:login'))