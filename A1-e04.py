# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 12:43:58 2025

@author: LabCivil1-Pc34
"""

monto = float(input('Ingresa la cantidad de dinero en pesos chilenos:  '))
moneda = input('A qué moneda quieres convertirlo? (dólares o euros) ').lower()

# primero realizamos la comisión para que no se vea afectado el monto 
comision = 0
if monto >= 15000 and monto<= 100000:
    comision = monto* 0.05
elif monto > 100000:
    comision = monto* 0.035

# ahora lo convertimos
if moneda == 'dólar': 
    monto = monto/ 1011 #debemos dividir para convertirlo
elif moneda =='euro':
    monto = monto/900

print(f'la comision fue de ${comision} clp y el monto convertido fue de {monto} en {moneda}')
