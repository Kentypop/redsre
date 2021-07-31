from django.urls import path
from . import views
from .views import (PostListView, 
	PostDetailView, 
	PostCreateView,
    PostUpdateView,
    PostDeleteView,
    PriceListView,
    PriceDetailView,
    PriceUpdateView,
    PriceDeleteView
	)

urlpatterns = [
    path('', views.PostListView.as_view() , name='info-home'),
    path('post/<int:pk>/', PostDetailView.as_view() , name='post-detail'),
    path('post/new/', PostCreateView.as_view() , name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view() , name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view() , name='post-delete'),
    path('about/', views.about, name='info-about'), 
    path('hometry/', views.hometry, name='info-hometry'),
    path('price/', views.price, name='info-price'),
    path('pricenew/', views.pricenew, name='info-pricenew'),
    path('pricelist/', PriceListView.as_view() , name='info-pricelist'),
    path('price/<int:pk>/', PriceDetailView.as_view() , name='info-pricedetail'),
    path('price/<int:pk>/update/', PriceUpdateView.as_view() , name='info-priceupdate'),
    path('price/<int:pk>/delete/', PriceDeleteView.as_view() , name='info-pricedelete'),
]