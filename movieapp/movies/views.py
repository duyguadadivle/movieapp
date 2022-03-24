from django.http import HttpResponse
from django.shortcuts import render
from tomlkit import date
from datetime import date

# Create your views here.

data = {
    "movies": [
        {
            "title": "film adı 1",
            "description": "film açıklama 1",
            "imageUrl": "m1.jpg",
            "coverImage": "cover1.jpg",
            "slug": "film-adi-1",
            "language": "english",
            "date": date(2023,5,5)
        },
        {
            "title": "film adı 2",
            "description": "film açıklama 2",
            "imageUrl": "m2.jpg",
            "coverImage": "cover2.jpg",
            "slug": "film-adi-2",
            "language": "english",
            "date": date(2023,5,6)
        },
        {
            "title": "film adı 3",
            "description": "film açıklama 3",
            "imageUrl": "m3.jpg",
            "coverImage": "cover3.jpg",
            "slug": "film-adi-3",
            "language": "english",
            "date": date(2023,5,7)
        },
        {
            "title": "film adı 4",
            "description": "film açıklama 4",
            "imageUrl": "m4.jpg",
            "coverImage": "cover4.jpg",
            "slug": "film-adi-4",
            "language": "english",
            "date": date(2023,5,8)
        },
    ],
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
    # son 4 film gösterilsin
    movies = data["movies"][-4:]
    sliders = data["sliders"]
    return render(request, 'index.html',{
        "movies": movies,
        "sliders": sliders

    })


def movies(request):
    movies = data["movies"]
    return render(request, 'movies.html', {
        "movies": movies
    })


def movie_details(request, slug):
    movies = data["movies"]
    # selectedMovie = None
    # for movie in movies:
    #     if movie["slug"] == slug:
    #         selectedMovie = movie

    selectedMovie = next(movie for movie in movies if movie["slug"] == slug)
    print(selectedMovie)
    # print(next(selectedMovie))

    return render(request, 'movie-details.html', {
        "movie": selectedMovie
    })