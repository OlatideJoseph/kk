from django.contrib.auth import get_user_model
from django.db import models


class Food(models.Model):
    name = models.CharField(max_length=100)
    ftype = models.CharField(max_length=100,null=True)
    quantity_avail = models.PositiveIntegerField()
    image=models.ImageField(default='default.jpg',upload_to='foods/')
    price = models.FloatField(blank=True, null=True)

    def __str__(self):
    	return f"""< Food : {self.name} >"""



class Order(models.Model):
    quantity = models.PositiveIntegerField()
    customer = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)

    def __str__(self):
    	return f"""{self.customer.username} ordered {self.food.name}"""