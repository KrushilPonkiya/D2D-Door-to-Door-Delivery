from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Feedback)
admin.site.register(DeliveryPersonProfile)
admin.site.register(Order)
admin.site.register(Ongoing)
admin.site.register(Rejected)
admin.site.register(Completed)

