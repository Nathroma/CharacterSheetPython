from django.db import models
from .stats import Stats
from .skills import Skills
from .basics import CharacterBasics

class Character(models.Model):
    name = models.CharField(max_length=100)
    level = models.IntegerField()
    xp = models.IntegerField()
    basics = models.OneToOneField(CharacterBasics, on_delete=models.CASCADE, null=True, blank=True)
    stats = models.OneToOneField(Stats, on_delete=models.CASCADE, null=True, blank=True)
    skills = models.OneToOneField(Skills, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name
