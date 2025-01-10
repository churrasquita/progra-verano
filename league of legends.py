# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 08:19:39 2025

@author: LabCivil1-Pc34
"""
print('-'*40)
print('            MENU             ')
print('-'*40)
print('1) Cantidad de partidas jugadas')
print('2) Carril preferido')
print('3) KDA')
print('4) Porcentaje de victorias en Clasificatorias')
print('5) Salir')
print('-'*40)

opcion = int(input('Ingrese una opción: '))
while opcion!=1 and opcion!=2 and opcion!=3 and opcion!=4 and opcion!=5:
    opcion = int(input('Ingrese una opción válida: '))
    
while opcion != 5:
    print('   ')

    if opcion == 1:
        arch = open('invocador.txt', 'r', encoding='utf-8')
        linea = arch.readline().strip()
        contNormal = 0
        contSolo = 0
        contFlex = 0
        while linea != '':
            partes = linea.split(',')
            tipoPartida = partes[0]
            if tipoPartida == 'NORMAL':
                contNormal += 1 
            elif tipoPartida == 'SOLO':
                contSolo += 1 
            else: 
                contFlex += 1
            linea = arch.readline().strip()
      
        print('Partidas jugadas')
        print(f'Normales: {contNormal}')
        print(f'Clasificatorias Solo/Duo: {contSolo}')
        print(f'Clasificatorias Flexibles: {contFlex}')
    
    elif opcion == 2:
        arch = open('invocador.txt', 'r', encoding='utf-8')
        linea = arch.readline().strip()
        contTop = 0
        contMid = 0
        contJg = 0
        contAdc = 0
        contSupp = 0
        while linea != '':
            partes = linea.split(',')
            carril = partes[1]
            if carril == 'TOP':
                contTop += 1 
            elif carril == 'MID':
                contMid += 1 
            elif carril == 'ADC':
                contMid += 1 
            else: 
                contSupp += 1
            linea = arch.readline().strip()
            
        if contTop>contMid and contTop>contJg and contTop>contAdc and contTop>contSupp:
            mayorCarril = contTop
            carrilPref = 'Superior'
        elif contMid>contTop and contMid>contJg and contMid>contAdc and contMid>contSupp:
            mayorCarril = contMid
            carrilPref = 'Central'
        elif contJg>contTop and contJg>contMid and contJg>contAdc and contJg>contSupp:
            mayorCarril = contJg
            carrilPref = 'Jungla'
        elif contAdc>contTop and contAdc>contJg and contAdc>contMid and contAdc>contSupp:
            mayorCarril = contAdc
            carrilPref = 'Tirador'
        elif contSupp>contTop and contSupp>contJg and contSupp>contAdc and contSupp>contMid:
            mayorCarril = contSupp
            carrilPref = 'Soporte'
        
        print(f'Carril preferido: {carrilPref}')
    
    elif opcion == 3:
        arch = open('invocador.txt', 'r', encoding='utf-8')
        linea = arch.readline().strip()
        
        totalMuertes = 0
        totalAsesinatos = 0
        totalAsistencias = 0
        while linea != '':
            partes = linea.split(',')
            asesinatos = int(partes[3])
            muertes = int(partes[4])
            asistencias = int(partes[5])
            totalMuertes +=muertes
            totalAsesinatos +=asesinatos
            totalAsistencias += asistencias
            
            linea = arch.readline().strip()
        kda = (totalAsesinatos/totalMuertes) + (totalAsistencias/totalMuertes)
        print(f' KDA: {kda}')
    
    elif opcion == 4:
        arch = open('invocador.txt', 'r', encoding='utf-8')
        linea = arch.readline().strip()
        
        contVict = 0
        totalClasif = 0
        while linea != '':
            partes = linea.split(',')
            tipoPartida = partes[0]
            finPartida = partes[6]
            
            if tipoPartida == 'SOLO' or tipoPartida == 'FLEX':
                totalClasif += 1
            if (tipoPartida == 'SOLO') and (finPartida == 'VICTORIA'):
                contVict += 1
            elif (tipoPartida == 'FLEX') and (finPartida == 'VICTORIA'):
                contVict += 1
                
            linea = arch.readline().strip()
        porcVict = contVict/totalClasif*100
        print(f'Victorias en Clasificatorias: {round(porcVict,2)} %')
    
    print('-'*40)
    print('            MENU             ')
    print('-'*40)
    print('1) Cantidad de partidas jugadas')
    print('2) Carril preferido')
    print('3) KDA')
    print('4) Porcentaje de victorias en Clasificatorias')
    print('5) Salir')
    print('-'*40)

    opcion = int(input('Ingrese una opción: '))
    
print('GG')