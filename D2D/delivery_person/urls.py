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
    path('viewpendingorders/<str:pk_test>/',views.viewpendingorders, name='viewpendingorders'),
    path('viewongoingorders/<str:pk_ongoing>/',views.viewongoingorders, name='viewongoingorders'),
    path('viewrejectedorders/<str:pk_rejected>/',views.viewrejectedorders, name='viewrejectedorders'),
    path('viewscompletedorders/<str:pk_completed>/',views.viewscompletedorders, name='viewscompletedorders'),
    path('hendlepending', views.hendlepending, name='hendlepending'),
    path('hendleongoing', views.hendleongoing, name='hendleongoing'),
]