from django.db import models

class User(models.Model):
    userId = models.IntegerField(unique=True)
    def __str__(self):
        return f"User {self.userId}"

class Movie(models.Model):
    movieId = models.IntegerField(unique=True)
    title = models.CharField(max_length=255)
    genres = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ratings')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='ratings')
    rating = models.FloatField()
    timestamp = models.DateTimeField()

    def __str__(self):
        return f"{self.user} rated {self.movie} ({self.rating})"

class Tag(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tags')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='tags')
    tag = models.CharField(max_length=100)
    timestamp = models.DateTimeField()

    def __str__(self):
        return f"{self.tag} - {self.movie}"
