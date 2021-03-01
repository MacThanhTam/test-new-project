from django.contrib import admin

# Register your models here.
from user.models import CustomerUser
admin.site.register(CustomerUser)