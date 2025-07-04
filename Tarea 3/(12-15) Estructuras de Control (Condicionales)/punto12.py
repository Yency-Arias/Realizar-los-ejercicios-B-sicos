#            ---Numero positivo, negativo o cero---
numero = int(input('Ingresa un numero: '))


if numero > 0:
    print(f'\nEl numero {numero} es positivo.')
elif numero < 0:
    print(f'\nEl numero {numero} es negativo.')
else:
    print('\nEl numero es cero.')