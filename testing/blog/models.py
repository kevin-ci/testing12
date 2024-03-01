from django.db import models
from cloudinary.models import CloudinaryField

class Blog(models.Model):
    title = models.CharField(max_length=200)
    image = CloudinaryField('image', default='placeholder')