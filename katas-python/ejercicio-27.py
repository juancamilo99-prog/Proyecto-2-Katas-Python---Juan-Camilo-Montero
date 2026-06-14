#Crea una función que calcule el promedio de una lista de números.

from functools import reduce

lista_numeros = [8,7,4,2]

def calcular_promedio(lista):

    #otra forma mas rapida para hacerla
    # return sum(lista) / len(lista)
    
    suma = reduce(
        lambda x,y: (x+y), lista
    )
    promedio = suma/len(lista)
    return promedio

resultado = calcular_promedio(lista_numeros)
print(resultado) 