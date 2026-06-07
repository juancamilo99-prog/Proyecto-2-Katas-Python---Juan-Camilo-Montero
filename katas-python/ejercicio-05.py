#5 .Escribe una función que tome una lista de números como 
#parámetro y un valor opcional nota_aprobado (por defecto 5). 
#La función debe calcular la media de los números en la lista 
# y determinar si la media es mayor o igual que nota_aprobado. 
# Si es así, el estado será "aprobado"; de lo contrario, "suspenso". 
# La función debe devolver una tupla que contenga la media y el estado.

#creamos la lista de numeros como parametros
listaNotas = [5, 10, 3, 8, 9, 1]
#creamos el valor opcion nota_aprobado
nota_aprobado = 5

def calcular_media_lista(lista):
    suma = 0

    for listaRecorrido in lista:
        suma += listaRecorrido
        media = suma/len(lista)
        if media >= nota_aprobado:
            estado = "aprobado"
        else:
            estado = "reprobado"
    return media, estado

resultado = calcular_media_lista(listaNotas)
print(resultado)




