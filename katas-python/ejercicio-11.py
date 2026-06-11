#Escribe un programa que pida al usuario que 
# introduzca su edad. Si el usuario ingresa un 
# valor no numérico o un valor fuera 
# del rango esperado (por ejemplo, menor que 0 o mayor que 120), 
# maneja las excepciones adecuadamente.

try:
    edadUsuario = int(input('Ingresa tu edad:'))
    if 0 <= edadUsuario <= 120:
        print(f"tu edad es correcta, y es: {edadUsuario}")
    else:
        print("Edad fuera del rango permitido")
except ValueError:
    print('El valor introducido tiene que ser numerico.')
