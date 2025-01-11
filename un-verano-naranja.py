# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 12:32:28 2025

@author: LabCivil1-Pc34
"""
print('a)')
solicitud = input('¿Que desea analizar? Día o Noche: ').upper()
while solicitud!= 'DÍA' and solicitud!= 'NOCHE':
    solicitud = input('ERROR: ¿Que desea analizar? Día o Noche: ').upper()
if solicitud == 'DÍA':
    periodo = 'D'
else:
    periodo = 'N'

rutas = input('¿Que rutas desea comparar?: ')
partesRuta = rutas.split()
while len(partesRuta) <2:
    rutas = input('ERROR: ¿Que rutas desea comparar?: ')
    partesRuta = rutas.split()

analizar = input('¿Que desea analizar? Accidentes, Vehiculos, Buses: ').upper()
while analizar!= 'ACCIDENTES' and analizar!= 'VEHICULOS' and analizar!= 'BUSES':
    analizar = input('ERROR: ¿Que desea analizar? Accidentes, Vehiculos, Buses: ').upper()
    
ruta1 = partesRuta[0] + '.txt'

ruta2 = partesRuta[1] + '.txt'

buses1 = 0
vehiculos1 = 0
accidentes1 = 0
arch1 = open(ruta1, encoding='utf-8')
linea = arch1.readline().strip()
while linea != '':
    partes = linea.split('-')
    if partes[0] == periodo:
        accidentes1 += int(partes[3])
        vehiculos1 += int(partes[2])
        if partes[1] == 'Buses':
            buses1 += int(partes[2])
        
    linea = arch1.readline().strip()

buses2 = 0
vehiculos2 = 0
accidentes2 = 0
arch2 = open(ruta2, encoding = 'utf-8')
linea = arch2.readline().strip()
while linea != '':
    partes = linea.split('-')
    if partes[0] == periodo:
        accidentes2 += int(partes[3])
        vehiculos2 += int(partes[2])
        if partes[1] == 'Buses':
            buses2 += int(partes[2])
        
    linea = arch2.readline().strip()

if analizar == 'ACCIDENTES':
    if accidentes1>accidentes2:
        diferencia = accidentes1-accidentes2
        print(f'En la {ruta1} se produjieron {diferencia} accidentes más que en la {ruta2}')
    else:
        diferencia = accidentes2-accidentes1
        print(f'En la {ruta2} se produjieron {diferencia} accidentes más que en la {ruta1}')
elif analizar == 'VEHICULOS':
    if vehiculos1 > vehiculos2:
        diferencia = vehiculos1-vehiculos2
        print(f'En la {ruta1} transitaron {diferencia} vehículos más que en la {ruta2}')
    elif vehiculos2 > vehiculos1:
        diferencia = vehiculos2-vehiculos1
        print(f'En la {ruta2} transitaron {diferencia} vehículos más que en la {ruta1}')
    else:
        print(f'En la {ruta1} y {ruta2} transitaron la misma cantidad de vehículos')
else:
    print(f'En la {ruta1} transitaron {buses1} buses')
    print(f'En la {ruta2} transitaron {buses2} buses')
    
print('b)')

mayorFactor = -1111
nombreMayorFactor = ''
for i in range(1,5):
    arch = open(f'Ruta0{i}.txt', 'r', encoding= 'utf-8')
    linea = arch.readline().strip()
    autos = 0
    camionetas = 0
    motos = 0
    buses = 0 
    camiones = 0
    while linea != '':
        partes = linea.split('-')
        if partes[0] == periodo:
            if partes[1] == 'Autos':
                autos += int(partes[3])
            if partes[1] == 'Camionetas':
                camionetas += int(partes[3])
            if partes[1] == 'Motos':
                motos += int(partes[3])
            if partes[1] == 'Buses':
                buses += int(partes[3])
            if partes[1] == 'Camiones':
                camiones += int(partes[3])
        
        linea = arch.readline().strip()
    factorRiesgo = (autos*3) + (camionetas*2) + motos + (buses*8) + (camiones*5)
    if factorRiesgo > mayorFactor:
        mayorFactor = factorRiesgo
        nombreMayorFactor = 'Ruta0'+ str(i)
    print(f'El factor de riesgo de la Ruta 0{i} es {factorRiesgo}')
print('c)')
print(f'La ruta con el mayor factor de riesgos de accidentes es {nombreMayorFactor}')
    

        
