from django.urls import path
from .views import order_page

urlpatterns=[
    path('order-food',order_page,name='page-order')
]

