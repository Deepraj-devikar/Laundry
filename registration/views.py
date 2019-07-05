from django.shortcuts import redirect, render

from .forms import CustomerLoginForm, CustomerRegistrationForm
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
			customer_obj = Customer.objects.get(email = form_data['email'])
			request.session['customer_id'] = customer_obj.id 
			request.session['is_login'] = True
		
	form = CustomerRegistrationForm()

	context = {
		'form': form,
		'found_email': found_email,
		'found_mobile': found_mobile
	}

	return render(request, "customer_registration.html", context)


def customer_login_view(request):
	context = {
			'email_not_matched': False
		}
	return render(request, "customer_login.html", context)

def customer_logingin_view(request):
	login_data = request.POST.copy()
	login_email = login_data.get('email')
	login_password = login_data.get('password')
	if Customer.objects.filter(email = login_email, password = login_password).exists():
		customer_obj = Customer.objects.get(email = login_email)
		request.session['customer_id'] = customer_obj.id 
		request.session['is_login'] = True
		return redirect("/")
	else:
		context = {
			'email_not_matched': True
		}
		return render(request, "customer_login.html", context)
