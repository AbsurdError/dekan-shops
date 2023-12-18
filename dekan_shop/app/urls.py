from .views import *
from django.urls import path

urlpatterns = [
    path('', one_page, name='one-page'),
    path('twopage/', two_page, name='two-page'),
    path('threepage/', tree_page, name='three-page'),
    path('shopform/', shop_form, name='shop-form')
]
