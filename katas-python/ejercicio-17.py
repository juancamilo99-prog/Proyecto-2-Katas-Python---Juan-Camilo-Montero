#Crea una función que tome una lista de dígitos y 
#devuelva el número correspondiente. Por ejemplo, 
#[5,7,2] corresponde al número 572. 
#Usa la función reduce().
from functools import reduce

listaNumeros = [5,7,2]

def devolverNumeroLista(lista):

    numero = reduce(
        lambda num, x: num * 10 + x, lista
    )
    return numero

resultado = devolverNumeroLista(listaNumeros)
print(resultado)
