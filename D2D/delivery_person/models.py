from django.db import models
from user.models import *
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
    created = models.DateTimeField()
    requestpackage = models.ForeignKey(Requestpackage, on_delete=models.PROTECT, null=True, blank=True)
    sendackage = models.ForeignKey(Sendpackage, on_delete=models.PROTECT, null=True, blank=True)
