# Escribe una función que reciba una lista de números y devuelva el valor más grande. Si la lista está vacía, debe devolver None.
# max_value([1, 2, 3, 4, 5])  # 5
# max_value([])  # None

def valor_mayor(lista):
    
    if not lista:
        return None
    
    numero = None
    
    for i in lista:
        if numero is None or i > numero:
            numero = i
        
    return numero

lista = []

while True:
    dato = input("Ingresar datos a la lista, cuando termine de agregar datos a la lista escriba 'salir': ")
    if dato.lower() == "salir":
        break
    lista.append(int(dato))
    
print(valor_mayor(lista))