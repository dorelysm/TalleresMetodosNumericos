"""
Proyecto final métodos numéricos

Opciones:
1. calculo de metodo biseccion 👍
2. calculo de metodo epsilon   👍
3. calculo de metodo secante   👍
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
#------------------------------------------------------------------
from Primer_corte.epsilon import calcular_epsilon
from Primer_corte.biseccion import metodo_biseccion
from Primer_corte.metodo_secante import metodo_secante
from Primer_corte.newton import *
from Primer_corte.reglaF import *
from Primer_corte.secante import *
from Primer_corte.taller_1 import conversionBinToDec
from Primer_corte.taller1_decToBin import conversionrDecToBin
from Primer_corte.taller2 import calcular_error
from Segundo_corte.derivacion import calcular_derivadas
from Segundo_corte.integracion import integracion
from Segundo_corte.ecuacionesDiferenciales import calcular_metodo_euler, calcular_metodo_rungeK
from Segundo_corte.lagrange import calcular_lagrange
from Tercer_Corte.gaussJordan import GaussJordan
from Tercer_Corte.descomposicionLU import descomposicion_lu
#------------------------------------------------------------------

opc = 1
while opc != 17:
    print("""
          Opciones:
            1. Calculo Biseccion
            2. Calculo Epsilon
            3. Calculo de la Secante
            4. Calculo de Newton
            5. Calculo de Regla Falsa
            6. Calculo metodo de la secante
            7. Conversion numero binario a decimal
            8. Conversion numero decimal a binario
            9. Calculo del error
            10. Calculo de derivación
            11. Calculo de Ecuaciones Diferenciales por método de Euler
            12. Calculo de Ecuaciones Diferenciales por método de Runge-Kutta
            13. Calculo de Integración Númerica
            14. Calculo de Lagrange
            15. Calculo de Gauss Jordan
            16. Calculo de Gauss Seidel
            17. Calculo de Descomposicion LU
            18. Salir
          """)
    opc = int(input('Ingrese su opción: '))
    if opc == 1:  # calcular biseccion
        metodo_biseccion()
        break
    elif opc == 2:
        calcular_epsilon()  # calcular epsilon
        break
    elif opc == 3:
        metodo_secante() #metodo de secante
        break
    elif opc == 4: #metodo de newton
        newton()
        break
    elif opc == 5: #metodo de regla falsa
        reglaF()
        break
    elif opc == 6: # metodo de la secante
        secante()
        break
    elif opc == 7:
        conversionBinToDec() #conversion binario a decimal
        break
    elif opc == 8:
        conversionrDecToBin()#conversion decimal a binario
        break
    elif opc == 9:
        calcular_error() #Calculo de error por distintos métodos
        break
    elif opc == 10: #Calculo de derivadas por distintos métodos
        calcular_derivadas()
        break
    elif opc == 11:
        calcular_metodo_euler() #Ecuaciones diferenciales por el metodo de euler
        break
    elif opc == 12:
        calcular_metodo_rungeK() #Ecuaciones diferenciales por el metodo de Ruge-Kutta
        break
    elif opc == 13:
        integracion() #Calculo de integrales
        break
    elif opc == 14: #lagrange
        calcular_lagrange()
        break
    elif opc == 15: #gauss jordan
        GaussJordan()
        break
    elif opc == 16: #gauss seidel
        break
    elif opc == 17: #descomposicion lu
        descomposicion_lu()
        break
    else:
        print("Fin del programa")
