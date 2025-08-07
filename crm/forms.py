from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Customer
class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="Email",widget=forms.TextInput)
    first_name = forms.CharField(label="First Name",max_length=100)
    last_name = forms.CharField(label="Last Name",max_length=100)



    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password1','password2')

 

class SignUpCustomer(UserCreationForm):
    email = forms.EmailField(label="Email",widget=forms.TextInput)
    first_name = forms.CharField(label="First Name",max_length=100)
    last_name = forms.CharField(label="Last Name",max_length=100)
    username = forms.EmailField(label="Username",widget=forms.TextInput)
    zipCode = forms.EmailField(label="Zip Code",widget=forms.TextInput)
    address = forms.EmailField(label="Address ",widget=forms.TextInput)



    class Meta:
        model = Customer
        fields = ('username','first_name','last_name','email','zipCode','address')
