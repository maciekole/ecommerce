from django.urls import path
from .views import cart_view

app_name = 'cart'

urlpatterns = [
    path('', cart_view.cart_detail, name='cart_detail'),
    path('add/<int:product_id>/', cart_view.cart_add, name='cart_add'),
    path('remove/<int:product_id>/', cart_view.cart_remove, name='cart_remove'),
]
