#Crea una función lambda que filtre los números 
# impares de una lista dada.

lista_numeros = [1,2,3,4,5,6,7,8,9,10,11]

def numeros_impares(lista):
    obtener_numeros_impares = list(filter(
        lambda impar: impar % 2 == 1, lista
    ))
    return obtener_numeros_impares

resultado = numeros_impares(lista_numeros)
print(resultado)