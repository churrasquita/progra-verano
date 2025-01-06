# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 11:50:25 2025

@author: LabCivil1-Pc34
"""
print('Calculemos si tus notas son aprobatorias!')
nota_1 = float(input('Ingresa la nota 1: '))
resiliencia = (input('Rendiste resiliencia?:')).lower()
if resiliencia == 'si':
    nota_resiliencia = float(input('Ingresa la nota de resiliencia:'))
    if nota_1 < 4 and nota_resiliencia >= 4:
        nota_1 = 4
    elif nota_1 >= 4:
        nota_1 = (nota_1+nota_resiliencia)/2
    else:
        nota_1 = nota_1

if nota_1 >=4:
    print(f'Tu nota {nota_1} es aprobatoria!')
    if nota_1%2 == 0:
        print('La nota ingresada es par')
    else:
        print('La nota ingresada no es par')
else:
    print(f'Tu nota {nota_1} no es aprobatoria')
    if nota_1%2 == 0:
        print('La nota ingresada es par')
    else:
        print('La nota ingresada no es par')
    
nota_2 = float(input('Ingresa la nota 2: '))
if nota_2 >=4:
    print(f'Tu nota {nota_1} es aprobatoria!')
    if nota_2%2 == 0:
        print('La nota ingresada es par')
    else:
        print('La nota ingresada no es par')
else:
    print(f'Tu nota {nota_1} no es aprobatoria')
    if nota_2%2 == 0:
        print('La nota ingresada es par')
    else:
        print('La nota ingresada no es par')
    
