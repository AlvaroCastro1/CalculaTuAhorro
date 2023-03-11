import bs4
import requests

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
print(bancos)

# bancos=[]
# for td in tabla.findAll('img'):
#     print( td )
#     if ".jpg" in td.getText():
#         bancos.append( td.getText() )
#     if "%" in td.getText():
#         bancos.append( td.getText() )


# nombre de bancos
# for td in tabla.findAll('img'):
#     print( td['alt'] )