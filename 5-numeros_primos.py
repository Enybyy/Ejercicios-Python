"""
Escribe una función que reciba un número n y devuelva una lista con todos los números primos menores o iguales a n.
Ejm:
primes_up_to_n(10)  # [2, 3, 5, 7]
"""

def numeros_primos(numero):
    
    lista=[]
    
    for n1 in range(1,numero+1,2):
        lista2=[]
        for n2 in range(1,n1+1,2):
            if n2 != n1 and n2 != 1:
                if n1 % n2 != 0:
                    lista2.append(True)
                else:
                    lista2.append(False)
            elif n1 == 1:
                lista.append(n1)
            elif n2 == n1:
                if all(lista2):
                    lista.append(n1)
                
    return lista
        
numero = int(input("Ingresar un número: "))
print(numeros_primos(numero))
