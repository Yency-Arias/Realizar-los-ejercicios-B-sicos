#              ---Tabla de multiplicar con while---
numero = int(input('Ingresa un numero para ver su tabla de multiplicar: '))

print(f'\nTabla de multiplicar de {numero}:')

i = 1
while i <= 10:
    print(f'{numero} x {i} = {numero * i}')
    i += 1