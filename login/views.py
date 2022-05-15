from datetime import datetime
from django.shortcuts import render, redirect
from . import forms
from .models import User, Password
import hashlib

# Create your views here.
def login(request):
    message = ""
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            femail = form.cleaned_data.get('email')
            fpassword = hashlib.sha256(str(form.cleaned_data.get('password')).encode('utf-8')).hexdigest()
            #если просто get(email = femail), то при несуществующем эмейле будет эксепшн
            current_user = User.objects.filter(email = femail).first()
            if current_user and Password.objects.get(userId = current_user).password == fpassword:
                return redirect ("main:main")
        message = 'Email or password is not correct'

    elif request.method == 'GET':
        form = forms.LoginForm()
    
    return render (request, "login.html", {'form': form, 'message': message})

#TODO add logic for existing user
def register(request):
    message = ""
    if request.method == 'POST':
        form = forms.RegisterForm(request.POST)
        if form.is_valid():
            fname = form.cleaned_data.get("name")
            fsurname = form.cleaned_data.get('surname')
            femail = form.cleaned_data.get('email')
            fpassword = hashlib.sha256(str(form.cleaned_data.get('password')).encode('utf-8')).hexdigest()
            #time provided automatically by db
            if User.objects.filter(email = femail).exists():
                message = 'This email is already used'
            else:
                user = User.objects.create(name=fname, surname = fsurname, email = femail)
                Password.objects.create(userId = user, password = fpassword)
                return redirect ("main:main")
    elif request.method == 'GET':
        form = forms.RegisterForm()
    
    return render (request, "register.html", {'form':form, 'message': message})

   

