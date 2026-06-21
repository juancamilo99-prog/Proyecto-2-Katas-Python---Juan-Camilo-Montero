#Crea una función llamada procesar_texto
#Procesa un texto según la opción especificada: contar_palabras, 
# reemplazar_palabras o eliminar_palabra.
#Código a seguir:
#Crear una función contar_palabras que cuente el número de veces que 
# aparece cada palabra en el texto y devuelva un diccionario.
#Crear una función reemplazar_palabras para sustituir una palabra_original 
# por una palabra_nueva en el texto y devolver el texto modificado.
#Crear una función eliminar_palabra que elimine una palabra del texto y 
# devuelva el texto sin ella.
#Crear la función procesar_texto que reciba un texto, una opción 
# ("contar", "reemplazar", "eliminar") y un número variable de argumentos según la opción elegida.
#Caso de uso:
#Verificar el funcionamiento completo de procesar_texto.

def procesar_texto():
    #procesamos las opciones que quiera el usuario
    opcion = int(input("que opcion desea?" \
    "1. contar una palabra" \
    "2. reemplazar una palabra" \
    "3. eliminar una palabra"))

    if opcion == 1:
        print("contar palabra")
        texto = input("digite la palabra: ")
        return contar_palabras(texto)
    elif opcion == 2:
        print("reemplazar palabra: ")
        texto = input("digite el texto: ")
        old_palabra = input("digite la palabra que quieres remplazar: ")
        new_palabra = input("digite la palabra nueva: ")
        return reemplazar_palabras(texto, old_palabra, new_palabra)
    elif opcion == 3:
        print("eliminar palabra: ")
        texto = input("digite el texto: ")
        texto_eliminar = input("digite la palabra a eliminar: ")
        return elminar_palabra(texto, texto_eliminar)
    else:
        print("opcion no valida, vuelvelo a intentar!")


def contar_palabras(texto):
    #separamos la cadena por cada palabra
    palabras = texto.split()
    contador_palabras = {}
    #recorremos las palabras
    for palabra in palabras:
        #preguntamos si esta palabra ya existe dentro del contador
        if palabra in contador_palabras:
            #si existe, le sumamos 1 al contador
            contador_palabras[palabra]+=1
        else:
            #si no existe, la añadimos por primera vez
            contador_palabras[palabra] = 1

    print(f"cantidad de la palabra {contador_palabras}")
    return contador_palabras

def reemplazar_palabras(texto, palabra_antigua, palabra_nueva):
    #usamos replace para reemplazar replace(old,new)
    return print(texto.replace(palabra_antigua, palabra_nueva))


def elminar_palabra(texto, palabra_eliminar):
    #separamos las cadena con split
    palabras = texto.split()
    nueva_lista = []
    #recorremos las palabras
    for p in palabras:
        #si la palabra es diferente a la palabra eliminar
        if p != palabra_eliminar:
            #las añadimos a una nueva lista
            nueva_lista.append(p)
    return print(" ".join(nueva_lista))

    
procesar_texto()

