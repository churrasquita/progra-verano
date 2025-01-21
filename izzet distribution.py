# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 22:17:22 2025

@author: catal
"""

import numpy as np

bodega = np.zeros([6,6]) # guardamos la cantidad de items
despachos = np.zeros([6,6]) # guardamos cont de despachos

#listas paralelas
zonas = ['A','B','C','D','E','F']
sectores = [1,2,3,4,5,6]
costos = [125,325,198,635,312,185]

#abrimos el arch
arch = open('recibidos.txt', 'r', encoding = 'utf-8')
linea = arch.readline().strip()
while linea!= '':
    partes = linea.split(';')
    fecha = partes[0]
    combinacion = partes[1].split('-')
    zona = combinacion[0]
    sector = int(combinacion[1])
    cantidadItem = int(partes[2])
    
    f = zonas.index(zona)
    c = sectores.index(sector)
    
    bodega[f][c] += cantidadItem
    
    if bodega[f][c] > 100:
        print(f'Se realiza un despacho en {zona} {sector} el {fecha}')
        bodega[f][c] -= 100
        despachos[f][c] += 1
    
    linea = arch.readline().strip()
    
print('2) Los envíos por zona-sector en el mes fueron: ')
print(despachos)

cont = 0
costoTotal = 0
for col in range(len(sectores)):
    for fila in range(len(zonas)):
        cont += despachos[fila][col]
        costoTotal += (costos[col]*(despachos[fila][col])) 
        # multiplicamos el despacho por el costo de su lista paralela
print(f'3) El costo total de los {cont} despachos es {costoTotal}')

# 5) como puede existir más de uno, hago una lista de mayores

mayores = []
mayor = -1111*99
nombreMayor = ''
for fila in range(len(zonas)):
    for col in range(len(sectores)):
        if bodega[fila][col] > mayor:
            mayor = bodega[fila][col]
            nombreMayor = f'{zonas[fila]} - {sectores[col]}'
           
mayores.append(nombreMayor)
for fila in range(len(zonas)):
    for col in range(len(sectores)):
        if bodega[fila][col] == mayor:
            mayorUbicacion = f'{zonas[fila]} - {sectores[col]}'

if mayorUbicacion not in mayores:
    mayores.append(mayorUbicacion)
            
print('4)Las ubicaciones con la mayor cantidad de items pendientes son: ')
for i in range(len(mayores)):
    print(f'{mayores[i]} con {mayor}')

print('5) El total de items pendientes por zonas:')

pendientesZonas = []
for fila in range(len(zonas)):
    cont = 0
    for col in range(len(sectores)):
        cont += bodega[fila][col]
    pendientesZonas.append(cont)
    
for a in range(len(zonas)-1):
    for b in range(a+1, len(pendientesZonas)):
        if pendientesZonas[a] < pendientesZonas[b]:
            aux = pendientesZonas[a]
            pendientesZonas[a] = pendientesZonas[b]
            pendientesZonas[b] = aux
            aux2 = zonas[a]
            zonas[a] = zonas[b]
            zonas[b] = aux2

for i in range(len(zonas)):
    print(f'Zonas {zonas[i]} - {pendientesZonas[i]}')
           


            

