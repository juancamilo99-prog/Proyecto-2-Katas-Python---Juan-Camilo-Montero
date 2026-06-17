#Crea una función que solicite al usuario ingresar una lista de nombres 
# y luego un nombre para buscar en esa lista. Si el nombre está en la 
# lista, imprime un mensaje indicando que fue encontrado; de lo contrario, 
# lanza una excepción.


def find_name():
    try:
        nombre_lista = []
        for tamanio in range(3):
            nombres = str(input("Escribe un nombre: "))
            nombre_lista.append(nombres)

            
        buscar_nombre = str(input("Escribe el nombre que quieres buscar: "))
        
        if buscar_nombre in nombre_lista:
            print(f"el nombre {buscar_nombre} , si se encuentra en la lista")
        else:
            raise Exception(f"el nombre {buscar_nombre} , no se encuentra en la lista")
    except Exception:
        print("Valor no soportado, vuelve a intentarlo")

find_name()