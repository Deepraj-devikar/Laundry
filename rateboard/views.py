from django.shortcuts import render

from rateboard.models import Rates 
from registration.models import Customer
# Create your views here.

def show_rate_board(request, *args, **kwargs):
	customer_name = 'blank'
	is_login = request.session.get('is_login', False)
	if is_login:
		customer_id = request.session.get('customer_id')
		customer_obj = Customer.objects.get(pk = customer_id)
		customer_name = customer_obj.name
	items_info = Rates.objects.all()
	context = {
		"items_info": items_info,
		"is_login": is_login,
		"customer_name": customer_name,
	}
	return render(request, "price.html", context)
