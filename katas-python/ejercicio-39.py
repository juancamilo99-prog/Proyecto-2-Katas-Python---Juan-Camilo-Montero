#Escribe una función que tome dos parámetros: 
#figura (una cadena que puede ser "rectangulo", "circulo" o "triangulo") 
#y datos (una tupla con los datos necesarios para calcular el área de la figura).
import math

def obtener_figura(figura, tupla_area):
    if figura == "rectangulo":
        rectangulo = lambda base, altura: base*altura
        #accedemos a la posicion 0 y 1 de la tupla
        return rectangulo(tupla_area[0], tupla_area[1])
    if figura == "circulo":
        circulo = lambda radio: math.floor(math.pi * radio**2)
        return circulo(tupla_area[0])
    if figura == "triangulo":
        triangulo = lambda base,altura: math.floor((base*altura)/2)
        return triangulo(tupla_area[0], tupla_area[1])
    
print("La base del rectangulo es: ",obtener_figura("rectangulo", (2,3)))
print("La base del circulo es: ", obtener_figura("circulo",(2,)))
print("La base del triangulo es: ", obtener_figura("triangulo", (5,2)))
