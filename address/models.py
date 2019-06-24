from django.db import models

from registration.models import Customer, DeliveryBoy

# Create your models here.
class CustomerAddress(models.Model):
	house_no 				= models.CharField(max_length = 20, null = True)
	street_area_locality 	= models.TextField(max_length = 50)
	state 					= models.CharField(max_length = 25)
	town_village_city 		= models.CharField(max_length = 25)
	pincode 				= models.DecimalField(max_digits = 20, decimal_places = 0)
	customer 				= models.ForeignKey(Customer, on_delete=models.CASCADE)

class DeliveryBoyAddress(models.Model):
	house_no 				= models.CharField(max_length = 20, null = True)
	street_area_locality 	= models.TextField(max_length = 50)
	state 					= models.CharField(max_length = 25)
	town_village_city 		= models.CharField(max_length = 25)
	pincode 				= models.DecimalField(max_digits = 20, decimal_places = 0)
	delivery_boy 			= models.ForeignKey(DeliveryBoy, on_delete=models.CASCADE)

class LaundryAddress(models.Model):
	house_no 				= models.CharField(max_length = 20, null = True)
	street_area_locality 	= models.TextField(max_length = 50)
	state 					= models.CharField(max_length = 25)
	town_village_city 		= models.CharField(max_length = 25)
	pincode 				= models.DecimalField(max_digits = 20, decimal_places = 0)
	