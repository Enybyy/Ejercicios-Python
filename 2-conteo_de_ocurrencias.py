# Dada una lista de números, escribe una función que devuelva un diccionario con el conteo de cada número en la lista.
# Ejm: count_occurrences([1, 2, 2, 3, 3, 3, 4])  # {1: 1, 2: 2, 3: 3, 4: 1}

def conteo_ocurrencias(lista):
    
    dic = {}
    
    for i in lista:
        l =  lista.count(i)
        dic[i] = l
        
    return dic
    
lista = [1,1,1,4,4,5,5,5,3]
print(conteo_ocurrencias(lista))