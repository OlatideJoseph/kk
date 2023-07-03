from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Food,Order
# Create your tests here.

class TestFoodAppComponents(TestCase):
	''' \
		A django test case class that test
		the food app model pages and views component in 
		unit
	'''
	@classmethod
	def setUpTestData(cls):
		cls.food=Food(
			name='food name',
			quantity_avail=50,
			price=5000.00
			)
		cls.user=get_user_model()(
			username='foodsuser',
			email='foodsuser@kapitalkitchen.ng',
			password='testpassword'
			)
		cls.order=Order(
			customer=cls.user,
			food=cls.food,
			quantity=1
			)
	def test_food_page(self):
		pass
	def test_foods_models(self):
		food=self.food
		self.assertEqual(food.name,'food name')
		self.assertEqual(food.quantity_avail,50)
		self.assertEqual(food.price,5000)
	def test_order_model(self):
		user=self.user
		order=self.order
		food=self.food
		self.assertEqual(order.customer.username,user.username)
