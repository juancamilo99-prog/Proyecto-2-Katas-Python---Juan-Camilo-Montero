#Crea una función lambda que sume elementos correspondientes de dos listas dadas.

lista_1 = [3,6,7,2]
lista_2 = [7,1,5,6]

def sumar_elementos(lista1, lista2):
    suma = list(map(
        lambda x,y: x+y, lista1, lista2
    ))
    return suma

resultado = sumar_elementos(lista_1, lista_2)
print(resultado)