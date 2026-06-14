#Crea una función lambda que calcule el resto 
# de la división entre dos números dados.

numero1 = 5
numero2 = 2

def resto_numeros(dividendo, divisor):
    resto = lambda x,y: x%y
    return resto(dividendo, divisor)

resultado = resto_numeros(numero1, numero2)
print(resultado)