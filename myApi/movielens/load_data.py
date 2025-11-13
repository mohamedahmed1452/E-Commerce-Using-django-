import csv
from datetime import datetime
from movielens.models import User, Movie, Rating, Tag


def load_movies(path):
    print("Loading movies...")
    with open(path, encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            Movie.objects.get_or_create(
                movieId=row['movieId'],
                defaults={
                    'title': row['title'],
                    'genres': row['genres']
                }
            )
    print("Movies loaded successfully!")


def get_or_create_user(user_id):
    user, _ = User.objects.get_or_create(userId=user_id)
    return user


def load_ratings(path):
    print("Loading ratings...")
    with open(path, encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            user = get_or_create_user(row['userId'])
            movie = Movie.objects.get(movieId=row['movieId'])
            Rating.objects.create(
                user=user,
                movie=movie,
                rating=row['rating'],
                timestamp=datetime.fromtimestamp(int(row['timestamp']))
            )
    print("Ratings loaded successfully!")


def load_tags(path):
    print("Loading tags...")
    with open(path, encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            user = get_or_create_user(row['userId'])
            movie = Movie.objects.get(movieId=row['movieId'])
            Tag.objects.create(
                user=user,
                movie=movie,
                tag=row['tag'],
                timestamp=datetime.fromtimestamp(int(row['timestamp']))
            )
    print("Tags loaded successfully!")
