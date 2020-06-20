from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
	PostName=models.CharField(max_length=20)
	Post=models.TextField()
	Date_Added=models.DateTimeField(default=timezone.now)

	def __str__(self):
		return "Name: {} , ID {}".format(self.PostName,self.id)