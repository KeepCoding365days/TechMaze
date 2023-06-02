from django.contrib import admin
from django.urls import include, path
from . import views

app_name="seller"
urlpatterns=[
    path("",views.index,name="seller_index"),

    path("products/",views.index,name="index"),
    path("Add_Product/",views.Add_Product,name="Add_Product"),
    path("AccessDenied",views.not_authorized,name="AccessDenied"),
    path("Orders",views.view_Orders,name="Seller_order_view")

]