from numpy import matrix, linalg
import numpy as np

def crear_matriz(n, m):
    matriz = np.zeros((n, m))
    
    print('Ingresa los datos de la matriz')
    
    for i in range(n):
        for j in range(m):
            x = float(input("Ingrese ({},{}): ".format(i,j)))
            matriz[i][j] = x
    
    return matriz

def gauss_jordan(): 
    n = int(input("Ingrese el tamaño de la matriz: "))
    matrizA = crear_matriz(n, n+1)
    solucion = np.zeros(n)
    print(solucion)
    
    
    return matrizA

matrizA=gauss_jordan()        
print(matrizA)