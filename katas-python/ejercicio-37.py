#Genera un programa que nos indique si es de noche, de día o 
# de tarde 
# según la hora proporcionada por el usuario.
import datetime

def obtener_hora(hora):
    if  6 <= hora < 12:
        #hora mayor de 6 y hora menor de 12
        print("Es de dia!")
    elif 12 <= hora < 20:
        print("Es de tarde!")
    else:
        print("Es de noche!")


hora_elegida = int(input("digite la hora (0-23): "))
obtener_hora(hora_elegida)

