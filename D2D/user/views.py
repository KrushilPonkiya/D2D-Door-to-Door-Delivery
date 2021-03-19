from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import Feedback


# Create your views here.



def userdashboard(request):
    if request.user.is_authenticated:
        return render(request, 'user/dashboard.html')
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
            return redirect('userdashboard')
    else:
        return HttpResponse('404 - Not Found')
