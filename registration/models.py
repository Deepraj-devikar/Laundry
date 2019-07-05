from django.db import models

# Create your models here.

class Customer(models.Model):
	name 		= models.CharField(max_length = 50)
	email 		= models.EmailField(max_length = 50)
	mobile 		= models.DecimalField(max_digits = 20, decimal_places = 0)
	password 	= models.CharField(max_length = 20)

	def __str__(self):
		return '{} : {}'.format(self.name, self.email)

class DeliveryBoy(models.Model):
	name 		= models.CharField(max_length = 50)

	def __str__(self):
		return '{}'.format(self.name)


