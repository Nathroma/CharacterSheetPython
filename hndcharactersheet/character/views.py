from django.shortcuts import render

def fiche_personnage(request):
    return render(request, 'characters/fiche.html')
