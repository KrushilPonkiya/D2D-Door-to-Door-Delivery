from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.forms import User
from django.contrib import messages
from .models import *
# Create your views here.
# from delivery_person.models import Order , Ongoing
from D2D.decorators import allowed_users


@login_required(login_url='/D2D-Login?')
@allowed_users(allowed_roles=['Delivery_person'])
def deliverydashboard(request):
    order = Order.objects.all()
    return render(request, 'deliveryperson/dashboard.html', {'order' : order})



@login_required(login_url='/D2D-Login?')
@allowed_users(allowed_roles=['Delivery_person'])
def deliveryongoing(request):
    ongoing = Ongoing.objects.all()
    return render(request, 'deliveryperson/ongoing.html', {'ongoing' : ongoing})


@login_required(login_url='/D2D-Login?')
@allowed_users(allowed_roles=['Delivery_person'])
def deliveryrejected(request):
    rejected = Rejected.objects.all()
    return render(request, 'deliveryperson/rejected.html', {'rejected': rejected})


@login_required(login_url='/D2D-Login?')
@allowed_users(allowed_roles=['Delivery_person'])
def deliverycompleted(request):
    completed = Completed.objects.all()
    return render(request, 'deliveryperson/completed.html', {'completed' : completed})


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


@login_required(login_url='/D2D-Login?')
@allowed_users(allowed_roles=['Delivery_person'])
def viewpendingorders(request, pk_test):
    order = Order.objects.get(id=pk_test)
    return render(request, 'viewpendingorders.html', {'ord' : order})


def hendlepending(request):
    if request.method == 'POST':
        orderid = request.POST.get('id') 
        status= request.POST.get('status')
        if status=='OnGoing':
            on = Ongoing()
            on.sender_name = request.POST['sender_name']
            on.receiver_name = request.POST['receiver_name']
            on.product_name = request.POST['product_name']
            on.product_weight = request.POST['product_weight']
            on.contact_number = request.POST['contact_number']
            on.pickup_address = request.POST['pickup_address']
            on.delivery_address = request.POST['delivery_address']
            on.delivery_city = request.POST['delivery_city']
            on.DateTime = request.POST['DateTime']
            on.save()
            Order.objects.filter(id=orderid).delete()
            messages.success(request, "Status updated to ongoing")
            return redirect("ongoing")
        elif status == 'Rejected':
            r = Rejected()
            r.sender_name = request.POST['sender_name']
            r.receiver_name = request.POST['receiver_name']
            r.product_name = request.POST['product_name']
            r.product_weight = request.POST['product_weight']
            r.contact_number = request.POST['contact_number']
            r.pickup_address = request.POST['pickup_address']
            r.delivery_address = request.POST['delivery_address']
            r.delivery_city = request.POST['delivery_city']
            r.DateTime = request.POST['DateTime']
            r.save()
            Order.objects.filter(id=orderid).delete()
            messages.success(request, "Status updated to rejected")
            return redirect("rejected")
        else:
            return redirect('delivery_dashboard')
    else:
        return HttpResponse('404 - Not Found')



@login_required(login_url='/D2D-Login?')
@allowed_users(allowed_roles=['Delivery_person'])
def viewrejectedorders(request, pk_rejected):
    rejected = Rejected.objects.get(id=pk_rejected)
    return render(request, 'viewrejectedorders.html', {'orderre' : rejected})


@login_required(login_url='/D2D-Login?')
@allowed_users(allowed_roles=['Delivery_person'])
def viewscompletedorders(request, pk_completed):
    completed = Completed.objects.get(id=pk_completed)
    return render(request, 'viewscompletedorders.html', {'orderco' : completed})


@login_required(login_url='/D2D-Login?')
@allowed_users(allowed_roles=['Delivery_person'])
def viewongoingorders(request, pk_ongoing):
    ongoing = Ongoing.objects.get(id=pk_ongoing)
    return render(request, 'viewongoingorders.html', {'ondergo' : ongoing})


def hendleongoing(request):
    if request.method == 'POST':
        ongoing = request.POST.get('id')
        status= request.POST.get('status')
        if status=='completed':
            co = Completed()
            co.sender_name = request.POST['sender_name']
            co.receiver_name = request.POST['receiver_name']
            co.product_name = request.POST['product_name']
            co.product_weight = request.POST['product_weight']
            co.contact_number = request.POST['contact_number']
            co.pickup_address = request.POST['pickup_address']
            co.delivery_address = request.POST['delivery_address']
            co.delivery_city = request.POST['delivery_city']
            co.DateTime = request.POST['DateTime']
            co.save()
            Ongoing.objects.filter(id=ongoing).delete()
            messages.success(request, "Status updated to ongoing")
            return redirect("completed")
