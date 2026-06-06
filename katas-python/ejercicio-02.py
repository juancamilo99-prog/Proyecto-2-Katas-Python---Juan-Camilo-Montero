#Dada una lista de números, 
# obtén una nueva lista con el 
# doble de cada valor. Usa la función map().

listaNumeros = [2,4,5,6,8]

def doblarvalores(lista):
    listDoblada = list(map(
        #usamos lambda para crear tomar cada numero de la lista 'x'
        #y multiplicarlo por 2
        lambda x: x*2, lista
    ))
    return listDoblada

resultado = doblarvalores(listaNumeros)
print(resultado)