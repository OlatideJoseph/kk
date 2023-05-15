from django.shortcuts import render
from django.http import HttpResponse
from foods.models import Food
# Create your views here.
def home(request):
	food=Food.objects.all()
	return render(request,'pages/home.html',{'foods':food})