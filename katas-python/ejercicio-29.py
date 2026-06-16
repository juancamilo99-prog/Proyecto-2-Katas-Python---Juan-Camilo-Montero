#Crea una función que convierta una variable en una cadena de texto 
# y enmascare todos los caracteres con el carácter '#' excepto 
# los últimos cuatro.

variable_texto = 123456

def convertir_texto(variable):
    
    cadena = str(variable)
    if len(cadena) <= 4:
        return cadena
    #multiplicamos el # por la cantidad  restada de la longitud de la cadena
    return "#" * (len(cadena)-4) + cadena[-4:]

resultado = convertir_texto(variable_texto)
print(resultado)