"""
    Ejercicio: Dada una lista de tuplas, escribe una función que las ordene según el segundo valor de cada tupla.
    sort_by_second_value([(1, 2), (3, 1), (5, 0)])  # [(5, 0), (3, 1), (1, 2)]
"""

# 
def ordenar_por_segundo_valor(tupla):

    return sorted(tupla, reverse=True)

tupla = [(1, 2), (3, 1), (5, 0)]
print(ordenar_por_segundo_valor(tupla))


def ordenar_por_segundo_valor(tupla):

    return sorted(tupla, reverse=True)

tupla = [(1, 2), (3, 1), (5, 0)]
print(ordenar_por_segundo_valor(tupla))