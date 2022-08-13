from django.urls import path
from .views.coupon_view import coupon_apply

app_name = 'coupons'

urlpatterns = [
    path('apply/', coupon_apply, name='apply'),
]
