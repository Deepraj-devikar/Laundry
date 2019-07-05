from django.forms import ModelForm


from .models import ItemCount, RequestComplition, Request
from rateboard.models import Rates

class RequestForm(ModelForm):
	class Meta:
		model = Request
		fields = [
			'request_type',
			'query'
		]

class ItemCountForm(ModelForm):
	class Meta:
		model = ItemCount
		fields = [
			'item_rate',
			'quantity',
		]

class RequestComplitionForm(ModelForm):
	class Meta:
		model = RequestComplition
		fields = [
			'suggest_time',
		]
