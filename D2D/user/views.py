import datetime
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import *
from D2D.decorators import allowed_users
from delivery_person.models import Order

# Create your views here.
@login_required(login_url='/D2D-Login?')
@allowed_users(allowed_roles=['Users'])
def userdashboard(request):
    return render(request, 'user/dashboard.html')


@login_required(login_url='/D2D-Login?')
@allowed_users(allowed_roles=['Users'])
def requestpackage(request):
    return render(request, 'user/receive.html')


def handlerequestpackage(request):
    if request.method == 'POST':
        if request.POST.get('My_username') and request.POST.get('sender_username') and request.POST.get('product_name') and request.POST.get('product_weight') and request.POST.get('number') and request.POST.get('pickup_add') and request.POST.get('delivery_add') and request.POST.get('city'):
            requestpackage = Requestpackage()
            o = Order()
            requestpackage.requester_name = request.POST['My_username']
            requestpackage.sender_name = request.POST['sender_username']
            requestpackage.product_name = request.POST['product_name']
            requestpackage.product_weight = request.POST['product_weight']
            requestpackage.Contact_number = request.POST['number']
            requestpackage.pickup_address = request.POST['pickup_add']
            requestpackage.delivery_address = request.POST['delivery_add']
            requestpackage.delivery_city = request.POST['city']
            requestpackage.DateTime = datetime.datetime.now()
            o.requester_name = request.POST['My_username']
            o.sender_username = request.POST['sender_username']
            o.product_name = request.POST['product_name']
            o.product_weight = request.POST['product_weight']
            o.contact_number = request.POST['number']
            o.pickup_address = request.POST['pickup_add']
            o.delivery_address = request.POST['delivery_add']
            o.delivery_city = request.POST['city']
            o.DateTime = datetime.datetime.now()
            requestpackage.save()
            o.save()
            messages.success(request, "Requesting Package request send successfully")
            return redirect('userdashboard')
    return HttpResponse('404 - Not Found')


@login_required(login_url='/D2D-Login?')
@allowed_users(allowed_roles=['Users'])
def sendpackage(request):
    return render(request, 'user/sendPackage.html')


def handlesendpackage(request):
    if request.method == 'POST':
        if request.POST.get('rec_username') and request.POST.get('product_name') and request.POST.get(
                'product_weight') and request.POST.get('number') and request.POST.get(
                'pickup_add') and request.POST.get('delivery_add') and request.POST.get('city'):
            receivepackag = Sendpackage()
            o = Order()
            receivepackag.sender_name = request.POST['My_username']
            receivepackag.receiver_name = request.POST['rec_username']
            receivepackag.product_name = request.POST['product_name']
            receivepackag.product_weight = request.POST['product_weight']
            receivepackag.Contact_number = request.POST['number']
            receivepackag.pickup_address = request.POST['pickup_add']
            receivepackag.delivery_address = request.POST['delivery_add']
            receivepackag.delivery_city = request.POST['city']
            receivepackag.DateTime = datetime.datetime.now()
            o.sender_name = request.POST['My_username']
            o.receiver_name = request.POST['rec_username']
            o.product_name = request.POST['product_name']
            o.product_weight = request.POST['product_weight']
            o.contact_number = request.POST['number']
            o.pickup_address = request.POST['pickup_add']
            o.delivery_address = request.POST['delivery_add']
            o.deliverycity = request.POST['city']
            o.DateTime = datetime.datetime.now()
            receivepackag.save()
            o.save()
            messages.success(request, "Sending package request send successfully")
            return redirect('userdashboard')
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
            return redirect('userdashboard')
    else:
        return HttpResponse('404 - Not Found')
