from django.urls import path
from . import views
from .views import (PostListView, 
	PostDetailView, 
	PostCreateView
	)

urlpatterns = [
    path('', views.PostListView.as_view() , name='info-home'),
    path('post/<int:pk>/', PostDetailView.as_view() , name='post-detail'),
    path('post/new/', PostCreateView.as_view() , name='post-create'),
    path('about/', views.about, name='info-about'),
    path('hometry/', views.hometry, name='info-hometry'),
    path('price/', views.price, name='info-price'),
    path('pricenew/', views.pricenew, name='info-pricenew'),
]