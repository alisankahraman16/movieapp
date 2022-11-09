from django.db import models

# Create your models here.
class Movie(models.Model):
    movieid = models.CharField(max_length=20, primary_key=True,verbose_name="Film İsmi")
    title = models.CharField(max_length=30,verbose_name="Başlık")
    year = models.CharField(max_length=4,verbose_name="Yıl")
    length = models.CharField(max_length=10,verbose_name="Uzunluk")
    genres = models.CharField(max_length=100,verbose_name="Türler")
    rate = models.IntegerField(default=0,verbose_name="Puan")
    poster = models.URLField(default='',verbose_name="Afiş")
    plot = models.CharField(max_length=500,verbose_name="Konu")
    trailer = models.URLField(default='',verbose_name="Fragman")
    def __str__(self):
        return self.movieid + '|' + self.title
