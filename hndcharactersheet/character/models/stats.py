from django.db import models
from .character import Character

class Stats(models.Model):
    character = models.OneToOneField(Character, on_delete=models.CASCADE)
    strength = models.IntegerField()
    dexterity = models.IntegerField()
    constitution = models.IntegerField()
    intelligence = models.IntegerField()
    wisdom = models.IntegerField()
    charisma = models.IntegerField()

    def __str__(self):
        return f"Stats de {self.character.name}"
