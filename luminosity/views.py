from django.shortcuts import render, HttpResponse
from luminosity import templates
import requests
#import request
# Create your views here.

'''
def luminosity(request):
    return render(request, "luminosity/luminosity.html")'''

def luminosity(request):
    # Verifica si hay un parámetro value en la petición GET
    if 'value' in request.GET:
        value = request.GET['value']
        # Verifica si el value no esta vacio
        if value:
            # Crea el json para realizar la petición POST al Web Service
            args = {'type': 'cd', 'value': value}
            response = requests.post('https://p1backend.azurewebsites.net/', args)
            # Convierte la respuesta en JSON
            measure_json = response.json()

    # Realiza una petición GET al Web Services
    response = requests.get('https://p1backend.azurewebsites.net/')
    # Convierte la respuesta en JSON
    luminosity = response.json()
    # Rederiza la respuesta en el template measure
    return render(request, "luminosity/luminosity.html", {'luminosity': luminosity})

def participante(request):
    print ('entre a participante')
    if 'cedula' in request.GET:
        print('entre al if')
        cedula = request.GET['cedula']
        nombre = request.GET['nombre']
        actividad = request.GET['actividad']
        estrato = request.GET['estrato']
        #valor = request.GET['value']
        print(request.GET)

       # Verifica si el value no esta vacio
        if cedula:
        # Crea el json para realizar la petición POST al Web Service
            args = {'cedula': cedula, 'nombre': nombre, 'actividad': actividad, 'estrato': estrato}
            print(args)
            response = requests.post('http://127.0.0.1:8000/participante/', args)
            # Convierte la respuesta en JSON
            medicion_json = response.json()

    # Realiza una petición GET al Web Services
    response = requests.get('http://127.0.0.1:8000/participante/')
    # Convierte la respuesta en JSON
    datos = response.json()
    # Rederiza la respuesta en el template measure
    return render(request, "luminosity/participantes.html", {'datos': datos})
    