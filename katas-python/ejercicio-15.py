#Crea una función lambda que sume 3 a cada número 
# de una lista dada.

listaNumeros = [3,5,7,2,8]

def funLambda(lista):

    sumaNumeros = list(map(
        lambda x: x + 3, lista
    ))
    return sumaNumeros

resultado = funLambda(listaNumeros)
print(resultado)