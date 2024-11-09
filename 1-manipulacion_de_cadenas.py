# Escribe una función que reciba una cadena de texto y devuelva la misma cadena, pero con las palabras invertidas (sin alterar el orden de las palabras)..
# Ejm: reverse_words("Hola Mundo")  => "Mundo Hola"

def texto_invertido(texto):
    
    lista_texto = texto.split()
    
    palabra_invertida = ""
    for i in lista_texto:
        palabra_invertida = i + " " + palabra_invertida
    return palabra_invertida

texto = texto_invertido(input(str("Ingresar texto: ")))
print(texto)