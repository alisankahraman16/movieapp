from django.contrib import admin

from .models import Movie
from .models import Actor
# Register your models here.
@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'movieid', 'rate')
    class Meta:
        model = Movie


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ('name', 'actorid')
    class Meta:
        model = Actor

