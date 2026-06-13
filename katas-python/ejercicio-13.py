#Genera una función que, para un conjunto de caracteres, 
# devuelva una lista de tuplas con cada letra en mayúsculas 
# y minúsculas. 
# Las letras no pueden estar repetidas. 
# Usa la función map().

def conversionTuplas(caracteres):
    return (caracteres.upper(), caracteres.lower())

def listaTuplas(palabras):
    letras = set(palabras.replace(" ", "").lower())
    return list(map(conversionTuplas, letras))

resultado = conversionTuplas("Hola PythOn")
print(resultado)