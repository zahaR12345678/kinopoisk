from django.urls import path
from kinopoisk.views import *

urlpatterns = [
    path('', home, name='home'),
    path('movie_detail/<int:movie_id>/',movie_detail, name='movie_detail'),
    path('composer_detail/<int:composer_id>/',composer_detail, name='composer_detail'),
    path('genre_detail/<int:genre_id>/',genre_detail, name='genre_detail'),
    path('director_detail/<int:director_id>/',director_detail, name='director_detail'),
    path('actor_detail/<int:actor_id>/',actor_detail, name='actor_detail'),
    path('movies_list/',movies_list, name='movies_list'),
    path('actors_list/',actors_list, name='actors_list'),
    path('composers_list/',composers_list, name='composers_list'),
    path('directors_list/',directors_list, name='directors_list'),
    path('genres_list/',genres_list, name='genres_list'),
         
         
         
]
