from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post, Price
from .forms import PriceForm
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
	ListView, 
	DetailView,
	CreateView,
	UpdateView,
	DeleteView,
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

class PostCreateView(LoginRequiredMixin, CreateView):
	model= Post	
	fields= ['title', 'content']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model= Post	
	fields= ['title', 'content'] 

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)	

	def test_func(self):
		#Get the post that we currently trying to update
		post= self.get_object()
		if self.request.user == post.author:
			return True
		return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model= Post	
	success_url= '/'

	def test_func(self):
		#Get the post that we currentl;y trying to update
		post= self.get_object()
		if self.request.user == post.author:
			return True
		return False						

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

class PriceListView(ListView):
	model= Price

	#template naming convention
	# <app>/<model>_<viewtype>.html
	#info/price_list.html

class PriceDetailView(DetailView):
	model= Price

	#https://stackoverflow.com/questions/39238867/django-generic-views-how-does-detailview-automatically-provides-the-variable-to
	def get_context_object_name(self, obj):

	    """Get the name to use for the object."""
	    if self.context_object_name:
	        return self.context_object_name
	    elif isinstance(obj, Price):
	        return obj._meta.model_name
	    else:
	        return None

	    print(self.context_object_name)  
	    print(obj._meta.model_name)
	    
class PriceUpdateView(LoginRequiredMixin, UpdateView):
	model= Price
	fields= ['name', 'price']


	#@@@@@@@@@@@ Here we need to make a check in place for user== Lily or the author
	#def test_func(self):
	#	#Get the post that we using now
	#	post= self.get_object()
	#	if self.request.user == 

class PriceDeleteView(LoginRequiredMixin, DeleteView):
	model= Price
	success_url= 'info-pricelist'

	#@@@@@@@@@@ need to make a check in place for user== Lily or the author







