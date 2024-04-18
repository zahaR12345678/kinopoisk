from django.contrib import admin
from kinopoisk.models import*
# # Register your models here.
@admin.register(Genre)
class GenreAmin(admin.ModelAdmin):
    list_display = (
        'id', 'name',
    )


@admin.register(MoviePerson)
class MoviePersonAdmin(admin.ModelAdmin):
    list_display = (
        'role', 'name', 
    )      

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'title', 'rating',
    )          

@admin.register(MovieReview)
class MovieReviewAdmin(admin.ModelAdmin):
    list_display = (
        'author', 'movie', 'likes', 
    )              