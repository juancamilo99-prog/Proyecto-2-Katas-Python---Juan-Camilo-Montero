#Crea una función que busque y devuelva el 
# primer elemento duplicado en una lista dada.

lista_numeros = [2,6,7,5,2,6,6]
repetidos = []

def find_repetidos(lista):

    for numero in lista:
        if lista.count(numero) > 1 and numero not in repetidos:
            repetidos.append(numero)
            return repetidos

resultado = find_repetidos(lista_numeros)
print(resultado)