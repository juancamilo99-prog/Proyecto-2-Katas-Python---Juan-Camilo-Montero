#Genera una función que, al recibir una frase, 
# devuelva una lista con la longitud de cada palabra. 
# Usa la función map().

def sendFrase(frase):
    lista = list(map(len, frase.split()))
    return lista

resultado = sendFrase("Hola mundo")
print(resultado)
    
