from django.urls import path,include
from . import views

urlpatterns=[
    path("",views.home,name="home"),
        path("logout/",views.logout_user,name="logout"),
        path("register/",views.register,name="register"),
        path("customer/<pk>",views.showCustomer,name="showCustomer"),
        path("user/<pk>",views.showUser,name="showUser"),


]