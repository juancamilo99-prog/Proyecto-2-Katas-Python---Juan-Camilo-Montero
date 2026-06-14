#Dada una lista numérica, obtén el producto 
# total de los valores. 
# Usa la función reduce().

from functools import reduce

lista_numeros = [2,3,6,7]

def producto_numeros(lista):

    producto = reduce(
        lambda x,y: x*y, lista
    )
    return producto

resultado = producto_numeros(lista_numeros)
print(resultado)