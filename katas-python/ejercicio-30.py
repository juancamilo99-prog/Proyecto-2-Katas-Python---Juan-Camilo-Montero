#Crea una función que determine si dos palabras 
# son anagramas,
# es decir, si están formadas por las mismas 
# letras pero en diferente orden.

palabra_uno = "roma"
palabra_dos = "vida"

def buscar_anagrama(palabra1, palabra2):
    if sorted(palabra1) == sorted(palabra2):
        print("la palabra es anagrama")
        return True
    else:
        print("la palabra no es anagrama")
        return False
    
resultado = buscar_anagrama(palabra_uno, palabra_dos)
print(resultado)