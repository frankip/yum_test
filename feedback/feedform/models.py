from django.db import models
from django.conf import settings


# Create your models here.

class Details(models.Model):
    RATING_CHOICES = (
			(1, '1'),
			(2, '2'),
			(3, '3'),
			(4, '4'),
			(5, '5'),
		)
    neighbourhood_names = (
            ('nairobi', 'nairobi'),
            ('westlands','westlands'),
            ('langata','langata'),
            ('muthaiga','muthaiga'),
            ('thika','thika')
    )
    user = models.ForeignKey('auth.User')
    phone_number = models.PositiveIntegerField()
    neighbourhood = models.CharField(choices=neighbourhood_names, max_length=200)
    rating = models.IntegerField(choices=RATING_CHOICES)
    comments = models.TextField()

    # def __str__(self):
	#     return self.user

    def __unicode__(self):
	    return self.user  