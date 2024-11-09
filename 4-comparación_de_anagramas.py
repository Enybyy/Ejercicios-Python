"""
Escribe una función que reciba dos cadenas de texto y devuelva True si las cadenas son anagramas 
(es decir, contienen las mismas letras en cualquier orden), y False en caso contrario.

Ejm:
are_anagrams("listen", "silent")  # True
are_anagrams("hello", "world")    # False

"""

def anagrama(texto1, texto2):
    
    if len(texto1) == len(texto2):
    
        cadena = []
        
        for t1 in texto1:
            cadena.append(t1)
            
        for t2 in texto2:
            
            if t2 in cadena:
                return True
            else:
                return False
    else:
        return False

texto1 = input(str("Ingresar primera palabra: "))
texto2 = input(str("Ingresar segunda palabra: "))

print(anagrama(texto1,texto2))