from django.db import models


# Create your models here.
class Character(models.Model):
    name = models.CharField(max_length=100)
    height = models.CharField(max_length=20)
    mass = models.CharField(max_length=20)
    hair_color = models.CharField(max_length=20)
    skin_color = models.CharField(max_length=20)
    eye_color = models.CharField(max_length=20)
    birth_year = models.CharField(max_length=20)
    gender = models.CharField(max_length=20)
