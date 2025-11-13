from django.contrib import admin

# Register your models here.
from .models import User, Movie, Rating, Tag
admin.site.register(User)
admin.site.register(Movie)
admin.site.register(Rating)
admin.site.register(Tag)
