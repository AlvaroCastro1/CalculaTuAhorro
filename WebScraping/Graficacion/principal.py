import bs4
import requests
import numpy as np
import matplotlib.pyplot as mp

url_base = "https://simulador.condusef.gob.mx/condusefahorro/datos_ppa.php?capital_inicial=25%2C000&ahorro=1%2C200&periodo=28&fecha_inicio_base=2006-01-02&fecha_fin_base=2023-02-26&durante=5"
resultado = requests.get(url_base)
sopa = bs4.BeautifulSoup(resultado.text, "lxml")

#print(sopa.select("title")[0].getText())

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
#print(bancos)
#tiempo escogido
tiempo=3
#deposito inicial 
deposito=20000
#Modelo para gaficar
func = lambda d,tasa,t: d*np.exp(tasa*t)

x = np.linspace(-10, 20, 100)  # Genera 100 valores equidistantes en el rango -10 a 10

for nombre, tasa_str in bancos.items():
    tasa = float(tasa_str.strip('%')) / 100
    y=func(deposito,tasa, x)
    
    print(nombre)
    #print(y)
    #solucion=ecuacion_dif(deposito,tasa, tiempo)  
    #print(solucion.lhs)
    #mp.scatter(tasa, float(solucion.rhs), color="blue", label=nombre)
    mp.plot(x,y, label=nombre)
mp.xlim(0,20)
mp.ylim(deposito-deposito/4, deposito+deposito)
mp.title('CRECIMIENTO DEL DEPOSITO EN FUNCION DEL INTERES ')
mp.xlabel("AÑOS")
mp.ylabel("CRECIMIENTO DEL DEPOSITO EN "+str(tiempo)+"AÑOS")
mp.grid()
mp.show()