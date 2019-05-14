from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import ExtendedUserCreationForm
from .models import Usuario
from libro.models import Genero, Libro
# Create your views here.

#Bienvenida
def bienvenida(request):
    return render(request, 'bienvenida.html', {})


#home
def home(request):
    generos = Genero.objects.all()
    libros = Libro.objects.all().order_by('-anoEdicion')

    context = {'generos': generos, 'libros': libros}
    return render(request, 'home.html', context)


#Registrar usuario
def registro(request):
    if request.method == 'POST':
        form = ExtendedUserCreationForm(request.POST)

        if form.is_valid():
            usuario = form.save()

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')

            usuari = authenticate(username=username, password=password)
            login(request, usuari)

            return redirect('usuario:home')
    else:
        form = ExtendedUserCreationForm()

    context = {'form': form }

    return render(request, 'registro.html', context)


#Iniciar sesion
def inicioSesion(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return redirect('usuario:home')
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username, password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'login.html', {})


