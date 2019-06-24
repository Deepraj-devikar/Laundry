from django.contrib import admin

from .models import Request, ItemCount, RequestComplition

# Register your models here.
admin.site.register(Request)
admin.site.register(ItemCount)
admin.site.register(RequestComplition)