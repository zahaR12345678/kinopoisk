from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'kinopoisk/home.html')

def movie_detail(request, movie_id):
    return render(request, 'kinopoisk/detail/movie_detail.html')

def composer_detail(request, composer_id):
    return render(request, 'kinopoisk/detail/composer_detail.html')

def genre_detail(request, genre_id):
    return render(request, 'kinopoisk/detail/genre_detail.html')

def director_detail(request, director_id):
    return render(request, 'kinopoisk/detail/director_detail.html')

def actor_detail(request, actor_id):
    return render(request, 'kinopoisk/detail/actor_detail.html')

def actors_list(request):
    return render(request, 'kinopoisk/list/actors_list.html')

def composers_list(request):
    return render(request, 'kinopoisk/list/composers_list.html')

def genres_list(request,):
    return render(request, 'kinopoisk/list/genres_list.html')

def directors_list(request, ):
    return render(request, 'kinopoisk/list/directors_list.html')

def movies_list(request):
    return render(request, 'kinopoisk/list/movies_list.html')