"""
Proyecto final métodos numéricos

Opciones:
1. calcular epsilon
2. Metodo bisecion
3. secante
4. newton
5. regla falsa
6. derivadas
7. integrales
8. lagrange
9. ecuaciones diferenciales
10. gauss jordan
11. gauss seidel
    
"""
from Primer_corte.epsilon import *
from Primer_corte.biseccion import metodo_biseccion
from Primer_corte.metodo_secante import metodo_secante

from Tercer_Corte.gaussJordan import GaussJordan

opc = 1
while opc!=0:
    print("""
          Opciones:
            1. calcular epsilon
            2. Metodo bisecion
            3. secante
            4. newton
            5. regla falsa
            6. derivadas
            7. integrales
            8. lagrange
            9. ecuaciones diferenciales
            10. gauss jordan
            11. gauss seidel
            0. Salir
          """)
    opc = int(input('Ingrese su opción: '))
    
    if opc==1: #calcular epsilon
        calcular_epsilon()
    elif opc ==2:
        metodo_biseccion()
    elif opc ==3:
        metodo_secante()
    elif opc ==4:
        pass
    elif opc ==5:
        pass
    elif opc ==6:
        pass
    elif opc ==7:
        pass
    elif opc ==8:
        pass
    elif opc ==9:
        pass
    elif opc ==10:
        GaussJordan()
    elif opc ==11:
        pass
    