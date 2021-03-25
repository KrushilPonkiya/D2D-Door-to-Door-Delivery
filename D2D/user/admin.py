from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(Feedback)
admin.site.register(UserProfile)
admin.site.register(Requestpackage)
admin.site.register(Sendpackage)

