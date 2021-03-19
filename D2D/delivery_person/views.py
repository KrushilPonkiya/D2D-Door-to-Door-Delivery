from django.contrib.auth import authenticate, login, logout
from django import forms
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.forms import User
from django.contrib import messages
from .models import *
# Create your views here.


def deliverydashboard(request):
    if request.user.is_authenticated:
        return render(request, 'deliveryperson/dashboard.html')
    else:
        return HttpResponse('404 - Not Found')

def deliveryongoing(request):
    if request.user.is_authenticated:
        return render(request, 'deliveryperson/ongoing.html')
    else:
        return HttpResponse('404 - Not Found')

def deliveryrejected(request):
    if request.user.is_authenticated:
        return render(request, 'deliveryperson/rejected.html')
    else:
        return HttpResponse('404 - Not Found')

def deliverycompleted(request):
    if request.user.is_authenticated:
        return render(request, 'deliveryperson/completed.html')
    else:
        return HttpResponse('404 - Not Found')

def deliverynotifications(request):
    if request.user.is_authenticated:
        return render(request, 'deliveryperson/notifications.html')
    else:
        return HttpResponse('404 - Not Found')

def deliveryuser(request):
    if request.user.is_authenticated:
        return render(request, 'deliveryperson/user.html')
    else:
        return HttpResponse('404 - Not Found')

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