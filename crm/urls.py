from django.urls import path,include
from . import views

urlpatterns=[
    path("",views.home,name="home"),
        path("logout/",views.logout_user,name="logout"),
        path("register/",views.register,name="register"),
        path("customer/<int:pk>",views.showCustomer,name="showCustomer"),
        path("user/<int:pk>",views.showUser,name="showUser"),
        path("registerCustomer/",views.registerCustomer,name="registerCustomer"),
        path("updateCustomer/<int:pk>/",views.updateCustomer,name="updateCustomer"),
        path("customers/",views.customers,name="customers"),
                path("delete/<int:pk>",views.deleteCustomer,name="deleteCustomer"),






]