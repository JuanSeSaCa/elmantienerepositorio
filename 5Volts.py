#ingresar 5 voltajes, obtener su promedio.
#si su promedio es mayor a 220 = alto voltajes
# sino, voltaje correcto
import os
os.system('cls')
voltaje1=0
voltaje2=0
voltaje3=0
voltaje4=0
voltaje5=0
voltaje1=(int(input(" Ingrese el valor del voltaje 1 ")))
voltaje2=(int(input(" Ingrese el valor del voltaje 2 ")))
voltaje3=(int(input(" Ingrese el valor del voltaje 3 ")))
voltaje4=(int(input(" Ingrese el valor del voltaje 4 ")))
voltaje5=(int(input(" Ingrese el valor del voltaje 5 ")))

promedio=(voltaje1+voltaje2+voltaje3+voltaje4+voltaje5)/5
print(f'El promedio de voltaje es {promedio}')

if (promedio)/5 > 220:
    print("ALTO VOLTAJE")
else:
    print("VOLTAJE CORRECTO")
    os.system('pause')

