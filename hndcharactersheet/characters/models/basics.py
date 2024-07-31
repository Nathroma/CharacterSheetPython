from django.db import models
from .character import Character

class CharacterBasics(models.Model):
    character = models.OneToOneField(Character, on_delete=models.CASCADE)
    race = models.CharField(max_length=100)
    background = models.CharField(max_length=100)
    character_class = models.CharField(max_length=100)
    archetype = models.CharField(max_length=100)
    alignment = models.CharField(max_length=100)
    faith = models.CharField(max_length=100)
    
    age = models.IntegerField()
    size = models.CharField(max_length=50)
    weight = models.CharField(max_length=50)
    eyes = models.CharField(max_length=50)
    hair = models.CharField(max_length=50)
    beard = models.CharField(max_length=50)
    portrait = models.ImageField(upload_to='portraits/')

    def __str__(self):
        return f"Informations de base de {self.character.name}"
