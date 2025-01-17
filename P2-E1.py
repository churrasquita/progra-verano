# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 10:06:27 2025

@author: LabCivil1-Pc34
"""
import random
def ficha_aleatoria():
    return random.choice(['A', 'B', 'C', 'D', 'a', 'b', 'c', 'd'])

def intercambiar(carril, ind1, ind2):
    aux = carril[ind1]
    carril[ind1] = carril[ind2]
    carril[ind2] = aux
    
def mover(letra,direccion):
    if direccion == 'adelante':
        if letra== 'A':
            idx = carrilA.index('A')
            intercambiar(carrilA, idx, idx+1)
        elif letra == 'B':
            idx = carrilB.index('B')
            intercambiar(carrilB, idx, idx+1)
        elif letra == 'C':             
            idx = carrilC.index('C')
            intercambiar(carrilC, idx, idx+1)
        elif letra == 'D':
            idx = carrilD.index('D')
            intercambiar(carrilD, idx, idx+1)
    elif direccion == 'atras':
        if letra== 'a' and carrilA[0] == '':
            idx = carrilA.index('A')
            intercambiar(carrilA, idx, idx-1)
        elif letra == 'b' and carrilB[0] == '':
            idx = carrilB.index('B')
            intercambiar(carrilB, idx, idx-1)
        elif letra == 'c' and carrilC[0] == '':
            idx = carrilC.index('C')
            intercambiar(carrilB, idx, idx-1)
        elif letra == 'd' and carrilD[0] == '':
            idx = carrilD.index('D')
            intercambiar(carrilD, idx, idx-1)
    
    
def ganador():
    if carrilA[-1] == 'A' or carrilB[-1] == 'B' or carrilC[-1] == 'C' or carrilD[-1] == 'D':
        return False
    else:
        return True 
    

longitud = int(input('Ingrese la longitud del tablero: '))
simulaciones = int(input('Cantidad de simulaciones: '))

carrilA = ['A']
carrilB = ['B']
carrilC = ['C']
carrilD = ['D']

for i in range(longitud):
    carrilA.append('')
    carrilB.append('')
    carrilC.append('')
    carrilD.append('')

for s in range(1, simulaciones+1):
    print(f'Simulación: {s}')
    ganador()
    while ganador != False: 
        ficha = ficha_aleatoria()
        if ficha == 'A' or ficha == 'B' or ficha == 'C' or ficha == 'D':
            mover(ficha,'adelante')
        elif ficha == 'a' or ficha == 'b' or ficha == 'c' or ficha == 'd':
            mover(ficha,'atras')
        print(f'Ficha: {ficha}')
        print(f'A: {carrilA}')
        print(f'B: {carrilB}')
        print(f'C: {carrilC}')
        print(f'D: {carrilD}')
        ganador()
    
    
