"""
Programa para hallar una raíz por el
método de la secante
"""

import math

# Funciones
def funcion(x):
    x = math.radians(x)
    resultado = math.cos(x) + x
    return resultado

def secante(funcion, Xsubcero, Xsubuno, tol):
    error = 1e3
    n = 0
    Xsubn = 0

    while error > tol:
        Xsubn = Xsubcero - \
            ((Xsubuno - Xsubcero)/(funcion(Xsubuno) -
             funcion(Xsubcero))) / funcion(Xsubcero)
        Xsubcero = Xsubuno
        Xsubuno = Xsubn

        error = abs(funcion(Xsubn))
        n += 1

    return Xsubn, n

def metodo_secante():
    Xsubcero = int(input('Ingrese x0: '))
    Xsubuno = int(input('Ingrese x1: '))
    tol = 1e-4

    resultado, n = secante(funcion, Xsubcero, Xsubuno, tol)
    print("")
    print("Raíz: {:4f}".format(resultado))
    print("Número de iteraciones: {:d}".format(n))
