from django.db import models


# Create your models here.
class Planet(models.Model):
    name = models.CharField(max_length=100)
    diameter = models.CharField(max_length=20)
    climate = models.CharField(max_length=20)
    gravity = models.CharField(max_length=20)
    terrain = models.CharField(max_length=20)
    population = models.CharField(max_length=20)
