#Para una lista con elementos de tipo integer y string, 
# obtén una nueva lista solo con los valores int. 
# Usa la función filter().

lista_variada = [2, "hola", 5, 20, "bienvenidos",9]

def obtener_solo_integer(lista):
    lista_numeros = list(filter(
        lambda enteros: type(enteros) == int, lista
    ))
    return lista_numeros

resultado = obtener_solo_integer(lista_variada)
print(resultado)