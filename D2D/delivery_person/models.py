from django.db import models
# from user.models import *
from django.contrib.auth.models import User


class Feedback(models.Model):
    feedback_id = models.AutoField
    name = models.CharField(max_length=50, default="")
    email = models.CharField(max_length=50, default="")
    message = models.CharField(max_length=500)

    def __str__(self):
        return self.name


class Delivery_Person(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.TextField(max_length=250)
    phone_number = models.IntegerField()
    aadhaar = models.CharField(max_length=12)
    PAN_card = models.CharField(max_length=10)
    Rc_no = models.CharField(max_length=16)
    Driving_licence = models.CharField(max_length=16)


class Order(models.Model):
    order_id = models.AutoField
    requester_name = models.CharField(max_length=50, default="")
    sender_name = models.CharField(max_length=50, default="")
    receiver_name = models.CharField(max_length=50, default="")
    product_name = models.CharField(max_length=50, default="")
    product_weight = models.CharField(max_length=50, default="")
    contact_number = models.CharField(max_length=12, default="")
    pickup_address = models.TextField(max_length=250, default="")
    delivery_address = models.TextField(max_length=250, default="")
    delivery_city = models.TextField(max_length=50, default="")
    DateTime =  models.DateTimeField(auto_now=True)


class Ongoing(models.Model):
    ongoing_id = models.AutoField
    sender_name = models.CharField(max_length=50, default="")
    receiver_name = models.CharField(max_length=50, default="")
    product_name = models.CharField(max_length=50, default="")
    product_weight = models.CharField(max_length=50, default="")
    contact_number = models.CharField(max_length=12, default="")
    pickup_address = models.TextField(max_length=250, default="")
    delivery_address = models.TextField(max_length=250, default="")
    delivery_city = models.TextField(max_length=50, default="")
    DateTime =  models.DateTimeField(auto_now=True)


class Rejected(models.Model):
    rejected_id = models.AutoField
    sender_name = models.CharField(max_length=50, default="")
    receiver_name = models.CharField(max_length=50, default="")
    product_name = models.CharField(max_length=50, default="")
    product_weight = models.CharField(max_length=50, default="")
    contact_number = models.CharField(max_length=12, default="")
    pickup_address = models.TextField(max_length=250, default="")
    delivery_address = models.TextField(max_length=250, default="")
    delivery_city = models.TextField(max_length=50, default="")
    DateTime =  models.DateTimeField(auto_now=True)

class Completed(models.Model):
    completed_id = models.AutoField
    sender_name = models.CharField(max_length=50, default="")
    receiver_name = models.CharField(max_length=50, default="")
    product_name = models.CharField(max_length=50, default="")
    product_weight = models.CharField(max_length=50, default="")
    contact_number = models.CharField(max_length=12, default="")
    pickup_address = models.TextField(max_length=250, default="")
    delivery_address = models.TextField(max_length=250, default="")
    delivery_city = models.TextField(max_length=50, default="")
    DateTime =  models.DateTimeField(auto_now=True)
