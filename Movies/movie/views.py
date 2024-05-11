from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from Movies.settings import STATIC_URL
from .models import Movie
import json
import os

def movie(request):
    template = loader.get_template('movie_list.html')
    return HttpResponse(template.render())

def movie_list(request):
    movies_json_path = os.path.join('movie', 'movies.json')

    with open(movies_json_path, 'r') as f:
        movies_data = json.load(f)
    print(f"STATIC_URL: {STATIC_URL}")  
    context = {'movies': movies_data}
    return render(request, 'movie_list.html', context)

def movie_detail(request, id):
  try:
    movie = Movie.objects.get(pk=id)  # Retrieve movie by ID
  except Movie.DoesNotExist:
    return render(request, 'error.html')  # Handle movie not found

  context = {'movie': movie}
  return render(request, 'movie_detail.html', context)