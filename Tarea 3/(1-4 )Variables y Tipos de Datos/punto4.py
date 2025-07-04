#               ---Suma, resta, multplicacion y division de dos numeros---
num1 = float(input('Introduce el primer numero: '))
num2 = float(input('Introduce el segundo numero: '))


suma = num1 + num2
resta = num1 - num2
multi = num1 * num2

if num2 != 0:
    div = num1 / num2 
    print(f'\nSuma: {suma}\nResta: {resta}\nMultiplicación: {multi}\nDivisión: {div:.2f}')

else:
    print(f'\nSuma: {suma}\nResta: {resta}\nMultiplicación: {multi}\nDivisión: No se puede dividir entre cero.')