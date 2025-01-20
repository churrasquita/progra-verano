# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 11:23:11 2025

@author: LabCivil1-Pc34
"""
def buscar_agregar(e,li):
    if e not in li:
        li.append(e)
    return li.index(e)

import numpy as np
rentas = np.zeros([10,7])

arch = open('rentas.txt', 'r', encoding = 'utf-8')
linea = arch.readline().strip()

marcas = []
dias = []
ingresoTotal = 0
cantDias= 0
while linea != '':
    partes = linea.split(',')
    marca = partes[0]
    tipo = partes[1]
    f = buscar_agregar(marca, marcas)
    
    for i in range(2,len(partes)):
        dia = partes[i]
        c = buscar_agregar(dia, dias)
        cantDias += 1
        if tipo == 'Standard':
            precio = 44000
        else:
            precio = (44000*1.4)
        ingresoTotal += precio   
        
        rentas[f,c] += precio*1.19 # vamos guardando el precio con iva
    linea = arch.readline().strip()
    
print(f'1) Ingreso total sin IVA: {ingresoTotal}')


mayor = -1 
diaMayor = ''
for col in range(len(dias)):
    sumador = 0
    for fil in range(len(marcas)):
        sumador += rentas[fil][col]
    if sumador > mayor:
        mayor = sumador
        diaMayor = dias[col] 
print(f'2) El días que generó más ingresos fue el {diaMayor} con $ {mayor}')

print('3) Ingresos por marca')
for fila in range(len(marcas)):
    sumadorMarcas = 0
    for col in range(len(dias)):
        sumadorMarcas += rentas[fila][col]
    print(f' - {marcas[fila]} {sumadorMarcas}')
