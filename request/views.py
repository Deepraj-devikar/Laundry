from django.shortcuts import redirect, render
from django import forms

from rateboard.models import Rates
from registration.models import Customer
from .forms import ItemCountForm, RequestComplitionForm, RequestForm
from .models import ItemCount, RequestComplition, Request

def request_view(request):
	customer_name = 'blank'
	is_login = request.session.get('is_login', False)
	if is_login:
		customer_id = request.session.get('customer_id')
		customer_obj = Customer.objects.get(pk = customer_id)
		customer_name = customer_obj.name
		if Request.objects.filter(customer = customer_obj, status = "not completed").exists():
			request_object = Request.objects.get(customer = customer_obj, status = "not completed")
			request_id = request_object.id
			form = ItemCountForm()
			context = {
				'form' : form,
				'request_id' : request_id,
				'is_login': is_login,
				'customer_name': customer_name,
			}
			print("not completed request found")
			return render(request, "item_count.html", context)
		else:
			form = RequestForm(request.POST or None)
			context = {
				'form': form,
				'is_login': is_login,
				'customer_name': customer_name,
			}
			print("all requests are completed")
			return render(request, "request.html", context)
	else:
		return redirect("/customer_registration")

def requesting_view(request):
	customer_name = 'blank'
	is_login = request.session.get('is_login', False)
	if is_login:
		customer_id = request.session.get('customer_id')
		customer_obj = Customer.objects.get(pk = customer_id)

	form = RequestForm(request.POST or None)
	if form.is_valid():
		requesting_data = request.POST.copy()
		request_type_value = requesting_data.get('request_type')
		query_value = requesting_data.get('query')
		request_obj = Request(customer = customer_obj, query = query_value)
		request_obj.save()

	return redirect("/")

def item_counting_view(request, request_value):
	form = ItemCountForm(request.POST or None)
	if form.is_valid():
		item_count_data = request.POST.copy()
		item_rate_value = item_count_data.get('item_rate')
		quantity_value = item_count_data.get('quantity')
		item_rate_obj = Rates.objects.get(pk = item_rate_value)
		request_obj = Request.objects.get(pk = request_value)
		item_count_obj = ItemCount(item_rate = item_rate_obj, quantity = quantity_value, request = request_obj)
		item_count_obj.save()

	print("it is in item counting view ", request_obj, item_rate_obj, quantity_value)
	return redirect("request")

def request_completing_view(request, request_value):
	request_obj = Request.objects.get(pk = request_value)
	request_obj.status = "completed"
	request_obj.save()
	return redirect("/")
