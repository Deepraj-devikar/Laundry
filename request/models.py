from django.db import models

from registration.models import Customer, DeliveryBoy
from rateboard.models import Rates
 
# Create your models here.
class Request(models.Model):
	customer 		= models.ForeignKey(Customer, on_delete=models.CASCADE)
	delivery_boy 	= models.ForeignKey(DeliveryBoy, on_delete=models.CASCADE)
	request_type 	= models.CharField(max_length = 20, default = "collecting")
	query 			= models.TextField(max_length = 250)

class ItemCount(models.Model):
	item_rate 	= models.ForeignKey(Rates, on_delete=models.CASCADE)
	quantity 	= models.IntegerField(default = 1)
	request 	= models.ForeignKey(Request, on_delete = models.CASCADE)

class RequestComplition(models.Model):
	suggest_time 	= models.DateTimeField()
	complete_time 	= models.DateTimeField()
	duration_late 	= models.DurationField(default = 0)   
	request 		= models.ForeignKey(Request, on_delete = models.CASCADE)