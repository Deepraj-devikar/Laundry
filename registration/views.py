from django.shortcuts import render

from .forms import CustomerRegistrationForm
from .models import Customer

# Create your views here.
def customer_registration_view(request):
	form = CustomerRegistrationForm(request.POST or None)

	found_email = False
	found_mobile = False
	
	if form.is_valid():
		form_data = form.cleaned_data
		found_email = Customer.objects.filter(email = form_data['email']).exists()
		found_mobile = Customer.objects.filter(mobile = form_data['mobile']).exists()
		if found_email or found_mobile:
			pass
		else:
			form.save()
		
	form = CustomerRegistrationForm()

	context = {
		'form': form,
		'found_email': found_email,
		'found_mobile': found_mobile
	}

	return render(request, "customer_registration.html", context)


def customer_login_view(request):
	pass