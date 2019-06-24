from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def home_view(request, *args, **kwargs):
	return render(request, "home.html", {})

def order_view(request, *args, **kwargs):
	return render(request, "order.html", {})

def price_view(request, *args, **kwargs):
	return render(request, "price.html", {})