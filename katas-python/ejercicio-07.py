#Genera una función que convierta una lista de tuplas 
# a una lista de strings. Usa la función map().

listaTupla = (2, 1, 4, 5)

def convertListString(tupla):
    return list(map(str, tupla))

resultado = convertListString(listaTupla)
print(resultado)
    