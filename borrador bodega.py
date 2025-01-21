# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 10:02:17 2025

@author: LabCivil1-Pc34
"""
def mover(mx):
    for col in range(5):
        for fila in range(5):
            aux = mxbodega[fila][col] 
            mxbodega[fila][col] = mxbodega[fila+1][col]
            mxbodega[fila+1][col] = aux
                                
    

import numpy as np

arch = open('bodega.txt', encoding= 'utf-8')
linea = arch.readline().strip()
partesCat = linea.split(',')

categorias = []
for i in range(len(partesCat)):
    categorias.append(partesCat[i])
mxbodega = np.zeros([6,5])

filas = [1,2,3,4,5,6]
contDias = 0
f = 0
contProductos = 0
print('1) Envíos')
while linea != '':
    contDias += 1
    linea = arch.readline().strip()
    partes = linea.split(',')
    if linea != 'MOVER':
        for c in range(5):
            mxbodega[0][c] += int(partes[c])
            contProductos += int(partes[c])
            linea = arch.readline().strip()
    else:
        mover(mxbodega)
    for c in range(5):
        if mxbodega[5][c]>100:
            print(f'Día {contDias}')
            print(f'cargamento de {categorias[c]} enviado')
        
    
    linea = arch.readline().strip()
print(f'2) En {contDias} han ingresado a bodega {contProductos} productos')
