from django.db import models

# Create your models here.

class Movie(models.Model):
    audience = models.ForeignKey("aud.User",on_delete = models.CASCADE)
    title = models.CharField(max_lenght = 50)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add = True)
