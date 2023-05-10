from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.

class Food(models.Model):
	name=models.CharField(max_length=100)
	ftype=models.CharField(max_length=100)
	quantity_avail=models.PositiveIntegerField(
		blank=False,
		null=False,
		default=1
		)
	price=models.FloatField(blank=False,null=True,default=0.00)



class Order(models.Model):
	'''
	    A database model that stores customers orders
	'''
	customer=models.ForeignKey(
		get_user_model(),
		on_delete=models.CASCADE
		)
	food=models.ForeignKey(
		Food,on_delete=models.CASCADE
		)
	quantity=models.PositiveIntegerField(
		blank=False,
		null=False,
		default=1,
		help_text="stores the quantity of product ordered"
		)