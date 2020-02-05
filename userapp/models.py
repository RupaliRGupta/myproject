from django.db import models

# Create your models here.

class UserModel(models.Model):
	utypes=[('User','User'),('Admin','Admin')]
	email=models.CharField(max_length=30)
	password=models.CharField(max_length=20)
	utype = models.CharField(max_length=15,choices=utypes)
	def __str__(self):
		return "{0} {1}".format(self.email,self.password)