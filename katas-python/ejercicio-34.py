#Crea la clase Arbol
#Define un árbol genérico con un tronco y ramas como atributos.
#Métodos disponibles: 
# crecer_tronco, nueva_rama, crecer_ramas, quitar_rama, info_arbol.
#Código a seguir:
#Inicializar un árbol con un tronco de longitud 1 y una lista vacía de ramas.
#Implementar el método crecer_tronco para aumentar la longitud del tronco en una unidad.
#Implementar el método nueva_rama para agregar una nueva rama 
# de longitud 1 a la lista de ramas.
#Implementar el método crecer_ramas para aumentar en una unidad 
# la longitud de todas las ramas existentes.
#Implementar el método quitar_rama para eliminar una rama en una 
# posición específica.
#Implementar el método info_arbol para devolver información sobre 
# la longitud del tronco, el número de ramas y sus longitudes.
#Caso de uso:
#       a. Crear un árbol.
#        b. Hacer crecer el tronco una unidad.
#         c. Añadir una nueva rama.
#       d. Hacer crecer todas las ramas una unidad.
#        e. Añadir dos nuevas ramas.
#        f. Retirar la rama situada en la posición 2.
#        g. Obtener información sobre el árbol.

class Arbol:
    
    def __init__(self):
        self.troncos = 1
        self.ramas = []

    def crecer_tronco(self):
        self.troncos += 1

    
    def nueva_rama(self, cantidad):
        self.ramas.append(cantidad)


    def crecer_ramas(self):
        for i in range(len(self.ramas)):
            self.ramas[i] += 1


    def quitar_rama(self, posicion):
        if 0 <= posicion < len(self.ramas):
            self.ramas.pop(posicion)



    def info_arbol(self):
        return {
            "longitud_tronco": self.troncos,
            "numero_ramas": len(self.ramas),
            "longitud_ramas": self.ramas
        }
    

#casos de uso

#1. crear un arbol

arbol_nuevo = Arbol()

#2. hacer crecer el tronco una unidad

arbol_nuevo.crecer_tronco()

#3. añadir una nueva rama

arbol_nuevo.nueva_rama(1)

#4. hacer crecer todas las ramas una unidad

arbol_nuevo.crecer_ramas()

#5. añadir dos nuevas ramas

arbol_nuevo.nueva_rama(2)

#6. retirar la rama situada en la posicion 2

arbol_nuevo.quitar_rama(2)

#7. obtener informacion sobre el arbol

print(arbol_nuevo.info_arbol())
