#Crea una función que retorne las palabras de una lista 
# que comiencen con una letra en específico. 
# Usa la función filter().

listaPalabras = ["manzana", "banana", "naranja", "pera", "melocotón"]

def findPalabra(lista, letra):
    
    buscar_por_letra = list(filter(
        lambda palabra: letra in palabra, lista
    ))

    return buscar_por_letra

resultado = findPalabra(listaPalabras,"m")
print(resultado)