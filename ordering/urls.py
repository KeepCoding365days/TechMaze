from django.contrib import admin
from django.urls import include, path
from . import views

app_name="ordering"
urlpatterns=[
    path("products/",views.home,name="products"),
    path("cart/",views.view_cart,name="view_cart"),
    path("checkout",views.checkout,name="checkout"),
    path ("Favourites",views.view_fvrts,name="view_fvrts"),
    path("Orders",views.order_cust_view,name="order_cust_view")
]