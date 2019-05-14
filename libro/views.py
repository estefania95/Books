from django.shortcuts import render
from .models import Genero

# Create your views here.


def genero(request):
    generos = Genero.objects.all()
    context = {'generos': generos}
    return render(request, 'home.html', context)

