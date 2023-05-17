from django.urls import path
from . import views

urlpatterns = [
    path('coupon/extract', views.ExtractCouponCode.as_view(), name='coupon_extract'),
]
