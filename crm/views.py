from django.shortcuts import render, HttpResponse,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages

# Create your views here.
def home(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request,username=username,password=password)
        if not user is None:
            login(request,user)
            messages.success(request, "Login Successful!")
            redirect('home')
        else:
           messages.error(request,"Login Failed!")
           return render(request,"home.html")
    else:
        return render(request,"home.html")
    
    

