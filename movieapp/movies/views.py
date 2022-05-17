from django.http import HttpResponse, HttpResponseRedirect
# from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from tomlkit import date
from datetime import date
from django.shortcuts import get_object_or_404, render
# from movieapp.movies.models import Slider
# from movieapp.movies.forms import CommentForm
from movies.forms import CommentForm


# from movieapp.movies.models import Movie
from movies.models import Movie, Slider
from django.urls import reverse



def movieapp(request):
    movies = Movie.objects.filter(is_active=True, is_home=True)
    sliders = Slider.objects.filter(is_active=True)
    return render(request, 'movies/movieapp.html',{
        "movies": movies,
        "sliders": sliders

    })


def movies(request):
    movies = Movie.objects.filter(is_active=True)
    return render(request, 'movies/movies.html', {
        "movies": movies
    })


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


    return render(request, 'movies/movie-details.html', {
        "movie": movie,
        "genres": movie.genres.all(),
        "people": movie.people.all(),
        "videos": movie.video_set.all(),
        "comments": movie.comments.all().order_by("-date_added"),
        "comment_form": comment_form #
})