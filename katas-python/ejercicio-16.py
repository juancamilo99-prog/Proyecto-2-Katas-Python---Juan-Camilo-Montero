#Escribe una función que tome una cadena de texto 
# y un número entero n como parámetros y devuelva 
# una lista de todas las palabras que sean más 
# largas que n. Usa la función filter().

texto = "Hola mundo bienvenidos a python"
numero = 5

def palabrasMasLargas(cadena, cantidad):
    
    lista = list(filter(
        lambda x: len(x) > cantidad, cadena.split()
        ))
    return lista

resultado = palabrasMasLargas(texto, numero)
print(resultado)