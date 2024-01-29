#3 voltajes distintos, si es <= 115 voltaje correcto, >115 y <220 = alto voltaje, > a 220= peligro

import os
os.system('cls')
voltaje1=0
voltaje2=0
voltaje3=0

voltaje1=(int(input(" Ingrese el valor del voltaje 1 ")))
voltaje2=(int(input(" Ingrese el valor del voltaje 2 ")))
voltaje3=(int(input(" Ingrese el valor del voltaje 3 ")))


promedio=(voltaje1+voltaje2+voltaje3)/3
print(f'El promedio de voltaje es {promedio}')

if (promedio) <115:
    print("VOLTAJE CORRECTO")
elif (promedio >= 115) and (promedio <220):
    print("ALTO VOLTAJE")
elif (promedio) >= 220:


    sfdf
    print("PELIGROO")
os.system('pause')

