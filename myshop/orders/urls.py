from django.urls import path
from .views.order_view import order_create
from .views.admin_view import admin_order_detail

app_name = 'orders'

urlpatterns = [
    path('create/', order_create, name='order_create'),
    path('admin/order/<int:order_id>/', admin_order_detail, name='admin_order_detail'),
]
