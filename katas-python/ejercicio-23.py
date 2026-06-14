#Concatena una lista de palabras. 
# Usa la función reduce().

from functools import reduce

lista_palabras = ["Hola", "mundo", "bienvenidos", "a", "python"]

def concatenar_palabras(lista):

    palabra_completa = reduce(
        lambda x,y: x+" "+y, lista 
    )
    return palabra_completa

resultado = concatenar_palabras(lista_palabras)
print(resultado)
