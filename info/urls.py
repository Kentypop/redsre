from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='info-home'),
    path('about/', views.about, name='info-about'),
    path('hometry/', views.hometry, name='info-hometry'),
    path('price/', views.price, name='info-price'),
    path('pricenew/', views.pricenew, name='info-pricenew'),
]