from django.db import models
from django_resized import ResizedImageField
from datetime import datetime
from django.contrib.auth.models import User



class DogBreed(models.Model):
	breed = models.CharField(max_length=50)

	def __str__(self):
		return self.breed

	class Meta:
		ordering = ['breed']



class Dog(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	breed = models.ForeignKey('DogBreed', on_delete=models.CASCADE)
	gender = models.CharField(max_length=10)
	birthYear = models.CharField(max_length=15)
	info = models.TextField(max_length=1000)
	phone_no = models.CharField(max_length=20, null=True, blank=False)
	date = models.DateTimeField(default=datetime.now, blank=True)
	image = ResizedImageField(size=[320,240], quality=100, upload_to='pictures', null=True, blank=False)
	image2 = ResizedImageField(size=[320,240], quality=100, upload_to='pictures', null=True, blank=True)
	image3 = ResizedImageField(size=[320,240], quality=100, upload_to='pictures', null=True, blank=True)
	image4 = ResizedImageField(size=[320,240], quality=100, upload_to='pictures', null=True, blank=True)
	image5 = ResizedImageField(size=[320,240], quality=100, upload_to='pictures', null=True, blank=True)
	image6 = ResizedImageField(size=[320,240], quality=100, upload_to='pictures', null=True, blank=True)

	def __str__(self):
		return (f'{self.birthYear}, {self.gender}, {self.breed}, {self.date}, ({self.user})')

	class Meta:
		ordering = ['-date']