from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post, Price
from .forms import PriceForm
from django.contrib import messages
from django.views.generic import (
	ListView, 
	DetailView,
	CreateView,
)	

poststry= [
	{
		'author': 'CoreyMS',
		'title': 'Blog Post 1',
		'content': 'Firsty post content',
		'date_posted': 'August 27, 2018'
	},
	{
		'author': 'sean',
		'title': 'Blog Post 2',
		'content': 'second post contentttttttttt',
		'date_posted': 'August 28, 2018'
	}
]

girl= [
	{
		'name': 'Mayaka',
		'age': 23,
	},
	{
		'name': 'Koko',
		'age': 23,
	},
	{
		'name': 'Ai',
		'age': 22,
	}		
]


def home(request):
	context= {
		'posts': Post.objects.all()
	}
	return render(request, 'info/home.html', context)	

class PostListView(ListView):
	model= Post	
	template_name= 'info/home.html'  # <app>/<model>_<viewtype>.html
	context_object_name= 'posts'
	ordering= ['-date_posted']

class PostDetailView(DetailView):
	model= Post	

class PostCreateView(CreateView):
	model= Post	
	fields= ['title', 'content']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

def hometry(request):
	context= {
		'posts': poststry,
		'girls': girl,
	}
	return render(request, 'info/hometry.html', context)	

def about(request):
	return render(request, 'info/about.html', {'title': 'About'})

def price(request):
	context= {
		'prices': Price.objects.all()
	}
	return render(request, 'info/price.html', context)		

def pricenew(request):
	form= PriceForm(request.POST)
	if not request.user.is_superuser or not request.user.is_staff:
		return redirect('info-home')
	if form.is_valid():
		form.save()
		name= form.cleaned_data.get('name')
		messages.success(request, f'Hair price created for {name}!')
		return redirect('info-price')


	return render(request, 'info/pricenew.html', {'form': form})	

