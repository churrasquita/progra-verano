# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 20:47:54 2025

@author: catal
"""
def maximos(mtx,lista):
    mayor = -1111*99
    for fila in range(len(tiendas)):
        for col in range(len(sectores)):
            if mtx[fila][col]>mayor:
                lista.clear()
                mayor = mtx[fila][col]
                lista.append(tiendas[fila])
            elif mayor == mtx[fila][col]:
                lista.append(tiendas[fila])
    return mayor

def agregar(e,li):
    if e not in li:
        li.append(e)
        

import numpy as np
arch = open('ventas.txt', 'r', encoding = 'utf-8')
linea = arch.readline().strip()

mxEdad = np.zeros([2,3])
sexos = ['Hombres', 'Mujeres']

sectores = []
tiendas = []
while linea != '':
    partes = linea.split('-')
    rut = partes[0]
    sexo = partes[1]
    edad = int(partes[2])
    sector = partes[3]
    tienda = partes[4]
    if sexo == 'M':
        f = 0
     
    elif sexo == 'F':
        f = 1
    if edad >= 18 and edad <=30:
        c = 0
    elif edad >= 31 and edad <= 50:
        c = 1
    else:
        c = 2
    mxEdad[f,c] += 1
    agregar(sector, sectores)
    agregar(tienda, tiendas)
    
    linea = arch.readline().strip()
    
print('1)')
for fila in range(len(sexos)):
    # se reinician cuando cambio de fila
    sumas1 = []
    total = 0
    sumador = 0
    for col in range(3):
        sumador = mxEdad[fila][col]
        total += sumador
        sumas1.append(sumador)
    print(sexos[fila])
    print(f'    entre 18 y 30 años {sumas1[0]/total*100} %')
    print(f'    entre 31 y 50 años {sumas1[1]/total*100} %')
    print(f'    51 años y más {sumas1[2]/total*100} %')

print('2)')

mxTiendas = np.zeros([(len(tiendas)), len(sectores)])
mxVentas = np.zeros([(len(tiendas)), len(sectores)])
arch = open('ventas.txt', 'r', encoding = 'utf-8')
linea = arch.readline().strip()

while linea != '':
    partes = linea.split('-')
    
    sector = partes[3]
    tienda = partes[4]
    monto = int(partes[5])
    f = tiendas.index(tienda)
    c = sectores.index(sector)
    mxTiendas[f][c] += monto
    mxVentas[f][c] += 1
    
    linea = arch.readline().strip()
    
lista = []
mayor = maximos(mxTiendas,lista)
print(f'Con $ {mayor} la Tienda comercial es:')
for i in range(len(lista)):
    print(lista[i])

print('Los sectores donde realizarón 9 ventas o más son:')

# buscamos el nombre de la tienda y sus valores en la matric
for i in lista:
    for fila in range(len(tiendas)):
        for col in range(len(sectores)):
            if i == tiendas[fila]:
                if mxVentas[fila][col] >= 9:
                    print(sectores[col])
    
print('3)')

for fila in range(len(tiendas)):
    print(tiendas[fila])
    suma = 0
    sumas = []
    total = 0
    for col in range(len(sectores)):
        suma =mxTiendas[fila][col]
        print(f'{sectores[col]} $ {suma/(len(sectores))}')
