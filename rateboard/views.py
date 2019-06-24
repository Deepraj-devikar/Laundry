from django.shortcuts import render

from rateboard.models import Rates 
# Create your views here.

def show_rate_board(request, *args, **kwargs):
	items_info = Rates.objects.all()
	context = {
		"items_info": items_info
	}
	return render(request, "price.html", context)
