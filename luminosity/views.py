from django.shortcuts import render, HttpResponse
from luminosity import templates
import requests

from matplotlib import pyplot
import io
from django.http import HttpResponse as hp
from matplotlib.backends.backend_agg import FigureCanvasAgg
from random import sample

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
            response = requests.post('http://p1backend.azurewebsites.net/luminosity/', args)
            # Convierte la respuesta en JSON
            measure_json = response.json()

    # Realiza una petición GET al Web Services
    response = requests.get('http://p1backend.azurewebsites.net/luminosity/')
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
            response = requests.post('http://p1backend.azurewebsites.net/participante/', args)
            # Convierte la respuesta en JSON
            medicion_json = response.json()

    # Realiza una petición GET al Web Services
    response = requests.get('http://p1backend.azurewebsites.net/participante/')
    # Convierte la respuesta en JSON
    datos = response.json()
    # Rederiza la respuesta en el template measure
    return render(request, "luminosity/participantes.html", {'datos': datos})
    
def grafico():
    personas = ('en peligro', 'fuera de peligro')
    valores = (50, 20)
    colores = ('red', 'blue')

    _, _, texto = pyplot.pie(valores, colores, labels=personas, autopct='%1.1f%%')

    for text in texto:
        text.set_color('white')
    pyplot.axis('equal')
    pyplot.title('Personas')

    buf = io.BytesIO()
    canvas = FigureCanvasAgg(pyplot)
    canvas.print_png(buf)

    response = hp(buf.getvalue(), content_type='image/png')
    response['Content-Length'] = str(len(response.content))
    return response

def plot(request):
    # Creamos los datos para representar en el gráfico
    x = range(1,11)
    y = sample(range(20), len(x))

    # Creamos una figura y le dibujamos el gráfico
    f = pyplot.figure()

    # Creamos los ejes
    axes = f.add_axes([0.15, 0.15, 0.75, 0.75]) # [left, bottom, width, height]
    axes.plot(x, y)
    axes.set_xlabel("Eje X")
    axes.set_ylabel("Eje Y")
    axes.set_title("Mi gráfico dinámico")

    # Como enviaremos la imagen en bytes la guardaremos en un buffer
    buf = io.BytesIO()
    canvas = FigureCanvasAgg(f)
    canvas.print_png(buf)

    # Creamos la respuesta enviando los bytes en tipo imagen png
    response = HttpResponse(buf.getvalue(), content_type='image/png')

    # Limpiamos la figura para liberar memoria
    f.clear()

    # Añadimos la cabecera de longitud de fichero para más estabilidad
    response['Content-Length'] = str(len(response.content))

    # Devolvemos la response
    return response