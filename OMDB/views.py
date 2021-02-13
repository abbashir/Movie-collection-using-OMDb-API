from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
import requests


# Create your views here.
def home(request):
    return render(request, 'omdb/home.html')


@login_required
def dashboard(request):
    response = requests.get('http://www.omdbapi.com/?apikey=3ca6c0cc&s=*Star&r=json')
    movies = response.json()
    context = {
        'movies': movies['Search']
    }

    return render(request, 'omdb/dashboard.html', context)


@login_required
def search(request):
    title = request.GET.get('title')
    year = request.GET.get('year')

    response = requests.get('http://www.omdbapi.com/?apikey=3ca6c0cc&s=' + title + '&y=' + year)
    movies = response.json()

    if movies['Response'] == 'True':
        context = {
            'movies': movies['Search']
        }
    else:
        context = {}

    return render(request, 'omdb/search.html', context)


@login_required
def movie_details(request, imdbID):
    response = requests.get('http://www.omdbapi.com/?apikey=3ca6c0cc&i=' + imdbID)
    movie = response.json()
    print(movie)
    context = {
        'movie': movie
    }
    return render(request, 'omdb/movie_details.html', context)
