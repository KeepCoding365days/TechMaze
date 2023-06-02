from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User,Group
from Registration.models import seller_info
# Create your views here.

def AccessDenied(request):
    return render(request,"Denied.html",{})

@login_required
def index(request):
    if request.user.groups.last().name=="Admin":
        return render(request,"AdminIndex.html",{})
    else:
        return HttpResponseRedirect(reverse("administration:AccessDenied"))

@login_required
def verify_sellers(request):
    if request.user.groups.last().name=="Admin":
        if request.method=="POST":
            name=request.POST.get("username")
            decision=request.POST.get("decision")
            data= seller_info.objects.all()
            for i in data:
                if i.user.username==name:
                    grp=Group.objects.get(name="Sellers")
                    if decision=="Approve":
                        grp.user_set.add(i.user)
                        i.user.groups.remove(2) #bcz employees can be sellers admin grp id:2 seller:1
                    elif decision=="DisApprove":
                        #obj=seller_info.objects.get(user.username=name)
                        i.delete()

            data=seller_info.objects.all()
            context={"data":data}
            return render(request,"verify_sellers.html",context)
            #return HttpResponseRedirect(reverse("administration:verify_sellers"))
            #return render(request,"AdminIndex.html",{})
        else:
            data=seller_info.objects.all()
            context={"data":data}
            return render(request,"verify_sellers.html",context)
    else:
        return HttpResponseRedirect(reverse("administration:AccessDenied"))