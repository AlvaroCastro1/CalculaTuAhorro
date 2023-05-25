import requests
import bs4
from django.shortcuts import render
from django.http import HttpResponse
from .models import Banco
from django.views.generic.list import ListView
from django.http.response import JsonResponse
# Create your views here.

def inicio(request):
    labels = []
    data = []
    
    bancos = Banco.objects.order_by('-tasa')[:5]
    for bank in bancos:
        labels.append(bank.nombre)
        data.append(float(bank.tasa))
    return render(request, 'base/inicio.html', {'labels':labels, 'data': data})

class Lista_Bancos(ListView):
    model = Banco

def lista_bancos(pedido):
    return HttpResponse('Lista de Bancos')

def generar_bancos(request):
    url_base = "https://simulador.condusef.gob.mx/condusefahorro/datos_ppa.php?capital_inicial=25%2C000&ahorro=1%2C200&periodo=28&fecha_inicio_base=2006-01-02&fecha_fin_base=2023-02-26&durante=5"
    resultado = requests.get(url_base)
    sopa = bs4.BeautifulSoup(resultado.text, "lxml")

    tabla = sopa.find("table", class_="table table-striped")
    cantidad_bancos = len(tabla.select("tr"))
    contador = 1
    bancos = {}
    # se quita un elemento
    for banco in range(cantidad_bancos - 1):
        nombre_banco = tabla.select("tr")[contador].select('img')[0]['alt']
        tasa = tabla.select("tr")[contador].select('td')[3].getText()
        contador += 1
        bancos[nombre_banco] = tasa

    for nombre, tasa_str in bancos.items():
        tasa = float(tasa_str.strip('%')) / 100
        nuevo_banco = Banco(nombre=nombre, tasa=tasa)
        nuevo_banco.save()

    return HttpResponse("Bancos generados exitosamente.")