"""
Proyecto final métodos numéricos

Opciones:
1. calculo de metodo biseccion
2. calculo de metodo epsilon
3. calculo de metodo secante
4. calculo de metodo newton
5. calculo de metodo regla falsa
6. calculo de metodo secante
7. calculo conversiones de numeros binario en forma de punto flotante
8. calculo de conversion numero binario a decimal
9. calculo del error
10. calculo de metodo de biseccion
11. calculo de derivacion
12. calculo de ED
13. calculo de integracion
14. calculo de integracion numerica
15. calculo de metodo de lagrange 
16. calculo de gauss jordan
17. calculo de gauss seidel
"""
from Primer_corte.epsilon import *
from Primer_corte.biseccion import metodo_biseccion
from Primer_corte.metodo_secante import metodo_secante

from Tercer_Corte.gaussJordan import GaussJordan

opc = 1
while opc != 18:
    print("""
          Opciones:
            1. calculo Biseccion
            2. calculo Epsilon
            3. calcul de la Secante
            4. calculo de Newton
            5. Calculo de Regla Falsa
            6. Calculo metodo de la secante
            7. Calculo numero binario en forma punto flotante
            8. Conversion numero binario a decimal
            9. Calculo del error
            10. Calculo método de bisección
            11. Calculo de derivación
            12. Calculo de Ecuaciones Diferenciales
            13. Calculo de Integración
            14. Calculo de Integración Númerica
            15. Calculo de Lagrange
            16. Calculo de Guass Jordan
            17. Calculo de Guass Seidel
            18.. Salir
          """)
    opc = int(input('Ingrese su opción: '))
    if opc == 1:  # calcular biseccion
        metodo_biseccion()
        break
    elif opc == 2:
        calcular_epsilon() # calcular epsilon
        break
    elif opc == 3:
        metodo_secante()
        break
    elif opc == 4:
        break
    elif opc == 5:
        break
    elif opc == 6:
        break
    elif opc == 7:
        break
    elif opc == 8:
        break
    elif opc == 9:
        break
    elif opc == 10:
        GaussJordan()
        break
    elif opc == 11:
        break
    elif opc == 12:
        break
    elif opc == 13:
        break
    elif opc == 14:
        break
    elif opc == 15:
        break
    elif opc == 16:
        break
    elif opc == 17:
        break
    else:
        print("Fin del programa")
