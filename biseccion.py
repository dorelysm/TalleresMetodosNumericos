import math

iteraciones = 0
f_max = 999999

e = input("Ingrese la función a resolver: ")
x_a = float(input("Ingrese el valor de la cota superior: "))
x_b = float(input("Ingrese el valor de la cota inferior: "))
tolera = float(input("Ingrese el valor de la tolerancia: "))


def biseccion(x):
    return eval(e)


while abs(f_max) >= tolera:
    puntoIntermedio = ((x_a + x_b) / 2)
    f_a = biseccion(x_a)
    f_b = biseccion(x_b)
    f_c = biseccion(puntoIntermedio)

    iteraciones += 1

    print(" x_a: " ,x_a, " x_b: ", x_b, " c: ", puntoIntermedio, " f_c: ", f_c, " N_itera: ", iteraciones)
    #print(f"El valor ingresado de x_a es el siguiente {x_a}")
    #print(f"El valor ingresado de x_a es el siguiente {x_b}")
    #print(f"Punto medio es {f_c}")
    #print(f"El total de iteraciones que hubo fue el siguiente: {iteraciones}")

    if ((f_a * f_c) < 0):
        x_b = puntoIntermedio
    elif ((f_b * f_c) < 0):
        x_a = puntoIntermedio

    if abs(f_c) < tolera:
        break

print(f"La raíz buscada es {puntoIntermedio}")
