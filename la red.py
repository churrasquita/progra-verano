# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 16:53:55 2025

@author: catal
"""

def agregar(e,li):
    if e not in li:
        li.append(e)
    
arch = open('usuarios.txt', 'r', encoding = 'utf-8')
linea = arch.readline().strip()

generos = []
dominios = []
while linea != '':
    partes = linea.split(',')
    email = partes[2].split('@')
    dominio = email[1]
    genero = partes[3]
    ip = partes[4].split('.')
    region = int(ip[0])
    
    agregar(dominio,dominios)
    generos.append(genero)
    
    linea = arch.readline().strip()

import numpy as np

red = np.zeros([3, (len(dominios))])

arch = open('usuarios.txt', 'r', encoding = 'utf-8')
linea = arch.readline().strip()
regionesUnicas = ['Región uno', 'Región dos', 'Región tres']

contFemale =0
contMale = 0
while linea != '':
    partes = linea.split(',')
    email = partes[2].split('@')
    dominio = email[1]
    genero = partes[3]
    ip = partes[4].split('.')
    region = int(ip[0])
    
    if region>=200:
        f = 0
    elif region>=100 and region <= 199:
        f = 1
        if genero == 'Male':
            contMale += 1
    else:
        f = 2
    c = dominios.index(dominio)
    
    if region >= 200 and genero == 'Female':
        contFemale += 1
    
    red[f][c] +=1
    linea = arch.readline().strip()
    
mayor = -111
mayorDom = ''    
contDom= []
for col in range(len(dominios)):
    sumador = 0
    for fila in range(3):
        sumador += red[fila][col]
    if sumador>mayor:
        mayor = sumador 
        mayorDom = dominios[col]
    contDom.append(sumador)
print('1) Dominio más utilizado globalmente:')
print(mayorDom)

total = 0
sumas = []
for fila in range(3):
    sumaFila = 0
    for col in range(len(dominios)):
        if dominios[col] == mayorDom:
            total += red[fila][col] # le sumo la cantidad de usos del dominio
            sumaFila += red[fila][col]
    sumas.append(sumaFila)
for i in range(3):
    print(f'{regionesUnicas[i]}: {round(sumas[i]/total*100,2)} %')

# contFemale = 0
# for col in range(len(dominios)):
#     if red[0][col] != 0 and generos[col] == 'Female':
#         contFemale += 1
    
print(f'2) Dominios usados solo por el género Female en Región uno: {contFemale}')
print(f'3) Dominios usados solo por el género Male en Región dos: {contMale}')

suma = 0
for col in range(len(dominios)):
    if red[2][col] == 0:
        suma += 1
print(f'4) Dominios no usados en Región tres: {suma}')
