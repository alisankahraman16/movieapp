from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'index.html')

def movies(request):
    return render(request, 'movies.html')

def movie_details(request, slug):        
    return render(request, 'movie_details.html', {
        "slug": slug
    })
