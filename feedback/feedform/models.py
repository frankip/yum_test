from django.db import models
from django.conf import settings


# Create your models here.

class Details(models.Model):
    user = models.ForeignKey('auth.User')
    phone_number = models.PositiveIntegerField()
    neighbourhood = models.CharField(max_length=200)
    rating = models.CharField(max_length=200)
    comments = models.TextField()

    # def __str__(self):
	#     return self.user

    def __unicode__(self):
	    return self.user  