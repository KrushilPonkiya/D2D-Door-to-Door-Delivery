from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.forms import User
from django.contrib import messages
from .models import *
# Create your views here.
from user.models import Requestpackage, Sendpackage
from D2D.decorators import allowed_users


@login_required(login_url='/D2D-Login?')
@allowed_users(allowed_roles=['Delivery_person'])
# @user_passes_test(lambda u: u.groups.filter(name='Delivery_person').exists().count==0,   login_url='/user')
def deliverydashboard(request):
    requestpackage = Requestpackage.objects.all()
    sendpackage = Sendpackage.objects.all()
    return render(request, 'deliveryperson/dashboard.html', {'r_p':requestpackage, 's_p':sendpackage})


@login_required(login_url='/D2D-Login?')
@allowed_users(allowed_roles=['Delivery_person'])
def deliveryongoing(request):
    if request.user.is_authenticated:
        return render(request, 'deliveryperson/ongoing.html')
    else:
        return HttpResponse('404 - Not Found')


@login_required(login_url='/D2D-Login?')
@allowed_users(allowed_roles=['Delivery_person'])
def deliveryrejected(request):
    if request.user.is_authenticated:
        return render(request, 'deliveryperson/rejected.html')
    else:
        return HttpResponse('404 - Not Found')


@login_required(login_url='/D2D-Login?')
@allowed_users(allowed_roles=['Delivery_person'])
def deliverycompleted(request):
    return render(request, 'deliveryperson/completed.html')


@login_required(login_url='/D2D-Login?')
@allowed_users(allowed_roles=['Delivery_person'])
def deliverynotifications(request):
    return render(request, 'deliveryperson/notifications.html')


@login_required(login_url='/D2D-Login?')
@allowed_users(allowed_roles=['Delivery_person'])
def deliveryuser(request):
    return render(request, 'deliveryperson/user.html')


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


def handleorder(request):
    receiveorder = Order.Requestpackage.objects.get.all()
    sendorder = Order.Sendackage.objects.get.all()
    parms = receiveorder + sendorder
    return render(request, 'deliveryperson/dashboard.html', parms)
