from django.test import TestCase
from django.urls import reverse
# Create your tests here.


class TestPagesAppComponent(TestCase):
	def test_default_view(self):
		resp=self.client.get('/')
		self.assertEqual(resp.status_code,200)
		self.assertContains(resp,'Home')
		self.assertTemplateUsed(resp,'pages/home.html')
		
	def test_default_view_with_reverse(self):
		url=reverse('pages-home')
		resp=self.client.get('/')
		self.assertEqual(resp.status_code,200)
		self.assertContains(resp,'Home')
		self.assertTemplateUsed(resp,'pages/home.html')