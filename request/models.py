from django.db import models

from registration.models import Customer, DeliveryBoy
from rateboard.models import Rates

import time
from datetime import datetime, date, time, timedelta
 
# Create your models here.
class Request(models.Model):
	customer 		= models.ForeignKey(Customer, on_delete=models.CASCADE)
	delivery_boy 	= models.ForeignKey(DeliveryBoy, on_delete=models.CASCADE, null = True, blank = True)
	request_type 	= models.CharField(max_length = 20, default = "collecting") # (1) "returning"
	status			= models.CharField(max_length = 20, default = "not completed") # (1) "completed"
	query 			= models.TextField(max_length = 250)

	def __str__(self):
		if self.request_type == "collecting":
			return '{} is {} from {} task {}'.format(self.delivery_boy, self.request_type, self.customer, self.status)
		elif self.request_type == "returning":
			return '{} is {} to {} task {}'.format(self.delivery_boy, self.request_type, self.customer, self.status)

class ItemCount(models.Model):
	item_rate 	= models.ForeignKey(Rates, on_delete=models.CASCADE)
	quantity 	= models.IntegerField(default = 1)
	request 	= models.ForeignKey(Request, on_delete = models.CASCADE, blank = True)

	def __str__(self):
		return '{} {} {}'.format(self.request.customer, self.quantity, self.item_rate)

class RequestComplition(models.Model):
	suggest_time 	= models.DateTimeField()
	complete_time 	= models.DateTimeField()
	duration_late 	= models.DurationField(default = timedelta())   
	request 		= models.ForeignKey(Request, on_delete = models.CASCADE)

	def __str__(self):
		if self.request.status == "completed":
			if self.duration_late == timedelta(seconds=0) :
				return '{} on time'.format(self.request)
			else :
				return '{} being late by {}'.format(self.request, self.duration_late)
		elif self.request.status == "not completed":
			return '{} have complete before time {}'.format(self.request, self.suggest_time)

