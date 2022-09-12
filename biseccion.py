from pickle import NONE
from re import A
import numpy as np
import math
#import matplotlib.pyplot as plt

fx = (lambda x: math.pow(x, 3) + 4 * math.pow(x, 2-10))
a = 1
b = 2
tolera = 0.0001
c = (a + b) / 2
fa = fx(a)
fb = fx(b)
fc = fx(c)

valor = np.sign(fa) * np.sign(fb)

if valor < 0:
    a = a 
    b = c
elif valor > 0:
    a = c
    b = b

tramo = b - a
print(c)
#a = float(input(print("Digite el valor de (A): ")))
#b = float(input(print("Digite el valor de (B): ")))
