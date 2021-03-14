from django.urls import path
from . import views

urlpatterns = [
    path('', views.userdashboard, name='userdashboard'),
    path('feedback', views.handlefeedback, name='feedback'),

]
