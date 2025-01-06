# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 10:27:10 2025
cata
"""
figura = input('Ingresa una figura geométrica para calcular su área:').lower()

if figura == 'triángulo': 
    base = float(input('Ingresa el valor de su base: '))
    altura = float(input('Ingresa el valor de su altura: '))
    print(f'Su área es: {base*altura/2} u2')
    
elif figura == 'cubo':
    lado = float(input('Ingresa el valor de sus lados: '))
    print(f'Su área es de: {lado*6} u2')
    
elif figura == 'círculo':
    radio = float(input('Ingresa el valor de su radio: '))
    print(f'Su área es de: {(radio**2) * 3.14} u2')
else:
    print('Figura incorrecta, ingrese nuevamente!')
