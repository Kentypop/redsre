from django import forms
from django.contrib.auth.models import User
from .models import Price

class PriceForm(forms.ModelForm):

	class Meta:
		model= Price
		fields= ('name', 'price',)