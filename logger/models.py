from django.db import models
from django.contrib.auth.models import AbstractUser
from UserControl.models import User


class LoggerRecords(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
	datetime = models.CharField(max_length=100)
	action = models.CharField(max_length=1000)
	username = models.CharField(max_length=1000)

	def __str__(self):
		return f"{self.user.username}, {self.datetime}, {self.action}" 
