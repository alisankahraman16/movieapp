from django.contrib import admin

from .models import Movie
# Register your models here.
@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'movieid', 'rate')
    list_display_links =  ('title','movieid','rate')
    search_fields = ["title"]
    list_filter = ["title"]
    class Meta:
        model = Movie

