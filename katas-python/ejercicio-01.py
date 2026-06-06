#Escribe una función que reciba una cadena de 
# texto como parámetro y devuelva un diccionario 
# con las frecuencias de cada letra en la cadena. 
# Los espacios no deben ser considerados.

#definimos el nombre de la funcion y el parametro
def contarLetras(cadenaString):
    #creamos el diccionario vacio
    diccionarioFrecuenta = {}
    for letra in cadenaString:
        #recorremos el string letra por letra
        if letra != " ":
            #si la letra ya esta en el diccionario, sumamos 1 a su valor
            if letra in diccionarioFrecuenta:
                diccionarioFrecuenta[letra] += 1
            else:
                #si la letra no esta en el diccionario, la agregamos con valor 1
                diccionarioFrecuenta[letra] = 1
    return diccionarioFrecuenta
cadena = "Hola mundo"
resultado = contarLetras(cadena)
print(resultado)