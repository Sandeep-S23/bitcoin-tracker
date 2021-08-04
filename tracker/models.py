from django.db import models
from django.contrib.auth.models import User

class Alert(models.Model):
	alert_owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
	price = models.IntegerField()
	triggered = models.BooleanField(default=False)
	created_at = models.DateTimeField(auto_now_add=True)
	triggered_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.price


