#             ---Año bisiesto---
año = int(input("Ingresa un año: "))


if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
    print(f'\nEl año {año} es bisiesto.')
    
else:
    print(f'\nEl año {año} no es bisiesto.')