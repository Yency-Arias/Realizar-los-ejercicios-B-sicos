#                ---Contando palabras---
frase = input('Ingresa una frase: ')

palabras = frase.split()


cantidad_de_palabras = len(palabras)


if cantidad_de_palabras == 1:
    
    print(f'\nLa frase contiene {cantidad_de_palabras} palabra')

else:
    
    print(f'\nLa frase contiene {cantidad_de_palabras} palabras')