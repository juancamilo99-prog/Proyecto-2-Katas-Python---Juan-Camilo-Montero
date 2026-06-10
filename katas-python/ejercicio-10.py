#Escribe una función que reciba una lista de números 
#y calcule su promedio. Si la lista está vacía, 
#lanza una excepción personalizada y maneja el error adecuadamente.

lista_numeros = [2,5,7,6]
lista_vacia = ["",""]

def calcular_promedio(lista):
    try:
        suma = 0
        for numero in lista:
            suma += numero
            promedio = suma/len(lista)
        return promedio
    except Exception:
        print("No se puede tener una lista Vacia")

resultado = calcular_promedio(lista_numeros)
print(resultado)