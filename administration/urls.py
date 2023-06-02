from django.urls import path,include
from . import views

app_name="administration"

urlpatterns=[
    path("AccessDenied/",views.AccessDenied,name="AccessDenied"),
    path("",views.index,name="index"),
    path("verify_sellers/",views.verify_sellers,name="verify_sellers"),
]
