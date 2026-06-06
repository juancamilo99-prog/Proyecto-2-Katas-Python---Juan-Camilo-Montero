#Escribe una función que tome una lista de palabras y 
#una palabra objetivo como parámetros. La función debe 
# devolver una lista con todas las palabras de la 
#lista original que contengan la palabra objetivo.


listaPalabras = ["manzana", "banana", "naranja", "pera", "melocotón"]

def palabras_con_objetivo(lista, palabraObjetivo):
    palabras_con_objetivo = list(filter(
        lambda palabra: palabraObjetivo in palabra, lista
    ))
    return palabras_con_objetivo

resultado = palabras_con_objetivo(listaPalabras, "ana")
print(resultado)