import bs4
import requests
import numpy as np
import matplotlib.pyplot as mp

url_base = "https://simulador.condusef.gob.mx/condusefahorro/datos_ppa.php?capital_inicial=25%2C000&ahorro=1%2C200&periodo=28&fecha_inicio_base=2006-01-02&fecha_fin_base=2023-02-26&durante=5"
resultado = requests.get(url_base)
sopa = bs4.BeautifulSoup(resultado.text, "lxml")

tabla = sopa.find("table", class_="table table-striped")
cantidad_bancos = len(tabla.select("tr"))
# print(f"hay {cantidad_bancos} bancos")

contador = 1
bancos={}
# se quita un elemento
for banco in range(cantidad_bancos -1):
    nombre_banco = tabla.select("tr")[contador].select('img')[0]['alt']
    tasa = tabla.select("tr")[contador].select('td')[3].getText()
    contador+=1
    bancos[nombre_banco] = tasa


def calcular_dinero_anio(tasa, tiempo, deposito):
    anios=[]
    dinero_anio=[]
    func = lambda d,tasa,t: d*np.exp(tasa*t)

    for i in range(0,tiempo,1):
        anios.append(i)

    for i in range(tiempo):
        dinero_anio.append(round(func(deposito, tasa,i),2))
    print(anios)
    print()
    print(dinero_anio)

#tiempo escogido
tiempo=3
#deposito inicial 
deposito=20000
calcular_dinero_anio(0.12, 3, 2000)