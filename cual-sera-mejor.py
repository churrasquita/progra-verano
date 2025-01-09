# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 23:33:11 2025

@author: catal
"""
arch = open('autos.txt', 'r', encoding='utf-8')
linea = arch.readline().strip()

# variables globales (ambas marcas)
menorGlobal = 99999999
nombreMenorGlobal = ''

antiguoGlobal = 9999999
nombreAntiguoGlobal = ''

cFabricacionTotal = 0 #cont para sacar promedio
sFabricacionTotal = 0 #acumulador para sacar promedio

while linea != '':
    partes = linea.split(',')
    marca = partes[0]
    cantAutos = int(partes[1])
    
    # por cada marca (variables locales)
    mayorCilindrada = -1111
    nombreMayorCilindrada = ''
    motorCilindrada = ''
    
    masEficiente = -1111
    nombreMasEficiente = ''
    
    cManual = 0
    cAutomatico = 0
    cTransmision = 0
    
    menorLocal = 9999
    nombreMenorLocal = ''
    
    masAntiguo = 99999
    nombreMasAntiguo = ''
    
    cFabricacion = 0
    sFabricacion = 0
    
    for i in range(cantAutos):
        linea = arch.readline().strip()
        partes2 = linea.split(',')
        modelo = partes2[0]
        tipoMotor = partes2[1]
        cilindrada = float(partes2[2])
        hp = int(partes2[3])
        transmision = partes2[4]
        primeraFabricacion = int(partes2[5])
        ultimaFabricacion = partes2[6] # no se debe colocar int ya que puede decir 'presente'
        
        eficiencia = hp/cilindrada # por cada lt
        if cilindrada>mayorCilindrada:
            mayorCilindrada = cilindrada
            nombreMayorCilindrada = modelo
            motorCilindrada = tipoMotor
            
        if eficiencia > masEficiente:
            masEficiente = eficiencia
            nombreMasEficiente = modelo
        
        #Para sacar porcentaje
        if transmision =='Manual':
            cManual += 1
            cTransmision += 1
        else:
            cAutomatico += 1
            cTransmision += 1
        
        if cilindrada < menorLocal:
            menorLocal = cilindrada
            nombreMenorLocal = modelo
        
        if ultimaFabricacion == 'Presente':
            if primeraFabricacion<masAntiguo:
                masAntiguo = primeraFabricacion
                nombreMasAntiguo = modelo
        else:
            fabricacion = int(ultimaFabricacion)-primeraFabricacion
            cFabricacion += 1
            sFabricacion += fabricacion
        
        
    if menorLocal < menorGlobal:
        menorGlobal = menorLocal
        nombreMenorGlobal = nombreMenorLocal
    
    if masAntiguo < antiguoGlobal:
        antiguoGlobal = masAntiguo
        nombreAntiguoGlobal = nombreMasAntiguo
    
        
            
    porcManual = cManual/cTransmision*100
    porcAutomatico = cAutomatico/cTransmision*100   
    cFabricacionTotal += cFabricacion
    sFabricacionTotal += sFabricacion
    
        
    print(marca.upper())
    print(f'  El vehículo con mayor cilindrada es {nombreMayorCilindrada} con {mayorCilindrada}L en motor {motorCilindrada}')
    print(f'  El vehículo más eficiente es {nombreMasEficiente} con {masEficiente}')
    print(f'  El {round(porcAutomatico,1)}% de los {marca} tiene transmisión utomática')
    print(f'  y el {round(porcManual,1)} % tiene transmision manual')
    linea = arch.readline().strip()

promFabricacion = sFabricacionTotal/cFabricacionTotal
print(f'El vehículo con menor cilindrada es: {nombreMenorGlobal} con {menorGlobal}L')
print(f'De los vehículos que todavía se fabrican, el que lleva más tiempo es: {nombreAntiguoGlobal}')
print(f'De los vehículos que ya no se fabrican, en promedio su periodo de fabricación fue de {round(promFabricacion,2)} años')