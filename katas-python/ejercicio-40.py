#Escribe un programa en Python que utilice condicionales para determinar 
# el monto final de una compra en una tienda en línea, después 
# de aplicar un descuento. El programa debe:
#a. Solicitar al usuario el precio original de un artículo.
#b. Preguntar si tiene un cupón de descuento (respuesta sí o no).
#c. Si la respuesta es sí, solicitar el valor del cupón de descuento.
#d. Aplicar el descuento al precio original, siempre que el valor del 
# cupón sea válido (mayor a cero).
#e. Mostrar el precio final de la compra, considerando o no el descuento.
#f. Usar estructuras de control de flujo (if, elif, else) 
# para llevar a cabo las acciones.

def calcular_precio_final():
    monto_compra = float(input("digite el monto de la compra: "))
    existe_cupon = input("tiene cupon? si/no")
    if existe_cupon == "si":
        return cupon_descuento(monto_compra)
    else:
        print("no tienes cupon!")
        print("El precio final es: ", monto_compra)
        return monto_compra

def cupon_descuento(monto):
        cantidad_cupon = int(input("de cuanto es el cupon?"))
        if cantidad_cupon > 0:
            descuento = (monto*cantidad_cupon)/100
            resultado = monto-descuento
            print("el total del producto con descuento es: ",resultado)
            return resultado
        else:
             print("cupon no valido!")
             return monto
        

calcular_precio_final()
