#Calcula la diferencia total en los valores de una lista. 
#Usa la función reduce().

from functools import reduce

lista_numeros = [2,6,8,9]

def calcular_diferencia(lista):

    diferencia = reduce(
        lambda x,y: x-y, lista
    )
    return diferencia

resultado = calcular_diferencia(lista_numeros)
print(resultado)