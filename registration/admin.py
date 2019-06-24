from django.contrib import admin

from .models import Customer, DeliveryBoy

# Register your models here.
admin.site.register(Customer)
admin.site.register(DeliveryBoy)
