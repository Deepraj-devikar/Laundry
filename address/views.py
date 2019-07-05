from django.shortcuts import redirect, render

from registration.models import Customer
from .forms import CustomerAddressForm
from .models import CustomerAddress

# Create your views here.
def customer_address_view(request):
	form = CustomerAddressForm(request.POST or None)

	if form.is_valid():
		form.save()
		
	form = CustomerAddressForm()

	customer_name = 'blank'
	is_login = request.session.get('is_login', False)
	if is_login:
		customer_id = request.session.get('customer_id')
		customer_obj = Customer.objects.get(pk = customer_id)
		customer_name = customer_obj.name
	else:
		return redirect("/customer_registration")

	context = {
		'form': form,
		'is_login': is_login,
		'customer_name': customer_name,
	}

	return render(request, "customer_address.html", context)
