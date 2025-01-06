# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 12:43:58 2025

@author: LabCivil1-Pc34
"""

monto = int(input('Ingresa la cantidad de dinero en pesos chilenos (debe ser mayor a $15.000 clp):  '))
moneda = input('A qué moneda quieres convertirlo? (dólares o euros)').lower()

comision = 0
if monto >= 15000 and comision<= 100000:
    comision = comision* 0.05
elif monto > 100000:
    comision = comision * 0.035

if moneda == 'dolar': 
    monto = monto/ 1008
elif moneda =='euro':
    monto = monto/900

print(f'la comision fue de {comision} y el monto convertido fue de {monto} en {moneda}')