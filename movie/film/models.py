from django.db import models

# Create your models here.

class Film(models.Model):
    film_id = models.CharField(max_length=20, primary_key=True)
    title = models.CharField(max_length=20)
    keywords = models.CharField(max_length=20)