from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Tour(models.Model):

    place = models.CharField(max_length=200)
    image = models.ImageField(upload_to='tour_img/', blank=True, null=True)  # For uploading images

    def __str__(self):
        return self.place


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    preferred_loc = models.CharField(max_length=100)
    budget = models.FloatField()
    
    def __str__(self):
        return self.user.username  # Return username instead of name

    