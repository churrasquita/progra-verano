# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 10:10:53 2025

@author: LabCivil1-Pc34
"""
def imprimir_continentes(lista1,lista2):
    for i in range(len(lista1)):
        print(lista2[i])
        print(f' {round(lista1[i],1)} M')

def intercambiar(lista,a,b):
    aux = lista[a]
    lista[a] = lista[b]
    lista[b] = aux

def intercambiarMatrices(matriz, a,b,c):
    aux = matriz[c][a]
    matriz[c][a] = matriz[c][b]
    matriz[c][b] = aux
   
    
def burbujaMayor(lista1, lista2, matriz1, matriz2):
    mayor = -11*99
    contMayor = ''
    for a in range(len(lista1)-1):
        for b in range(a+1, len(lista2)):
            if lista1[a]>lista1[b]:
                intercambiar(lista1,a,b)
                intercambiar(lista2,a,b)
                mayor = lista1[b]
                contMayor = lista2[b]
                
                for c in range(5): # cambiamos los valores de las matrices
                    intercambiarMatrices(matriz1, a,b,c)
                for k in range(1):
                    intercambiarMatrices(matriz2, a,b,k)
                    
    imprimir_continentes(lista1,lista2)
    return mayor, contMayor
    
def buscar_agregar(e,li):
    if e not in li:
        li.append(e)
    return li.index(e)

import numpy as np

arch = open('tesoros.txt', 'r', encoding= 'utf-8')
linea = arch.readline().strip()

mxColeccion = np.zeros([5,20])
mxCont = np.zeros([1,20])
mxReli = np.zeros([5,1])
rarezas = []
continentes = []
while linea != '':
    partes = linea.split(',')
    if len(partes) == 4:
        rareza = partes[1]
        continente = partes[2]
        valor = float(partes[3])
        
        f = buscar_agregar(rareza, rarezas)
        c = buscar_agregar(continente, continentes)
        
        mxColeccion[f][c] += valor
        mxCont[0,c] += 1
        mxReli[f,0] += 1
    linea = arch.readline().strip()
    
sumasCont = []
for col in range(len(continentes)):
    suma = 0
    for fila in range(len(rarezas)):
        suma += mxColeccion[fila][col]
    sumasCont.append(suma)

print('1) Valor por continente')
mayor, contMayor = burbujaMayor(sumasCont, continentes, mxColeccion, mxCont)

print('2) Valor por rareza del continente con mayor valor')
for col in range(len(continentes)):
    if continentes[col] == contMayor:
        suma = 0
        for fila in range(len(rarezas)):
            print(f' {rarezas[fila]}: {round(mxColeccion[fila][col],1)} M')

menor = 9999*9
rarezaMenor = ''
for fila in range(len(rarezas)):
    suma = 0
    for col in range(len(continentes)):
        suma += mxColeccion[fila][col]
    if suma <menor:
        menor= suma
        rarezaMenor = rarezas[fila]

print('3) Colección con menor valor')
print(f'{rarezaMenor} {round(menor,1)}')

print('4) Valor medio de la colección reliquia')

total = 0
suma = 0
for fila in range(len(rarezas)):
    total = 0
    suma = 0
    if rarezas[fila] == 'reliquia':
        for col in range(len(continentes)):
            suma += mxColeccion[fila][col]
            total = mxReli[fila][0]
        promedio = suma/total
print(f'{round(promedio,2)}M')

for i in range(len(continentes)):
    print(f'{continentes[i]}: {round(mxCont[0,i])}')


