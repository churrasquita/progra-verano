# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 23:13:14 2025

@author: catal
"""
opcion = int(input('Ingrese opción (1, 2 o 3, -1 para terminar): '))
while opcion != 1 and opcion!=2 and opcion!= 3:
    opcion = int(input('Error (1, 2 o 3, -1 para terminar): '))
    

while opcion != -1:
    if opcion == 1:
        terminacionPatente = input('Ingrese terminación de patente: ')
        
        arch = open('estacionados.txt', 'r', encoding = 'utf-8')
        linea = arch.readline().strip()
        totalEstacionados = 0
        contPatente = 0
        while linea != '':
            partes = linea.split(',')
            patente = partes[0]
            horaLlegada = int(partes[1])
            minLlegada = int(partes[2])
            horaSalida = int(partes[3])
            minSalida = int(partes[3])
            
            partes2 = patente.split('-')
            if terminacionPatente == partes2[2]:
                contPatente += 1
                
            totalEstacionados += 1        
            
            linea = arch.readline().strip()
            
        if terminacionPatente== '-':
            print(f'1) Cantidad de autos estacionados: {totalEstacionados}')
        else:
            print(f'1) Cantidad de autos estacionados: {contPatente}')
    elif opcion == 2:
        arch = open('estacionados.txt', 'r', encoding = 'utf-8')
        linea = arch.readline().strip()
        
        paseLibre = 0
        total = 0
        while linea != '':
            partes = linea.split(',')
            patente = partes[0]
            horaLlegada = int(partes[1])
            minLlegada = int(partes[2])
            horaSalida = int(partes[3])
            minSalida = int(partes[3])
            
            duracion = ((horaSalida*60)+minSalida) - ((horaLlegada*60) + minLlegada)
            
            if duracion < 30:
                paseLibre += 1
            total += 1
           
            linea = arch.readline().strip()
        
        porcLibre = paseLibre/total *100
        print(f'2) Un {porcLibre} % de los vehículos tuvo pase libre')
            
    opcion = int(input('Ingrese opción (1, 2 o 3, -1 para terminar): '))
    

