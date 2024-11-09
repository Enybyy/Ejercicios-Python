# p = "hola mundo"
# print(dir(p))

# lista = [1,1,1,4,4,5,5,5,3]
# l = lista
# print(lista.count(l))

# lista = []
# print(lista)

# n = 2000

# def numeros_primos(numero):
    
#     lista=[]
    
#     for n1 in range(1,numero+1,2):
#         lista2=[]
#         for n2 in range(1,n1+1,2):
#             if n2 != n1 and n2 != 1:
#                 if n1 % n2 != 0:
#                     lista2.append(True)
#                 else:
#                     lista2.append(False)
#             elif n1 == 1 or n1 == 3:
#                 lista.append(n1)
#             elif n2 == n1:
#                 if all(lista2):
#                     lista.append(n1)
                
#     return lista
            
# print(numeros_primos(n))

# n = "123"

# a = n.split("")

# print(a)

tupla = [(1, 2), (3, 1), (5, 0)]

print(sorted(tupla, reverse=True))