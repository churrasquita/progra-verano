# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 11:34:42 2025

@author: LabCivil1-Pc34
"""
determinar_bisiesto = int(input('Ingrese año para determinar si es o no bisiesto:'))
if determinar_bisiesto%4 == 0 and determinar_bisiesto%100 != 0:
    print(f'El año {determinar_bisiesto} es bisiesto')
elif determinar_bisiesto%400 == 0:
    print(f'El año {determinar_bisiesto} es bisiesto')
else:
    print(f'El año {determinar_bisiesto} no es bisiesto')
    