from django.db import models
from django.core.validators import MinLengthValidator
from django.db import models
from ckeditor.fields import RichTextField
from django.core.validators import MinLengthValidator, MaxLengthValidator
# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Contact(models.Model):
    address = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.address




class Person(models.Model):
    genders = (
        ('E', 'Erkek'),
        ('K', 'kadın'),
    )

    duty_types = (
        ('1', 'Set Ekibi'),
        ('2', 'Oyuncu'),
        ('3', 'Yönetmen'),
        ('4', 'Senarist'),
    )

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    biography = models.CharField(max_length=3000)
    image_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    gender = models.CharField("Cinsiyet",max_length=1, choices=genders)
    duty_type = models.CharField("Görev",max_length=1, choices=duty_types)
    contanct = models.OneToOneField(Contact, on_delete=models.CASCADE, null=True, blank=True)

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    full_name.fget.short_description = "Ad Soyad"

    class Meta:
        verbose_name = 'Kişi'
        verbose_name_plural = 'Kişiler'
    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.duty_types[int(self.duty_type)-1][1]})"

class Movie(models.Model):
    title = models.CharField("Başlık",max_length=100)
    description = RichTextField()
    image_name = models.ImageField(upload_to="movies")
    image_cover = models.ImageField(upload_to="movies")
    date = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True, db_index=True)
    budget = models.DecimalField(max_digits=19, decimal_places=2)
    language = models.CharField("Dil",max_length=100)
    is_active = models.BooleanField(default=False)
    is_home = models.BooleanField(default=False)
    people = models.ManyToManyField(Person)
    genres = models.ManyToManyField(Genre,verbose_name="Türler")

    class Meta:
        verbose_name = 'Film'
        verbose_name_plural = 'Filmler'

    def __str__(self):
        return self.title

class Comment(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(default=" ")
    text = models.TextField(max_length=500)
    rating = models.IntegerField(null=True)
    date_added = models.DateTimeField(null=True, auto_now=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="comments")

class Video(models.Model):
    title = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    movie  = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return self.title