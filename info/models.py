from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
 	title= models.CharField(max_length=100)
 	content= models.TextField()
 	date_posted= models.DateTimeField(default=timezone.now)
 	author= models.ForeignKey(User, on_delete= models.CASCADE)

 	def __str__(self):
 		return self.title

 	#For redirect, created the post but WHERE to go AFTER its success	
 	#this method tell django how to find url to any spcific instance of a post
 	#Detail page, starting from 	
 	def get_absolute_url(self):	
 		#Reverse will return full path as a string
 		return reverse('post-detail', kwargs={'pk': self.pk})
 		#If u want it to go to homepage,instead of this speific post.
 		#set an attribute in createview called suces url n set that to the homepage

class Price(models.Model):
	name= models.CharField(max_length=50)
	price= models.DecimalField(max_digits= 5, decimal_places=2)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('info-pricedetail', kwargs={'pk': self.pk})	


	 		