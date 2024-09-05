from django.db import models

# Create your models here.
class Tour(models.Model):

    place = models.CharField(max_length=200)
    image = models.ImageField(upload_to='tour_img/', blank=True, null=True)  # For uploading images

    def __str__(self):
        return self.place
