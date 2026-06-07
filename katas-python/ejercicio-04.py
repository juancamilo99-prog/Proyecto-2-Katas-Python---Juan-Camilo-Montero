#Genera una función que calcule la diferencia entre los 
# valores de dos listas. Usa la función map().

listaValores1 = [1,5,11,15,19]
listaValores2 = [2,4,6,8,10]

#creamos una funcion para restar los parametros de las dos listas
def diferencia(x,y):
    return x - y


def calcularDiferencia(lista1, lista2):
    return list(map(diferencia,lista1,lista2))
    #otra manera de hacerlo seria con lambda
    #map(lambda x,y : x - y , lista1, lista2)


resultado = calcularDiferencia(listaValores1, listaValores2)
print(resultado)