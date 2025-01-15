# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 12:15:57 2025

@author: LabCivil1-Pc34
"""
def calorias(tipoEjercicio, minutos):
    if minutos > 20:
        # multiplicamos los primeros 20 min y el resto de min es el total-20
        if tipoEjercicio == 'CORRER':
            calorias = (20*10) + ((minutos-20)*12) 
        elif tipoEjercicio == 'BICICLETA':
            calorias = (20*4) + ((minutos-20)*5)
        elif tipoEjercicio == 'NATACIÓN':
            calorias = (20*7) + ((minutos-20)*8)
        else: # si es que no es ninguno de los ejercicios 
            return 0
    else:
        if tipoEjercicio == 'CORRER':
            calorias = (minutos*10)
        elif tipoEjercicio == 'BICICLETA':
            calorias = (minutos*4)
        elif tipoEjercicio == 'NATACIÓN':
            calorias = (minutos*7)
        else:
            return 0
    return calorias
  
def imprimir_cal(arch):
    linea = arch.readline().strip()
    while linea != '': 
        partes = linea.split(',')
        ejercicio= (partes[0]).upper()
        minutos = int(partes[1])
        cal = calorias(ejercicio, minutos)
        print(f'{partes[0]} : {cal} calorías')
        linea = arch.readline().strip()

arch = open('ejercicios.txt', 'r', encoding= 'utf-8')
imprimir_cal(arch)
