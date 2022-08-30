# --------------------------------------------
# Funcion para Convertir el numero decimal a binario
def decimalBinario(decimal):
    bina = " "
    bin(int(dec))
    binario = int(bin(decimal)[2:])
    return binario

# -------------------------------------------
# Funcion para Convertir el numero binario a decimal
def binarioDecimal(binario):
    dec = int(str(binario), 2)
    return dec

# Funcion para Convertir la parte decimal de un numero binario a decimal
def parteDecimalABinario(decimal):
    binD = ""
    decimal = float("0." + str(decimal))
    for i in range(10):
        decimal = decimal * 2
        if (str(decimal)[0] == "0"):
            binD = binD + "0"
        elif (str(decimal)[0] == "1"):
            decimal = decimal - 1
            binD = binD + "1"
    return binD
        
# -------------------------------------------
#Toma un numero decimal y separa la parte entera
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

#Toma un numero decimal y separa la parte decimal
def parteDecimal(numero, puntoPos):
    numero = str(numero)
    decimal = ""
    for i in range(len(numero)):
        if (i > puntoPos):
            decimal = decimal + numero[i]
    intDecimal = int(decimal)
    return intDecimal

#Toma un numero decimal y separa la parte entera y decimal
def separarNumero(numero):
    entero, puntoPos = parteEntera(numero)
    decimal = 0
    if puntoPos != len(str(numero)):
        decimal = parteDecimal(numero, puntoPos)
    return entero, decimal

def extraerSigno(numero):
    signo = "0"
    if numero[0] == "-":
        signo = "1"
        numero[0] = ""
    return signo

def calcularExpMax(exponente):
    bitsExp = len(str(exponente))
    expMax = 2**bitsExp
    return expMax

def calcularE(exp, expMax):
    decExp = binarioDecimal(exp)
    e = decExp - expMax//2
    return e

def binAPuntoFlotante(signo, exp, mantisa):
    numeroBin = signo + ' ' + exp + ' ' + mantisa
    print(numeroBin)
    numeroPF = ""
    if signo == "1":
        numeroPF = numeroPF + "-"
    
    

# --------------------------------------------
#Calculo de epsilon
def epsilon():
    epsilon = 1
    while (epsilon + 1) > 1:
        epsilon /= 2
    epsilon = 2 * epsilon
    print(f"El valor de Epsilon es {format(epsilon)}")
# --------------------------------------------
menu = int(input("""Menú principal:
1.Convertir decimal a binario
2.Convertir binario a decimal
4.Calcular Epsilon
5.Salir
Digite la opcion: \n"""))

while menu != 5:
    if menu == 1:
        print("Dame un número decimal, para tranformarlo a binario:")
        dec = float(input())
        entero, decimal = separarNumero(dec)
        print(f"Parte entera - {format(entero)}")
        print(f"Parte decimal - .{format(decimal)}")
        numero_binario = str(decimalBinario(entero)) + "." + parteDecimalABinario(decimal)
        print("El numero en binario punto flotante es: " + numero_binario)
    if menu == 2:
        #print(f"Dame un número en binario, para transformalo a decimal")
        #bin = float(input())
        #numBits = int(input("Ingrese el número de bits: "))
        #numMantisa = int(input("Ingrese el número de bits de la mantisa: "))
        
        signo = int(input("Ingrese el signo (0-1): "))
        exponente = int(input("Ingrese el exponente: "))
        mantisa = int(input("Ingrese la mantisa: "))
        
        binAPuntoFlotante(signo, exponente, mantisa)
        
        enteroBin, decimalBin = separarNumero(bin)
        print(f"Parte entera - {format(enteroBin)}")
        print(f"Parte decimal - {format(decimalBin)}")
        numero_decimal = str(binarioDecimal(enteroBin))
        print(f"El número {format(bin)} en decimal es {format(numero_decimal)}")
    if menu == 4:
        epsilon()
    break
