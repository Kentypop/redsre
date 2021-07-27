from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Question(models.Model):
	title= models.CharField(max_length= 100)
	body= models.TextField()
	date_posted= models.DateTimeField(default=timezone.now)
	author= models.ForeignKey(User, on_delete= models.CASCADE)

	def __str__(self):
		return self.title

class Answer(models.Model):
	body= models.TextField()
	question= models.ForeignKey(Question, on_delete= models.CASCADE)
	date_posted= models.DateTimeField(default=timezone.now)
	author= models.ForeignKey(User, on_delete= models.CASCADE)

	def __str__(self):
		return self.body