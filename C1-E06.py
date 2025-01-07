# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 22:07:59 2025

@author: catalina
"""
#obtener datos
edad = int(input('Ingrese la edad de la persona: '))
tiene_cupon = input('¿Tiene cupón?: ').lower()

#calculos 
if edad <= 3:
    valor = 0
elif edad >= 4 and edad <= 12:
    valor = 5000
elif edad >= 13 and edad <= 64:
    valor = 10000
else:
    valor = 7500

if tiene_cupon == 'si':
    valor-=2000
# else:
#    valor = valor
if valor == 0:
    print('Entra gratis!')
else:
    print(f'El precio del ticket es de ${valor}')