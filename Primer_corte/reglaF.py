import re

"""Para la solución de la regla falsa utilizaremos las variables que estan dentro de la función
para poder hacer los calculos necesarios, a medida que vaya avanzando en el codigo"""


def reglaF(funcion, x_i, x_f, iteraciones=1000, error_relativo=0.001):
    """Tendremos un contador y un error de calculo cuyo valor sera de 101"""
    resultado = None
    cont = 0
    error_c = 101
    """Evaluacion de que la raiz se encuentre dentro del resultado"""
    if funcion(x_i) * funcion(x_f) <= 0:
        # calculo de solucion
        while cont <= iteraciones and error_c >= error_relativo:
            cont += 1
            """Calculo de la regla falsa (ecuación)"""
            resultado = x_f - ((funcion(x_f) * (x_f - x_i)) /
                               (funcion(x_f) - funcion(x_i)))
            """Valor absoluto"""
            error_c = abs((resultado - x_i)/resultado) * 100
            """valores a establecer"""
            if funcion(x_i) * funcion(resultado) >= 0:
                x_i = resultado
            else:
                x_f = resultado
        print("La solucion tiene una aproximacion de {:.3f}".format(resultado))
        print("Con un total de iteraciones {:.0f}".format(cont))
        print("Y se encontro un error relativo de {:.3f}".format(
            error_c) + "%")
    else:
        print("No es posible encontrar los valores.")

def calcular_reglaf():
    """Llamamos al método, cuya función lambda va a servir para establecer los valores de dichas variables"""
    reglaF(lambda x: 4*x**4-9*x**2+1, 1, 4, 2, 2)
    """Los valores que seran modificados son los 4 ultimos :) """
