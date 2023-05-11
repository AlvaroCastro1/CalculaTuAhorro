from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def lista_bancos(pedido):
    return HttpResponse('Lista de Bancos')