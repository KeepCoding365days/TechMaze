from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout,login
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import seller_info
from seller.models import Product

# Create your views here.


def Register(request):
    if request.method=="POST":
        username=request.POST.get("username")
        name=request.POST.get("name")
        email=request.POST.get("email")
        password=request.POST.get("password")
        user=User.objects.create_user(username,email,password)
        user.first_name=name
        user.save()
        return HttpResponseRedirect(reverse('home'))

    else:
        return render(request,"Register.html",{})

def Login(request):
    if request.user.is_authenticated:
        return render(request,"LoggedIn.html",{})
    else:
        if request.method=="POST":
            username=request.POST.get("username")
            password=request.POST.get("password")
            user=authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user) #if user is admin redirecting to admin panel if seller redirecting to seller panel
                if user.groups.last()!=None: #otherwise redirecting to seller page.
                    if user.groups.last().name=='Admin':
                        return HttpResponseRedirect(reverse("administration:index"))
                    elif user.groups.last().name=='Sellers':
                        return HttpResponseRedirect(reverse("seller:index"))
                    else:
                        return HttpResponseRedirect(reverse('home'))
                else:
                    return HttpResponseRedirect(reverse('home'))
            else:
                return HttpResponseRedirect(reverse('registration:login_failed'))
        else:
            return render(request,"login.html",{})

@login_required
def seller_registration(request):
    data=request.user.groups.all()
    seller_check=False
    for i in data:
        if i.name=="Sellers":
            seller_check=True

    if seller_check:
        return render(request,"already_seller.html",{})

    elif request.method=="POST":
        data=User.objects.all()
        for i in data:
            if i==request.user:
                user=request.user

        address=request.POST.get("address")
        phone=request.POST.get("phone")
        cnic=request.POST.get("cnic")

        seller_info.objects.create(user=user,address=address,phone=phone,cnic=cnic)

        return HttpResponseRedirect(reverse("registration:seller_reg_thanks"))
    else:
        return render(request,"seller_reg_form.html",{})

def seller_reg_thanks(request):
    return render(request,"Thanks_seller.html",{})




def login_failed(request):
    return render(request,"login_failed.html",{})

def logout_view(request):
    logout(request)
    return render(request,"logout.html",{})
