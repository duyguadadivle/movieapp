from django.urls import path
from.import views

urlpatterns = [
    path("", views.movieapp, name="home_page"),
    path("movies", views.movies, name="movies_page"),
    path("movies/<slug:slug>", views.movie_details, name="movie_details"),
]
