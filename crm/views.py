from django.shortcuts import render, HttpResponse,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from .forms import SignUpForm
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
        return render(request,"home.html")
def logout_user(request):
    logout(request)
    return render(request,'home.html')


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
    
    

