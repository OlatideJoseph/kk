from django.shortcuts import render
from django.http import HttpResponse
import json
# Create your views here.
def order_page(request):
    if request.method == "POST":
        print(request.FORM)
    return HttpResponse(
        json.dumps({"msg":'testing'}),
        headers={
            'Content-Type':'application/json',
            'cache-control':'nocache'
            }
        )