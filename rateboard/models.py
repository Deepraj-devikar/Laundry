from django.db import models

# Create your models here.

class Rates(models.Model):
	item_name 	= models.CharField(max_length = 50)
	piece 		= models.IntegerField(default = 1)
	rate 		= models.IntegerField(default = 0) 

	def __str__(self):
		return '{} rate {}/{}'.format(self.item_name, self.rate, self.piece)
