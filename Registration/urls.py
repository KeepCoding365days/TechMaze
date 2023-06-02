from django.contrib import admin
from django.urls import include, path
from . import views

app_name="registration"
urlpatterns=[
    path("register/",views.Register,name="register"),
    path("login/",views.Login,name="login"),
    path("loginFailed/",views.login_failed,name="login_failed"),
    path("logout/",views.logout_view,name="logout_view"),
    path("SellerRegistration",views.seller_registration,name="seller_registration"),
    path("SuccesfullyApplied",views.seller_reg_thanks,name="seller_reg_thanks")

]