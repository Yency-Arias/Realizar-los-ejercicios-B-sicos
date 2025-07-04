#             ---Vocal o consonante?---
letra = input('Ingresa una letra: ').lower()


if len(letra) == 1 and letra.isalpha():

    if letra in 'aeiou':
        print(f'\nLa letra {letra} es una vocal.')
        
    else:
        print(f'\nLa letra {letra} es una consonante.')
    
else:
    print('\nPor favor, ingresa solo una letra valida.')