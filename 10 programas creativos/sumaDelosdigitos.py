import math

def sumar(numero):
    if(numero==0):
        return numero
    else:
        return (numero-numero%10**exponente(numero))/(10**exponente(numero))+sumar(numero%10**exponente(numero))

def exponente(numero):
    return int(math.log10(numero))
     
print("El resultado es: ",sumar(int(input("Ingrese un numero \n"))))


