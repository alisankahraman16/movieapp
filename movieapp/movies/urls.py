from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="home_page"),
    path('movies', views.movies, name="movies_page"),
    path('movies/<slug:slug>', views.movie_details, name="movie_details"),
    path('about', views.about, name="about"),
    path('page_404', views.page_404, name="page_404"),
    path('blank', views.blank, name="blank"),
]






