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
            response = requests.post('http://127.0.0.1:8000/luminosity/', args)
            # Convierte la respuesta en JSON
            measure_json = response.json()

    # Realiza una petición GET al Web Services
    response = requests.get('http://127.0.0.1:8000/luminosity/')
    # Convierte la respuesta en JSON
    luminosity = response.json()
    # Rederiza la respuesta en el template measure
    return render(request, "luminosity/luminosity.html", {'luminosity': luminosity})