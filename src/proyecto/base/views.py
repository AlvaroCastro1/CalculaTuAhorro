import requests
import bs4
from django.shortcuts import render
from django.http import HttpResponse
from .models import Banco
from django.views.generic.list import ListView
from django.http.response import JsonResponse
import shutil
import os
from PIL import Image

# Create your views here.

def inicio(request):
    labels = []
    data = []
    colors = []
    
    bancos = Banco.objects.order_by('-tasa')
    for bank in bancos:
        labels.append(bank.nombre)
        data.append(float(bank.tasa))
        colors.append(bank.rgb)
    return render(request, 'base/inicio.html', {'labels':labels, 'data': data, 'colors': colors})

class Lista_Bancos(ListView):
    model = Banco

def lista_bancos(pedido):
    return HttpResponse('Lista de Bancos')
def generar_bancos(request):
    carpeta = './api/static/images/img_bancos/'

    Banco.objects.all().delete()

    # Eliminar todos los archivos de la carpeta
    if os.path.exists(carpeta) and os.path.isdir(carpeta):
        # Obtener una lista de los archivos en la carpeta
        archivos = os.listdir(carpeta)

        if archivos:
            # Iterar sobre los archivos y eliminarlos uno por uno
            for archivo in archivos:
                ruta_archivo = os.path.join(carpeta, archivo)  # Construir la ruta completa del archivo
                if os.path.isfile(ruta_archivo):  # Verificar si es un archivo (no una carpeta)
                    os.remove(ruta_archivo)  # Eliminar el archivo
            print("Imagenes Banco: Archivos eliminados de la carpeta.")
        else:
            print("Imagenes Banco: La carpeta está vacía.")
    else:
        print("Imagenes Banco: La carpeta no existe.")
    
    url_base = "https://simulador.condusef.gob.mx/condusefahorro/datos_ppa.php?capital_inicial=25%2C000&ahorro=1%2C200&periodo=28&fecha_inicio_base=2006-01-02&fecha_fin_base=2023-02-26&durante=5"
    resultado = requests.get(url_base)
    sopa = bs4.BeautifulSoup(resultado.text, "lxml")

    tabla = sopa.find("table", class_="table table-striped")
    cantidad_bancos = len(tabla.select("tr"))
    contador = 1
    bancos = {}
    base = "https://simulador.condusef.gob.mx/condusefahorro/"

    for banco in range(cantidad_bancos - 1):
        fila = tabla.select("tr")[contador]

        if len(fila.select('td')) > 3:
            nombre_banco = fila.select('img')[0]['alt']
            img_banco = fila.select('img')[0]['src']
            imagen_curos_1 = requests.get(base + img_banco)

            # Guardar la imagen en la carpeta
            ruta_imagen = os.path.join(carpeta, nombre_banco + ".jpg")
            with open(ruta_imagen, "wb") as f:
                f.write(imagen_curos_1.content)

            # Obtener el color secundario
            color_secundario = obtener_color_secundario(ruta_imagen, 10)

            # Convertir el color secundario al formato 'rgba(r, g, b, 0.6)'
            color_rgb = f'rgba({color_secundario[0]}, {color_secundario[1]}, {color_secundario[2]}, 0.6)'

            # Guardar el color secundario en el diccionario de bancos
            bancos[nombre_banco] = {
                "tasa": fila.select('td')[3].getText(),
                "rgb": color_rgb
            }

        contador += 1

    for nombre, info in bancos.items():
        tasa_str = info["tasa"]
        tasa = float(tasa_str.strip('%')) / 100
        nuevo_banco = Banco(nombre=nombre, tasa=tasa, rgb=info["rgb"])
        nuevo_banco.save()

    return HttpResponse("Bancos generados exitosamente.")

def obtener_color_secundario(imagen, numero_colores):
    # Abrir la imagen
    img = Image.open(imagen)

    # Reducir los colores de la imagen a una paleta específica
    img_paleta = img.quantize(colors=numero_colores)

    # Obtener la paleta de colores
    paleta = img_paleta.getpalette()

    # Obtener el color dominante (el color con mayor frecuencia)
    color_dominante = paleta[:3]  # Los primeros tres valores (R, G, B) corresponden al color dominante

    # Obtener los colores secundarios (todos los colores excepto el dominante)
    colores_secundarios = [paleta[i:i+3] for i in range(0, len(paleta), 3) if paleta[i:i+3] != color_dominante]

    if colores_secundarios:
        # Devolver el primer color secundario
        color_secundario = colores_secundarios[0]
        return color_secundario
    else:
        return None