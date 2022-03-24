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
            "slug": "film-adi-1",
            "language": "english",
            "date": date(2023,5,5)
        },
        {
            "title": "film adı 2",
            "description": "film açıklama 2",
            "imageUrl": "m2.jpg",
            "slug": "film-adi-2",
            "language": "english",
            "date": date(2023,5,6)
        },
        {
            "title": "film adı 3",
            "description": "film açıklama 3",
            "imageUrl": "m3.jpg",
            "slug": "film-adi-3",
            "language": "english",
            "date": date(2023,5,7)
        },
        {
            "title": "film adı 4",
            "description": "film açıklama 4",
            "imageUrl": "m4.jpg",
            "slug": "film-adi-4",
            "language": "english",
            "date": date(2023,5,8)
        },
    ],
    "slider": [],
}


def index(request):
    movies = data["movies"]
    
    return render(request, 'index.html',{
        "movies": movies

    })


def movies(request):
    return render(request, 'movies.html')


def movie_details(request, slug):
    return render(request, 'movie-details.html', {
        "slug": slug
    })