# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 10:00:37 2025

@author: LabCivil1-Pc34
"""
x = float(input("Ingrese el primer número: "))
y = float(input('Ingrese el segundo número: '))

# analizar si la division es entera
if (y!= 0 and x%y== 0):
    print('La división es entera!')
elif y!=0 and x%y != 0:
    print(f' el resto de la división es {x%y}')
#indeterminacion
if x==0 or y==0:
    print('Error! no se puede dividir por cero.')
    
# mostrar cuál es mayor
if x > y:
    print(f' {x} es mayor')
    if y!= 0 and x%y == 0 :
        print(f'{x} es múltiplo de {y}')
    else:
        print(f'{x} no es múltiplo de {y}')
elif y > x:
    print(f'{y} es mayor')
    if (y%x == 0):
        print(f' {y} es múltiplo de {x}')
    else:
        print(f' {y} no es múltiplo de {x}')
else:
    print(f' {x} y {y} son iguales')
