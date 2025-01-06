# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 12:01:37 2025

@author: LabCivil1-Pc34
"""
nombre = input('Ingresa tu nombre de usuario!: ')
hora = float(input('ingresa la hora del día para saludarte! (sistema 24 hrs):'))
if hora >= 6 and hora <12: 
    print(f'Buenos días {nombre}!')
elif hora >= 12 and hora <=20:
    print(f'Buenas tardes {nombre}!')
else: 
    print(f'Buenas noches {nombre}!')