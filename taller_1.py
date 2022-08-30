def binarioDecimal(binario):
    dec = int(str(binario), 2)
    return dec

def binarioDecDecimal(binario):
    n = 2
    decimal = 0
    binario = str(binario)
    for i in range(len(binario)):
        x = int(binario[i]) * 1/n
        decimal = decimal + x
        n = n*2
    return decimal

def separarNumero(numero):
    entero, puntoPos = parteEntera(numero)
    print('entero: ' + str(entero))
    decimal = 0
    if puntoPos != len(str(numero)):
        decimal = parteDecimal(numero, puntoPos)
    return entero, decimal

def parteEntera(numero):
    numeroStr = str(numero)
    entero = ""
    puntoPos = len(numeroStr)
    for i in range (len(numeroStr)):
        if (numeroStr[i] != "."):
            entero = entero + numeroStr[i]
        elif (numeroStr[i] == "."):
            puntoPos = i
            break
    return int(entero), puntoPos

def parteDecimal(numero, puntoPos):
    numero = str(numero)
    decimal = ""
    for i in range(len(numero)):
        if (i > puntoPos):
            decimal = decimal + numero[i]
    intDecimal = int(decimal)
    return intDecimal

def extraerSigno(numero):
    numero = str(numero)
    signo = "0"
    if numero[0] == "-":
        signo = "1"
        numero = numero[1:len(numero)]
    return signo, float(numero)


signo = input('Signo: ')
exponente = input('Exponente: ')
mantisa = input('Mantisa: ')

numBin = signo + ' ' + exponente + ' ' + mantisa
print(numBin)

if signo == '0':
    decSigno = '+'
elif signo == '1':
    decSigno = '-'
    
expMax = 2**(len(exponente))-1
exp = binarioDecimal(exponente)
#print(exp)
e = exp - expMax//2

notacionCien = decSigno + "1." + mantisa + ' x 2^' + str(e)
print(notacionCien)

puntoFlotante = ""

if e < 0:
    for i in range(abs(e)):
        puntoFlotante = puntoFlotante + '0'
    puntoFlotante = puntoFlotante + '.1'
    puntoFlotante = puntoFlotante + mantisa
elif e > 0:
    puntoFlotante = puntoFlotante + '1'
    for i in range(e):
        puntoFlotante = puntoFlotante + mantisa[0]
        mantisa = mantisa[1: len(mantisa)]
    puntoFlotante = puntoFlotante + '.' + mantisa
elif e == 0:
    puntoFlotante = '1.' + mantisa
    
puntoFlotante = decSigno + puntoFlotante
print(puntoFlotante)

puntoFlotante, signo = extraerSigno(puntoFlotante)
entero, decimal = separarNumero(puntoFlotante)

print('parte entera: '+ str(entero))
print('parte decimal: ' + str(decimal))

decEntero = binarioDecimal(entero)
decDecimal = binarioDecDecimal(decimal)

numero = str(decSigno) + str(decEntero) + str(decDecimal)

print('El numero en base 10 es: ' + numero)


