#Escribe un programa que pida al usuario dos números 
# e intente dividirlos. Si el usuario ingresa un valor 
# no numérico o intenta dividir por cero, maneja esas 
# excepciones de manera adecuada y muestra un mensaje i
# ndicando si la división fue exitosa o no.

try:
    numero1 = int(input("Ingrese numero 1:"))
    numero2 = int(input("Ingrese numero 2:"))

    resultado = numero1 / numero2

    print(f"el resultado de la division es: {round(resultado,2)}")

except ValueError:
    print("Por favor, ingrese un numero valido!")
except ZeroDivisionError:
    print("No se puede dividir entre 0")
