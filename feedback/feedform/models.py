from django.db import models

# Create your models here.

class FeedBackForm(models.Model):
    name = models.CharField(max_length=200)
    phone_number = models.Integerfield()
    neighbourhood = models.CharField(max_length=200)
    rating = models.CharField()
    comments = models.TextField()
