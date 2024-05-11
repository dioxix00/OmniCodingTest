import json
from django.core.management.base import BaseCommand
from movie.models import Movie

class Command(BaseCommand):
    help = 'Populate database with data from a JSON file'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='Path to the JSON file')

    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']
        
        with open(file_path, 'r') as file:
            data = json.load(file)

            for movie_data in data:
                genre = ", ".join(movie_data.get('genre', []))

                movie = Movie.objects.create(
                    id=movie_data['id'],
                    name=movie_data['name'],
                    description=movie_data.get('description', ''),
                    duration=movie_data['duration'],
                    language=movie_data['language'],
                    userRating=movie_data['userRating'],
                    genre=genre
                )

        self.stdout.write(self.style.SUCCESS('Database populated successfully'))