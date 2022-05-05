from django.http import HttpResponse
from django.shortcuts import render
from tomlkit import date
from datetime import date
from django.shortcuts import get_object_or_404, render
# from movieapp.movies.forms import CommentForm
from movies.forms import CommentForm


# from movieapp.movies.models import Movie
from movies.models import Movie

data = {
    
    "sliders": [
        {
            "slider_image": "slider1.jpg",
            "url": "film-adi-1",
        },
        {
            "slider_image": "slider2.jpg",
            "url": "film-adi-2",
        },
        {
            "slider_image": "slider3.jpg",
            "url": "film-adi-3",
        },
        
    ],
}


def index(request):
    movies = Movie.objects.filter(is_active=True, is_home=True)
    sliders = data["sliders"]
    return render(request, 'index.html',{
        "movies": movies,
        "sliders": sliders

    })


def movies(request):
    movies = Movie.objects.filter(is_active=True)
    return render(request, 'movies.html', {
        "movies": movies
    })


def movie_details(request, slug):
    movie = get_object_or_404(Movie, slug=slug)
    comment_form = CommentForm()

    return render(request, 'movie-details.html', {
        "movie": movie,
        "genres": movie.genres.all(),
        "people": movie.people.all(),
        "videos": movie.video_set.all(),
        "comment_form": comment_form
})