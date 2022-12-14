from django.db import models


# Create your models here.
class Film(models.Model):
    title = models.CharField(max_length=100)
    episode = models.CharField(max_length=20)
    opening_text = models.TextField()
    director = models.CharField(max_length=100)
    producer = models.CharField(max_length=100)
    release_date = models.CharField(max_length=20)
    planets = models.ManyToManyField('planets.Planet', blank=True)
    characters = models.ManyToManyField('characters.Character', blank=True, related_name='film_character_set')
