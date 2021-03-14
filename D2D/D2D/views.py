# I created this file - Krushil.
from django.contrib.auth import authenticate, login, logout
from django import forms
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect


def index(request):
    return render(request, 'index.html')


def handlesignup(request):
    if request.method == 'POST':
        # Get the post paraameters
        username = request.POST.get('username')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        tel = request.POST.get('tel')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')

        # Check for errirneous inputs
        # if email and User.objects.filter(email == email).exclude(username == username).exists():
        #     messages.error(request, "Enter Unique Username")
        #     raise forms.ValidationError("Email , username , tel must be unique")

        if len(username) > 10:
            messages.error(request, "Username must under 10 characters")

        if not username.isalnum():
            messages.error(request, "Username should only contain letters and numbers")
            return redirect("home")

        if pass1 != pass2:
            messages.error(request, "Passwords do not match")
            return redirect("home")
        # Create the user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.phone_number = tel
        # myuser.User_Type = radio
        myuser.save()
        messages.success(request, "Your D2D account has been successfully created")
        return redirect('home')
    else:
        return HttpResponse('404 - Not Found')


def handlelogin(request):
    if request.method == 'POST':
        loginusername = request.POST['loginusername']
        loginpass = request.POST['loginpass']
        # logincheck = request.POST['logincheck']
        user = authenticate(username=loginusername, password=loginpass)
        if user is not None:
            login(request, user)
            messages.success(request, "You are successfully Logged In")
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid credentials, Please try again")
            return redirect('home')
    return HttpResponse('404 - Not Found')


def handlelogout(request):
    logout(request)
    messages.success(request, "Successfully Logged Out")
    return redirect('home')

