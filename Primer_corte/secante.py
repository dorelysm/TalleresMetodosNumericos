"""
Programa para hallar una raíz por el 
método de la secante
"""

import math

# Funciones
"""
def f(x):
    x = math.radians(x)
    resultado = -math.cos(x) + x
    return resultado
"""


def secante(f, x1, x2, tol):
    error = 1e3
    n = 0
    x3 = 0
    while error > tol:
        x3 = x1-((x2-x1)/(f(x2)-f(x1)))*f(x1)
        x1 = x2
        x2 = x3
        error = abs(f(x3))
        n += 1
    return x3, n

def calcular_secante():
    Xsubcero = int(input('Ingrese x0: '))
    Xsubuno = int(input('Ingrese x1: '))
    tol = 1e-6
    def f(x): return x-math.cos(x)


    resultado, n = secante(f, Xsubcero, Xsubuno, tol)

    print("Raíz: {:4f}".format(resultado))
    print("Número de iteraciones: {:d}".format(n))
