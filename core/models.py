from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    favouret_movies = models.ManyToManyField('kinopoisk.Movie')
    avatar = models.ImageField(
        upload_to='avatars/',null=True, blank=True
    )