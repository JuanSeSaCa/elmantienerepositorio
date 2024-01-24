#area triangulo equilatero, mostrar ingrese 
import os
os.system('cls')

lado =0
baseDato= float(input('digite el lado del triangulo equilatero '))

area = (0.4330127018922193) * baseDato**2
if area > 1000:
    print ('Datos no validos')
else:
    print(f'el area del triangulo es {area} unidades 2')
os.system('pause')
