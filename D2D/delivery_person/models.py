from django.db import models
#from user.models import *
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from D2D.decorators import allowed_users


class DeliveryPersonProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User, on_delete=models.CASCADE,default="")
    # The additional attributes we wish to include.
    Phone_Number = models.CharField(max_length=12,default="")
    Address =  models.TextField(max_length=250)
    Aadhaar_Number = models.CharField(max_length=12,default="")
    PAN_Number = models.CharField(max_length=10,default="")
    Driving_licence_number = models.CharField(max_length=16,default="")
    Vehicle_RC_number = models.CharField(max_length=16,default="")
    # Override the __unicode__() method to return out something meaningful!

    def __str__(self):
        return self.user.username

# @allowed_users(allowed_roles=['Delivery_person'])
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        DeliveryPersonProfile.objects.create(user=instance)
    else:
        instance.deliverypersonprofile.save()


class Feedback(models.Model):
    feedback_id = models.AutoField
    name = models.CharField(max_length=50, default="")
    email = models.CharField(max_length=50, default="")
    message = models.CharField(max_length=500)

    def __str__(self):
        return self.name



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
