from django.db import models


# Create your models here.
class Planet(models.Model):
    name = models.CharField(max_length=100)
    diameter = models.CharField(max_length=100)
    climate = models.CharField(max_length=100)
    gravity = models.CharField(max_length=100)
    terrain = models.CharField(max_length=100)
    population = models.CharField(max_length=100)
