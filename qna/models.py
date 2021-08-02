from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

class Question(models.Model):
	title= models.CharField(max_length= 100)
	body= models.TextField()
	date_posted= models.DateTimeField(default=timezone.now)
	author= models.ForeignKey(User, on_delete= models.CASCADE)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('questiondetail', kwargs={'pk': self.pk})	

class Answer(models.Model):
	body= models.TextField()
	question= models.ForeignKey(Question, on_delete= models.CASCADE)
	date_posted= models.DateTimeField(default=timezone.now)
	author= models.ForeignKey(User, on_delete= models.CASCADE)

	def __str__(self):
		return self.body

	def get_absolute_url(self):
		return reverse('answerdetail', kwargs={'pk': self.pk})		
