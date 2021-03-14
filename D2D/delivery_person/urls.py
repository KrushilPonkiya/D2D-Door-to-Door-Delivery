from django.urls import path
from . import views

urlpatterns = [
    path('', views.deliverydashboard, name='delivery_dashboard'),
    path('feedback', views.handlefeedback, name='feedback'),

]