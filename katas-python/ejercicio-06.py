#Escribe una función que calcule el factorial 
# de un número de manera recursiva.

def findFactorial(n):
     if n == 0:
          return 1
     #retornamos el numero por el numero menos cada vez
     #se active recursivamente
     return n * findFactorial(n - 1)
print(findFactorial(5))