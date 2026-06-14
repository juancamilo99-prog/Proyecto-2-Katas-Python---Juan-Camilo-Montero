#Crea una función que calcule el cubo de un 
# número dado mediante una función lambda.

import math

numero = int(input("digite su lado:"))

def obtener_cubo(lado):
    cubo = lambda x: math.pow(x,3)
    return cubo(lado)

resultado = obtener_cubo(numero)
print(resultado)