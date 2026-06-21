#Escribe un programa que determine qué calificación en texto 
# tiene un alumno según su calificación numérica.
#Reglas:
#        0 - 69: insuficiente
#        70 - 79: bien
#        80 - 89: muy bien
#        90 - 100: excelente

def determinar_calificacion(calificacion):
    if 0 <= calificacion <= 69:
        print("tu calificacion es insuficiente!")
    elif 70 <= calificacion <= 79:
        print("tu calificacion es bien!")
    elif 80 <= calificacion <= 89:
        print("tu calificacion es muy bien!")
    elif 90 <= calificacion <= 100:
        print("tu calificacion es excelente!")
    else:
        print("calificacion no valida!")

try:
    calificacion = int(input("digite tu calificacion: "))
    determinar_calificacion(calificacion)
except ValueError:
    print("debes introducir una nota numerica!")
