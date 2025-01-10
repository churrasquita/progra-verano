# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 12:32:28 2025

@author: LabCivil1-Pc34
"""
solicitud = input('¿Que desea analizar? Día o Noche: ').upper()
while solicitud!= 'DÍA' and solicitud!= 'NOCHE':
    solicitud = input('ERROR: ¿Que desea analizar? Día o Noche: ').upper()
if solicitud == 'DÍA':
    periodo = 'D'
else:
    periodo = 'N'

rutas = input('¿Que rutas desea comparar?: ').upper()
partesRuta = rutas.split()
while len(partesRuta) <2:
    rutas = input('ERROR: ¿Que rutas desea comparar?: ').upper()
    partesRuta = rutas.split()

analizar = input('¿Que desea analizar? Accidentes, Vehiculos, Buses: ').upper()
while analizar!= 'ACCIDENTES' and analizar!= 'VEHICULOS' and analizar!= 'BUSES':
    analizar = input('ERROR: ¿Que desea analizar? Accidentes, Vehiculos, Buses: ').upper()
    
ruta1 = partesRuta[0] + '.txt'
buses1 = 0
motos1 = 0

ruta2 = partesRuta[1] + '.txt'
buses2 = 0
motos2 = 0

arch1 = open(ruta1, encoding='utf-8')
linea = arch1.readline().strip()
while linea != '':
    linea = arch1.readline().strip()
    
arch2 = open(ruta2, encoding = 'utf-8')
linea = arch2.readline().strip()
while linea != '':
    linea = arch2.readline().strip()