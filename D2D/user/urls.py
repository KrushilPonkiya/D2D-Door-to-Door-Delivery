from django.urls import path
from . import views

urlpatterns = [
    path('', views.userdashboard, name='userdashboard'),
    path('feedback', views.handlefeedback, name='feedback'),
    path('requestpackege', views.requestpackage, name='requestpackege'),
    path('sendpackage', views.sendpackage, name='sendpackage'),

    path('handlerequestpackage', views.handlerequestpackage, name='handlerequestpackage'),
    path('handlesendpackage', views.handlesendpackage, name='handlesendpackage'),



]
