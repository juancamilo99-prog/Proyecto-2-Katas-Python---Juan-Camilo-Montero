#Crea una función que cuente el número de 
# caracteres en una cadena de texto dada.

from functools import reduce

cadena_texto = "Hola mundo bienvenidos"

def contar_caracter(cadena):
    
    texto = len(cadena.replace(" ", ""))
    return texto

resultado = contar_caracter(cadena_texto)
print(resultado)