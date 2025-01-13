# -*- coding: utf-8 -*-
"""
Created on Sun Jan 12 22:43:47 2025

@author: catal
"""
arch = open('archivos.txt', 'r', encoding = 'utf-8')
linea = arch.readline().strip()

corruptos = 0
contArch = 0
totalVideo = 0
system = 0
contSystem = 0

while linea != '':
    partes = linea.split(';')
    nombreArch = partes[0]
    tamano = int(partes[1])
    fechaCreacion = partes[2]
    fechaModificacion = partes[3]
    atributo = partes[4]
    
    partesArch = nombreArch.split('.')
    partes2 = fechaCreacion.split('/')
    partes3 = fechaModificacion.split('/')
    
    if (int(partes2[2])) < (int(partes3[2])) or (int(partes2[2])) == (int(partes3[2])):
        if partesArch[1] == 'avi' or partesArch[1] == 'mov' or partesArch[1] == 'mpeg':
            tamanoVideo = tamano/1000
            totalVideo += tamanoVideo
        if atributo == 'system':
            system += tamano
            contSystem += 1
        
    elif (int(partes2[2])) > (int(partes3[2])):
        corruptos += 1
        
        
    contArch += 1
    
    linea = arch.readline().strip()

porcCorruptos = corruptos/contArch*100
promSystem = system/contSystem # me piden calcular el tamaño promedio SOLO de esos arch
print(f' 1) Porcentaje de archivos corruptos: {round(porcCorruptos,2)}%')
print(f' 2) Tamaño utilizado por archivos de video: {round(totalVideo,2)} MB')
print(f' 3) Tamaño promedio de archivos del sistema: {round(promSystem,2)} KB')