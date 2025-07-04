#               ---Valor del area de un circulo---
import math

radio = float(input('Introduce el radio del circulo: '))


area = math.pi * (radio ** 2)


print(f'El área del círculo con radio {radio} es: {area:.2f}')