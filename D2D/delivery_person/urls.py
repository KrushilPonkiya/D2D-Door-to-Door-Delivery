from django.urls import path
from . import views

urlpatterns = [
    path('', views.deliverydashboard, name='delivery_dashboard'),
    path('ongoing', views.deliveryongoing, name='ongoing'),
    path('rejected', views.deliveryrejected, name='rejected'),
    path('completed', views.deliverycompleted, name='completed'),
    path('notifications', views.deliverynotifications, name='notifications'),
    path('user', views.deliveryuser, name='user'),
    path('feedback', views.handlefeedback, name='feedback'),
]