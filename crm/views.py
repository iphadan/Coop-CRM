from django.shortcuts import render, HttpResponse,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from .forms import SignUpForm,SignUpCustomer
from django.contrib.auth.models import User
from . import models
# Create your views here.
def home(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request,username=username,password=password)
        if  user is not None:
            login(request,user)
            messages.success(request, "Login Successful!")
            return redirect('home')
        else:
           messages.error(request,"Login Failed!")
           return render(request,"home.html")
    else:
        if request.user.is_authenticated: 
            users = User.objects.all().order_by('id')
            context = {'users':users}
            return render(request,"home.html",context )
        
    return render(request,'home.html')
def logout_user(request):
    logout(request)
    return render(request,'home.html')

def customers(request):
        if request.user.is_authenticated: 
            customers = models.Customer.objects.all().order_by('id')

            context = {'customers':customers}
            return render(request,"customerTable.html",context)
        else:
            messages.error(request,'Login before !')
            return redirect('home')



def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid() : 
            form.save()
            messages.success(request,"Registration successful, please login!")
            return redirect('home')
        else:
            messages.error(request,"something went wrong, please try again!")
            return redirect('register')
    else:
        form = SignUpForm()
    return render(request,'register.html', context={'form':form})
    
    

def showUser(request,pk):
    if request.user.is_authenticated:
        user = User.objects.get(id=pk)
        if user is not None:
            context = {
                'user':user
            }
            return render(request,'showUser.html',context)
        
        else:
            messages.error(request,'user does not exist')
            return render(request,'home.html')
    return redirect('home')
def showCustomer(request,pk):
    if request.user.is_authenticated:
        customer = models.Customer.objects.get(id=pk)
        if customer is not None:
            context = {
                'customer':customer
            }
            return render(request,'showCustomer.html',context)
        
        else:
            messages.error(request,'Customer does not exist')
            return render(request,'home.html')
    return redirect('home')

def registerCustomer(request):
    form = SignUpCustomer(request.POST or None)
    if request.user.is_authenticated:
        if form:
            context = {
                    'form':form
                }
            if form.is_valid():
                form.save()
                messages.success(request,'Customer Registered Successfully')
                return redirect('home')
            else:
                messages.error(request,'Something went wrong, please try again')
                return render(request,'registerCustomer.html',context)

        else:
            return render(request,'registerCustomer.html',context)

    return redirect('home')


def updateCustomer(request,pk):
    customer = models.Customer.objects.get(id=pk)
    form = SignUpCustomer(request.POST or None,instance=customer)
    context = {
        'form':form,
        'id':customer.id
    }
    if request.user.is_authenticated:
        if form.is_valid():
            form.save()
            messages.success(request,'Customer Created Successfully')
            return redirect('home')
        else:
            messages.error(request,'something went wrong, please try again!')
            return render(request,'updateCustomer.html',context)
    else:
        messages.error(request,'please, login before!')
        return redirect('home')

def deleteCustomer(request):
    pass