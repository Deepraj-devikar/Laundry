from django.contrib import admin
from .models import CustomerAddress, DeliveryBoyAddress, LaundryAddress

# Register your models here.
admin.site.register(CustomerAddress)
admin.site.register(DeliveryBoyAddress)
admin.site.register(LaundryAddress)