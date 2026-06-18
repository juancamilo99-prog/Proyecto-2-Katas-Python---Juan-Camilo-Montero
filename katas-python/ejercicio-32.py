#Crea una función que tome un nombre completo 
# y una lista de empleados, busque el nombre en
# la lista y devuelva el puesto del empleado si 
# se encuentra; de lo contrario, devuelve un mensaje 
# indicando que la persona no trabaja aquí.

lista_empleados = [
    {"nombre": "Camilo", "puesto": "Gerente"},
    {"nombre": "Nerea Guisado", "puesto": "Comercial"},
    {"nombre": "Allan Josue", "puesto": "Comercial"},
    {"nombre": "Abigail", "puesto": "Administrativo"}
]
buscar_empleado_lista = input("Escribe el nombre del empleado: ")

def buscar_empleado(nombre_empleado, lista):
    try:
        for empleados in lista:
            if empleados["nombre"].lower() == nombre_empleado.lower():
                return(f"empleado {empleados['nombre']} su puesto es de: {empleados['puesto']}")
        return("la persona no trabaja aqui")
    except Exception:
        print("dato no valido!")
        ## se ejecuta siempre el finally para validar que no sea un numero.
    finally: 
        if nombre_empleado.isdigit():
            return "dato no valido. debes introducir un nombre"

resultado = buscar_empleado(buscar_empleado_lista, lista_empleados)
print(resultado)