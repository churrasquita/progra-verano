# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 08:27:30 2025

@author: LabCivil1-Pc34
"""

def maximos_matriz(matriz, mayoresMarcas):
    maximo = -10** 10
    for col in range(len(marcas)):
 
        maximo = -10** 10
        for fila in range(len(colores)):
            if maximo<matriz[fila][col]:
                mayoresMarcas.clear()
                maximo = matriz[fila][col]
                mayoresMarcas.append(marcas[col])
            elif maximo == matriz[fila][col]:
                mayoresMarcas.append(marcas[col])
    return maximo
                
    
def buscar_agregar(e,lista):
    if e not in lista:
        lista.append(e)
    return lista.index(e)
        
import numpy as np
mxColores = np.zeros([20,60])

colores = []
marcas = []

mxAños= np.zeros([100, 60])
marcas2 = []
años = []

for i in range(1,26):
    arch = open(f'padron{i}.txt', 'r', encoding = 'utf-8')
    linea = arch.readline().strip()
    while linea != '':
        partes = linea.split(',')
        vin = (partes[0])
        marca = partes[1]
        color = partes[2]
        año = int(partes[3])
        
        f = buscar_agregar(color,colores)
        c= buscar_agregar(marca,marcas)
        
        mxColores[f][c] += 1
        
        f = buscar_agregar(año, años)
        c = buscar_agregar(marca, marcas2)
        mxAños[f][c] += 1
        
        linea = arch.readline().strip()

print('a)')
for fila in range(len(colores)):
    suma = 0
    mayor = -11*99
    # recorro dos veces para hayar el valor y para encontrar aquellas marcas que lo comparten
    for col in range(len(marcas)):
        suma += mxColores[fila][col]
        if mxColores[fila][col]>mayor:
            mayor = mxColores[fila][col]
    print(f'{colores[fila]} ({int(suma)}) max: {int(mayor)}')
    for col in range(len(marcas)):
        if mxColores[fila][col]==mayor: # si tienen el mismo valor
            print(f' {marcas[col]}')
 
print('b)')
# recorremos según las marcas ya que queremos buscar el año (fila)
# más reciente según marca
for col in range(len(marcas2)):
    masReciente = -111
    for fila in range(len(años)):
        if años[fila] > masReciente and mxAños[fila][col] != 0: # encontramos el más reciente 
            masReciente = años[fila]
    for fila in range(len(años)): # buscamos nuevamente el valor que coincida con el más reciente
        if mxAños[fila][col] != 0 and años[fila] == masReciente:
            print(f'{marcas[col]} - {años[fila]} - {int(mxAños[fila][col])}')
            
    

    
        