from django.shortcuts import redirect, render

from .forms import ItemCountForm, RequestComplitionForm, RequestForm
from .models import ItemCount, RequestComplition, Request

# Create your views here.
# def request_view(request):
# 	request_form = RequestForm(request.POST or None)
# 	if form.is_valid():
# 		request = request_form.save()
# 		return redirect('item_count', pk=request.id)
# 	request_form = RequestForm()
# 	context = {
# 		'form': request_form,
# 	}
# 	return render(request, "request.html", context)

# def item_count_view(request, request_id):
# 	item_count_form = ItemCountForm(request.POST or None)
# 	if form.is_valid():
# 		request = item_count_form.save()
# 		return redirect('item_count', pk=request.id)
# 	item_count_form = ItemCountForm()
# 	item_count_form.Meta.widgets = {
# 		'request' : 
# 	}
# 	context = {
# 		'form': item_count_form,
# 	}
# 	return render(request, "request.html", context)

