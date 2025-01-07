# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 09:30:10 2025

@author: LabCivil1-Pc34
"""
print('Bienvenido al simulador')
s = float(input('Distancia (S): '))
t = float(input('Tiempo situar (T): '))
i = float(input('Tiempo reacción (I): '))    
b = float(input('Tiempo lanzar(B): '))         
v = float(input('Velocidad (V): '))
edad = int(input('Edad del arquero (años): '))
estatura = float(input('Estatura del arquero (metros): '))
nivel = int(input('Nivel del arquero (1 a 100): '))

print('Calculando...')

mayor_diferencia = -111
mejor_opcion = 0
for c in range(1, 7):
    print(f'Resultado para área {c}')
    y = 0.6
    if c== 3 or c== 4:
        x = 0 
    else: 
        x = 7.3/3
    n = (((x+y+s)/2)*((t+i+2*b)/4))+(v/2)-1 
    r = (edad+(nivel*c/estatura))/2
    diferencia = n - r
    if diferencia > mayor_diferencia: # donde la diferencia sea mayor (positiva)
        mayor_diferencia = diferencia
        mejor_opcion = c
        
    print(f'    potencia: {n}')
    print(f'    arquero: {r}')
    print(f'    diferencia: {diferencia}')
    if r >= n:
        print('Penal atajado')
    else:
        print('GOL')

print('Resultado final:')
print(f'La mejor opción es tirar al area {mejor_opcion}')
    