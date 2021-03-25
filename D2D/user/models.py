from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Feedback(models.Model):
    feedback_id = models.AutoField
    name = models.CharField(max_length=50, default="")
    email = models.CharField(max_length=50, default="")
    message = models.CharField(max_length=500)

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # The additional attributes we wish to include.
    Phone_Number = models.IntegerField(null=True, blank=True)
    # Override the __unicode__() method to return out something meaningful!


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    # UserProfile.Phone_Number.get('number')
    if created:
        UserProfile.objects.create(user=instance)
    instance.userprofile.save()


class Requestpackage(models.Model):
    request_id = models.AutoField
    requester_name = models.CharField(max_length=50,default="")
    sender_name = models.CharField(max_length=50)
    product_name = models.CharField(max_length=50)
    product_weight = models.IntegerField(default="0")
    Contact_number = models.IntegerField(default="0")
    pickup_address = models.TextField(max_length=250)
    delivery_address = models.TextField(max_length=250)


class Sendpackage(models.Model):
    sendpackage_id = models.AutoField
    sender_name = models.CharField(max_length=50, default="")
    receiver_name = models.CharField(max_length=50)
    product_name = models.CharField(max_length=50)
    product_weight = models.IntegerField(default="0")
    Contact_number = models.IntegerField(default="0")
    pickup_address = models.TextField(max_length=250)
    delivery_address = models.TextField(max_length=250)
