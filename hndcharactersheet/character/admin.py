from django.contrib import admin

from .models.character import Character
from .models.stats import Stats
from .models.skills import Skills
from .models.basics import CharacterBasics

admin.site.register(Character)
admin.site.register(Stats)
admin.site.register(Skills)
admin.site.register(CharacterBasics)
