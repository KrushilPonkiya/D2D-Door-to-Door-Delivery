from django.contrib.auth import authenticate, login, logout
from django import forms
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.forms import User
from django.contrib import messages
from .models import *


# Create your views here.


def deliverydashboard(request):
    return render(request, 'deliveryperson/dashboard.html')


def handlefeedback(request):
    if request.method == 'POST':
        if request.POST.get('cf-name') and request.POST.get('cf-email') and request.POST.get('cf-message'):
            feedback = Feedback()
            feedback.name = request.POST['cf-name']
            feedback.email = request.POST['cf-email']
            feedback.message = request.POST['cf-message']
            feedback.save()
            messages.success(request, "Thank you for your feedback")
            return redirect('delivery_dashboard')
    else:
        return HttpResponse('404 - Not Found')

