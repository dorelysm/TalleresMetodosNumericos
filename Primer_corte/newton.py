from math import *
from re import X


def expo(x):
    """Funcion de prueba"""
    return x**2 + exp(-2*x) - 2*x*exp(-x)
    # retorna expo(x)= x**2 + e**-2x - 2xe**-x


def expoprima(x):
    """Derivada de la funsion de prueba"""
    return 2*x - 2*exp(-2*x) - 2*exp(-x) + 2*x*exp(-x)
    # returna expoprima(x)=d/dx expo(x)


def trig(x):
    """Funcion de prueba"""
    return cos(x) - x
    # retorna trig(x)= cos(x)-x


def trigprima(x):
    """Derivada funcion de prueba"""
    return -sin(x) - 1
    # retorna trigprima(x)= d/dx trig(x)


def newton(f, fprima, pO, tol, n):
    """
    Se realiza la implementacion del metodo de Newton
    Entradas:
    f -- funcion
    fprima -- derivada de la funcion f
    p0 -- aproximacion inicial
    tol -- tolerancia
    n -- numero maximo de iteraciones a realizar
    Salidas:
    p va a ser la aproximacion a cero de f
    None en caso de iteraciones agotadas
    """
    i = 1
    while i <= n:
        p = pO - f(pO)/fprima(pO)
        print("Iter = {0:<2}, p = {1:.12f}".format(i, p))
        if abs(p - pO) < tol:
            return p
        pO = p
        i += 1
    print("Iteraciones agotadas: Error!")
    return None

def calcular_newton():
    # trig(x), trigprima(x), pO = pi/4, TOL=10**-8, No=100
    print("Newton funcion trig(x):")
    newton(trig, trigprima, pi/4, 1e-8, 100)

    # expo(x), expoprima(x), po=4.0, TOL=10**-8, No=100
    print("Newton funcion expo(x):")
    newton(expo, expoprima, 4, 1e-8, 100)
