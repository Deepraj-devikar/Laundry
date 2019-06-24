from django.shortcuts import render

from .forms import CustomerAddressForm
from .models import CustomerAddress

# Create your views here.
def customer_address_view(request):
	form = CustomerAddressForm(request.POST or None)

	if form.is_valid():
		form.save()
		
	form = CustomerAddressForm()

	context = {
		'form': form,
	}

	return render(request, "customer_address.html", context)
