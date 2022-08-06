from django.urls import path
from .views.order_view import order_create

app_name = 'orders'

urlpatterns = [
    path('create/', order_create, name='order_create'),
]
