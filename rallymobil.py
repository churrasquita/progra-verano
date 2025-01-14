# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 08:23:33 2025

@author: LabCivil1-Pc34
"""
def duracion_ruta(ruta):
    totalDias = 0
    for letra in str(ruta):
        if letra == 'R':
            totalDias += 1 
        elif letra == 'M':
            totalDias += 3 
        elif letra == 'L':
            totalDias += 5
    return totalDias

def obtenerMayor(mayor, nombreMayor, valor, nombre): # necesita 4 valores para comparar entre si
    if mayor < valor:
        mayor = valor
        nombreMayor = nombre
    else:
        mayor = mayor
        nombreMayor = nombreMayor
    return mayor,nombreMayor

arch = open('rutas.txt', 'r', encoding = 'utf-8')
linea = arch.readline().strip()

mayor = -111*9
nombreMayor = ''
while linea != '':
    partes = linea.split(',')
    nombre = partes[0]
    ruta = partes[1]
    duracion = duracion_ruta(ruta)
    mayor, nombreMayor = obtenerMayor(mayor, nombreMayor, duracion, nombre)
    print(f'{nombre}: {duracion} días')

    linea = arch.readline().strip()
print('-'*20)
print(f'La ruta más larga es {nombreMayor} con {mayor} días')     

