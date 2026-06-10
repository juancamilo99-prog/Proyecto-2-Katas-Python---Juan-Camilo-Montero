#Escribe una función que tome una lista de nombres de mascotas 
# como parámetro y devuelva una nueva lista excluyendo ciertas 
# mascotas prohibidas en España. La lista de mascotas a excluir 
# es ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]. 
# Usa la función filter().

listaNombres = ["Perro", "Gato", "Mapache", "Loro", "Cocodrilo", "Oso","Raton"]
listaProhibidas = ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]

def findListPermitidas(lista):
    listaNombresPermitidos = list(filter(
        lambda findPalabra: findPalabra not in listaProhibidas, lista
    ))
    return listaNombresPermitidos

resultado = findListPermitidas(listaNombres)
print(resultado)