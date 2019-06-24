from django.forms import ModelForm


from .models import CustomerAddress


class CustomerAddressForm(ModelForm):
	class Meta:
		model = CustomerAddress
		fields = [
			'house_no',
			'street_area_locality',
			'state',
			'town_village_city',
			'pincode',
			'customer'
		]	