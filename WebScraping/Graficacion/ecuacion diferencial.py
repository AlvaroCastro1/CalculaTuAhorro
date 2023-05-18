from sympy import *
import numpy

def ecuacion_dif(d, k, y):
    t= symbols("t")
    N= Function("N")
    #k es la tasa de interes en porcentaje
    # d es la cantidad de dinero a agregar al abrir la cuenta
    # y es el tiempo que se desea calcular el rendimiento
    ed=Eq(N(t).diff(t)-k*N(t),0)
    CI={N(0):d}
    solucion_particular=dsolve(ed,N(t), ics=CI)
    print(solucion_particular)
    solucion= solucion_particular.subs('t', y)
    print(solucion)
    return solucion
    
    
deposito_Inicial=float(input("Ingrese el deposito inicial: "))
tasa_interes=float(input("Ingrese la tasa de interes: "))
tiempo=float(input("Ingrese el tiempo a aproximar: "))
ecuacion_dif(deposito_Inicial,tasa_interes,tiempo )