from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from D2D.decorators import allowed_users


class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User, on_delete=models.CASCADE,default="")
    # The additional attributes we wish to include.
    Phone_Number = models.CharField(max_length=12,default="")
    # Override the __unicode__() method to return out something meaningful!

    def __str__(self):
        return self.user.username
        # return "{0} {1}".format(self.user.username, self.user.first_name)


# @allowed_users(allowed_roles=['Users'])
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    # UserProfile.Phone_Number.get('number')
    if created:
        UserProfile.objects.create(user=instance)
    else:
        instance.userprofile.save()
    

# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.userprofile.save()



class Feedback(models.Model):
    feedback_id = models.AutoField
    name = models.CharField(max_length=50, default="")
    email = models.CharField(max_length=50, default="")
    message = models.CharField(max_length=500)

    def __str__(self):
        return self.name


class Requestpackage(models.Model):
    request_id = models.AutoField
    requester_name = models.CharField(max_length=50, default="")
    sender_name = models.CharField(max_length=50)
    product_name = models.CharField(max_length=50)
    product_weight = models.IntegerField(default="0")
    Contact_number = models.IntegerField(default="0")
    pickup_address = models.TextField(max_length=250)
    delivery_address = models.TextField(max_length=250)
    delivery_city = models.TextField(max_length=50, default="0")
    DateTime =  models.DateTimeField(auto_now=True)


class Sendpackage(models.Model):
    sendpackage_id = models.AutoField
    sender_name = models.CharField(max_length=50, default="")
    receiver_name = models.CharField(max_length=50)
    product_name = models.CharField(max_length=50)
    product_weight = models.IntegerField(default="0")
    Contact_number = models.IntegerField(default="0")
    pickup_address = models.TextField(max_length=250)
    delivery_address = models.TextField(max_length=250)
    delivery_city = models.TextField(max_length=50, default="0")
    DateTime =  models.DateTimeField(auto_now=True)
