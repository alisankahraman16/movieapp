from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from datetime import date
from movies.models import Movie, Slider
from movies.forms import CommentForm
from django.http.response import HttpResponseRedirect
from django.urls import reverse

# Create your views here.

def index(request):
    movies = Movie.objects.filter(is_active=True, is_home=True)
    
    sliders = Slider.objects.filter(is_active = True)
    return render(request, 'movies/index.html', {
        "movies": movies,
        "sliders": sliders
    })

def movies(request):
    movies = Movie.objects.filter(is_active=True)
    return render(request, 'movies/movies.html', {
        "movies": movies
    })

def about(request):
    return render(request, 'movies/about.html')

def page_404(request):
    return render(request, "movies/page_404.html")

def blank(request):
    return render(request, "movies/blank.html")

def movie_details(request, slug):    
    movie = get_object_or_404(Movie, slug=slug)
    comment_form = CommentForm()

    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.movie = movie
            comment.save()
            return HttpResponseRedirect(reverse("movie_details", args=[slug]))
    movie = get_object_or_404(Movie, slug=slug)
    

    return render(request, 'movies/movie_details.html',{
        "movie": movie,
        "genres": movie.genres.all(),
        "people": movie.people.all(),
        "videos": movie.video_set.all(),
        "comments": movie.comments.all().order_by("-date_added"),
        "comment_form": comment_form,
    })
