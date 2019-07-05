from django.shortcuts import render
from django.http import HttpResponse

from registration.models import Customer
# Create your views here.

def home_view(request, *args, **kwargs):
	customer_name = 'blank'
	is_login = request.session.get('is_login', False)
	if is_login:
		customer_id = request.session.get('customer_id')
		customer_obj = Customer.objects.get(pk = customer_id)
		customer_name = customer_obj.name
	context = {
		'is_login': is_login,
		'customer_name': customer_name,
	}
	return render(request, "home.html", context)

def order_view(request, *args, **kwargs):
	customer_name = 'blank'
	is_login = request.session.get('is_login', False)
	if is_login:
		customer_id = request.session.get('customer_id')
		customer_obj = Customer.objects.get(pk = customer_id)
		customer_name = customer_obj.name
	context = {
		'is_login': is_login,
		'customer_name': customer_name,
	}
	return render(request, "order.html", context)

def price_view(request, *args, **kwargs):
	customer_name = 'blank'
	is_login = request.session.get('is_login', False)
	if is_login:
		customer_id = request.session.get('customer_id')
		customer_obj = Customer.objects.get(pk = customer_id)
		customer_name = customer_obj.name
	context = {
		'is_login': is_login,
		'customer_name': customer_name,
	}
	return render(request, "price.html", context)

