from django.forms import ModelForm


from .models import ItemCount, RequestComplition, Request

class RequestForm(ModelForm):
	class Meta:
		model = Request
		fields = [
			'customer',
			'request_type',
			'query'
		]

class ItemCountForm(ModelForm):
	class Meta:
		model = ItemCount
		fields = [
			'item_rate',
			'quantity',
			'request'
		]

class RequestComplitionForm(ModelForm):
	class Meta:
		model = ItemCount
		fields = [
			'suggest_time',
		]
