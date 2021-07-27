from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.utils import timezone
from datetime import timedelta
import uuid

class Profile(models.Model):
	user= models.OneToOneField(User, on_delete= models.CASCADE)
	image= models.ImageField(default= 'default.jpg', upload_to= 'profile_pics')

	def __str__(self):
		return f'{self.user.username} Profile'
		
	def save(self, *args, **kwargs):	
		super(Profile, self).save(*args, **kwargs)

		img= Image.open(self.image.path)

		if img.height> 300 or img.width > 300:
			output_size= (300, 300)
			img.thumbnail(output_size)
			img.save(self.image.path)

def twentydays_coupon():
	return timezone.now()+ timedelta(days=20)

class Coupon(models.Model):
	user= models.OneToOneField(User, on_delete= models.CASCADE)
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	valid_from= models.DateTimeField(default=timezone.now)
	valid_till= models.DateTimeField(default=twentydays_coupon)

	def __str__(self):
		return f'{self.user.username} Coupon'	
