#           ---Intercambio de variables---
A = int(input('Ingresa el valor de A: '))
B = int(input('Ingresa el valor de B: '))


print(f'\nAntes del intercambio:\n\nA = {A}\nB = {B}\n\n------------------------')


A, B = B, A


print(f'Despues del intercambio:\n\nA = {A}\nB = {B}\n')