from django import forms
from django.forms import ModelForm


from .models import Customer


class CustomerRegistrationForm(ModelForm):
	class Meta:
		model = Customer
		fields = [
			'name',
			'email',
			'mobile',
			'password'
		]
		
class CustomerLoginForm(forms.Form):
	email_or_mobile = forms.CharField(max_length = 50)
	password = forms.CharField(max_length = 20)	