"""
    Ejercicio: Escribe una función que reciba un número entero y devuelva la suma de sus dígitos.
    Ejm:
    sum_digits(123)  # 6 (1 + 2 + 3)
"""

def texto_invertido(numero):
    
    lista = 0
    
    for i in str(numero):
        lista = lista + int(i)
    
    return lista

numero = int(input("Ingresar un número: ")) 
print(texto_invertido(numero))