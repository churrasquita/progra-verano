# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 23:11:55 2025

@author: catal
"""

arch = open('datos.txt', 'r', encoding = 'utf-8')
linea = arch.readline().strip()

masCalidaGlobal = -11
nombreCalidaGlobal = 0
ciudadCalidaGlobal = ''
regionCalidaGlobal = ''

masFria = 99999
nombreMasFria = ''

contador = 0

while linea != '':
    partes = linea.split(',')
    region = partes[0]
    cantCiudades = int(partes[1])
    
    sumaCiudades = 0
    acumuladorZonas = 0
    for i in range (cantCiudades):
        linea = arch.readline().strip()
        partesCiudad = linea.split(',')
        ciudad = partesCiudad[0]
        cantTermometros = int(partesCiudad[1])
        
        sumaTermometros = 0
        promedio = 0
        for j in range(cantTermometros):
            sumaTermometros += float(partesCiudad[2+(j)])
            if float(partesCiudad[2+j]) > masCalidaGlobal:
                masCalidaGlobal = float(partesCiudad[2+j])
                nombreCalidaGlobal = 1+j
                ciudadCalidaGlobal = ciudad
                regionCalidaGlobal = region
            if  float(partesCiudad[2+j]) < -1:
                contador += 1
       
        promTermometro = sumaTermometros/cantTermometros 
        sumaCiudades += sumaTermometros # para sumar los termometros de cada zona de la ciudad
        acumuladorZonas += cantTermometros
        

        arch2 = open('intervalos.txt', 'r', encoding = 'utf-8')
        linea2 = arch2.readline().strip()
        while linea2 != '':
            partes2 = linea2.split(',')
            intCiudad = partes2[0]
            tempMin = float(partes2[1])
            tempMax = float(partes2[2])
            if ciudad == intCiudad:
                if (promTermometro>=tempMin) and (promTermometro<=tempMax):
                    print(f'El estado de la ciudad {ciudad} es NORMAL')
                elif promTermometro<tempMin:
                    print(f'El estado de la ciudad {ciudad} es FRÍA')
                else:
                    print(f'El estado de la ciudad {ciudad} es CÁLIDA')
                    
            linea2 = arch2.readline().strip()
            
        promRegion = sumaCiudades/acumuladorZonas
        if promRegion < masFria:
            masFria = promRegion
            nombreMasFria = region
   
        
    linea = arch.readline().strip()
print(f'La zona más cálida es la N° {nombreCalidaGlobal}, {ciudadCalidaGlobal}, {regionCalidaGlobal} con {masCalidaGlobal}°')
print(f'La región más fría es {nombreMasFria} con {masFria}')

print(f'La cantidad de sensores fríos: {contador}')