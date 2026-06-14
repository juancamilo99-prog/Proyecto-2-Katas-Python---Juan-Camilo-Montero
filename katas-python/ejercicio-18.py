#Escribe un programa en Python que cree una lista de diccionarios 
# con información de estudiantes (nombre, edad, calificación) y 
# use filter para extraer a los estudiantes con una calificación 
# mayor o igual a 90.

diccionario_estudiantes = [
    {"nombre": "juan", "edad": 20, "calificacion": 90},
    {"nombre": "maria", "edad": 18, "calificacion": 60},
    {"nombre": "jose", "edad": 25, "calificacion": 40},
    {"nombre": "eli", "edad": 21, "calificacion": 100}
]

def extrar_datos_estudiantes(lista):
    diccionario_aprobados = list(filter(
        lambda aprobados: aprobados["calificacion"] >= 90,lista
    ))
    return diccionario_aprobados

resultado = extrar_datos_estudiantes(diccionario_estudiantes)
print(resultado)
