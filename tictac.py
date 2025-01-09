# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 11:02:35 2025

@author: LabCivil1-Pc34
"""
despliegue = ''

while despliegue != 'FIN':
    print('-------Menú-------')
    print('Elige un filtro o fin para terminar')
    despliegue = input('(T) Tipo (S) Sumergible (FIN): ').upper()
    while despliegue!= 'T' and despliegue!= 'S' and despliegue!= 'FIN':
        despliegue = input('(T) Tipo (S) Sumergible (FIN): ').upper()
    
    if despliegue == 'T':
        tipo = input('(A) Analógico (D) Digital (AD) Ambos: ').upper()
        if tipo == 'A':
            tipo = 'Analógico'
        elif tipo == 'D':
            tipo == 'Digital'
        else:
            tipo = 'Analógico/Digital'
            
           # RECIEN ABRIR EL ARCHIVO 
        arch = open('relojes.txt', encoding= 'utf-8')
        linea = arch.readline().strip()
        while linea != '':
            partes = linea.split(',')
            idReloj= partes[0]
            nombreReloj = partes[1]
            precio = int(partes[2])
            tipoReloj = partes[3]
            
            if tipoReloj == tipo: # para comprobar que sean del mismo tipo
                print(idReloj,nombreReloj,precio)
            linea = arch.readline().strip()
            
        numRelojCompra = int(input('Ingrese numero de reloj a comprar: '))
        arch = open('relojes.txt', encoding= 'utf-8')
        linea = arch.readline().strip()
        while linea != '':
            partes = linea.split(',')
            idReloj= partes[0]
            nombreReloj = partes[1]
            precio = int(partes[2])
            tipoReloj = partes[3]
            if tipoReloj==tipo and numRelojCompra==idReloj:
                print(f'COMPRADO {idReloj} {nombreReloj} {precio}')
         

    elif despliegue == 'S':
        sumergible = input('(S) Sumergible (N) No Sumergible: ')
        if sumergible == 'S':
            sumergible == 'Sí'
        else:
            sumergible = 'No'
            
        arch = open('relojes.txt', encoding= 'utf-8')
        linea = arch.readline().strip()
        
        while linea != '':
            partes = linea.split(',')
            idReloj= partes[0]
            nombreReloj = partes[1]
            precio = int(partes[2])
            tipoReloj = partes[3]
            esSumergible = partes[4]
            if sumergible == esSumergible:
                print(idReloj,nombreReloj,precio)
            linea = arch.readline().strip()
            
        numRelojCompra = int(input('Ingrese numero de reloj a comprar: '))
        arch = open('relojes.txt', encoding= 'utf-8')
        linea = arch.readline().strip()
        
        while linea != '':
            partes = linea.split(',')
            idReloj= partes[0]
            nombreReloj = partes[1]
            precio = int(partes[2])
            tipoReloj = partes[3]
            if esSumergible == sumergible and numRelojCompra==idReloj:
                print(f'COMPRADO {idReloj} {nombreReloj} {precio}')
            linea = arch.readline().strip()
        
        
    numeroReloj = int(input('Seleccione número de reloj a comprar: '))
    
    
print('Total recaudado: ')