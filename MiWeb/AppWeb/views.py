from django.http import HttpResponse
from datetime import datetime

from django.shortcuts import render

from AppWeb.models import Familiares
from django.template import loader

# Create your views here.

def inicio(request):

    lista = Familiares.objects.all()
    #diccionario = {'lista_familiares':lista}
    #plantilla = loader.get_template('inicio.html')
    #documento = plantilla.render(diccionario)
    return render(request, 'inicio.html', {'lista_familiares':lista})

def padre(request):

    nom = 'Pepe'
    apell = 'Argento'
    edad = 57
    nac = datetime.strptime("15-03-1965", "%d-%m-%Y")

    padre = Familiares(nombre=nom, apellido=apell, edad=edad, nacimiento=nac)
    padre.save()

    diccionario = {'nombre':padre.nombre, 'apellido':padre.apellido, 'edad':padre.edad, 'nacimiento':padre.nacimiento}
    plantilla = loader.get_template('papa.html')
    documento = plantilla.render(diccionario)
    return HttpResponse(documento)

def madre(request):

    nom = 'Moni'
    apell = 'Argento'
    edad = 55
    nac = datetime.strptime("04-05-1967", "%d-%m-%Y")

    madre = Familiares(nombre=nom, apellido=apell, edad=edad, nacimiento=nac)
    madre.save()

    diccionario = {'nombre':madre.nombre, 'apellido':madre.apellido, 'edad':madre.edad, 'nacimiento':madre.nacimiento}
    plantilla = loader.get_template('mama.html')
    documento = plantilla.render(diccionario)
    return HttpResponse(documento)

def hermano(request):

    nom = 'Koki'
    apell = 'Argento'
    edad = 25
    nac = datetime.strptime("29-06-1997", "%d-%m-%Y")

    hermano = Familiares(nombre=nom, apellido=apell, edad=edad, nacimiento=nac)
    hermano.save()

    diccionario = {'nombre':hermano.nombre, 'apellido':hermano.apellido, 'edad':hermano.edad, 'nacimiento':hermano.nacimiento}
    plantilla = loader.get_template('hermano.html')
    documento = plantilla.render(diccionario)
    return HttpResponse(documento)

def hermana(request):

    nom = 'Paola'
    apell = 'Argento'
    edad = 23
    nac = datetime.strptime("20-09-1998", "%d-%m-%Y")

    hermana = Familiares(nombre=nom, apellido=apell, edad=edad, nacimiento=nac)
    hermana.save()

    diccionario = {'nombre':hermana.nombre, 'apellido':hermana.apellido, 'edad':hermana.edad, 'nacimiento':hermana.nacimiento}
    plantilla = loader.get_template('hermana.html')
    documento = plantilla.render(diccionario)
    return HttpResponse(documento)