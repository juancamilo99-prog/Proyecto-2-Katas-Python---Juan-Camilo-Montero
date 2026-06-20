#Crea la clase UsuarioBanco
#Representa a un usuario de un banco con su nombre, 
# saldo y si tiene o no cuenta corriente.
#Métodos: retirar_dinero, transferir_dinero, agregar_dinero.
#Código a seguir:
#Inicializar un usuario con nombre, saldo y un indicador (True o False) 
# de cuenta corriente.
#Implementar retirar_dinero para sustraer dinero del saldo, lanzando 
# un error si no es posible.
#Implementar transferir_dinero para transferir dinero desde otro usuario,
#  lanzando un error en caso de fallo.
#Implementar agregar_dinero para aumentar el saldo del usuario.
#Caso de uso:
# a. Crear dos usuarios: "Alicia" con saldo inicial de 100 
# y "Bob" con saldo inicial de 50, ambos con cuenta corriente.
#b. Agregar 20 unidades al saldo de Bob.
#c. Transferir 80 unidades de Bob a Alicia.
#d. Retirar 50 unidades del saldo de Alicia.

class UsuarioBanco:

    def __init__(self, nombre,saldo,cuenta_corriente):
        self.nombre = nombre
        self.saldo = saldo
        self.cuenta_corriente = cuenta_corriente

    def retirar_dinero(self,cantidad_retiro):
            if cantidad_retiro > self.saldo:
                print(f"{self.nombre} tiene saldo insuficiente")
            else:
                 self.saldo -= cantidad_retiro
                 print("retiro exitoso!")

    def transferir_dinero(self,destinatario_persona,cantidad_transferencia):
            if cantidad_transferencia > self.saldo:
              print(f"{self.nombre} tiene saldo insuficiente")
            else:
                self.saldo -= cantidad_transferencia
                destinatario_persona.saldo += cantidad_transferencia
                print("transferencia exitosa!")

    def agregar_dinero(self,cantidad_agregar):
         self.saldo += cantidad_agregar
         print("ingreso exitoso!")
                   


    def mostrar_info(self):
        print(f"el saldo de {self.nombre} actualmente es de: {self.saldo}")
        print(f"el usuario {self.nombre} tiene cuenta corriente? {self.cuenta_corriente}")


alicia = UsuarioBanco('Alicia', 100, True)
bob = UsuarioBanco('Bob', 50, True)

#Bob
bob.agregar_dinero(20)
#transferir bob a alicia
bob.transferir_dinero('Alicia', 80) #bob no podria transferir por tener saldo menor a la cantidad a transferir
#retirar saldo alicia
alicia.retirar_dinero(50)

#info bob
print("Info de bob")
bob.mostrar_info()

#info de alicia
print("Info de alicia")
alicia.mostrar_info()