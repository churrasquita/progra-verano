# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 12:15:57 2025

@author: LabCivil1-Pc34
"""
def calorias(tipoEjercicio, minutos):
    if tipoEjercicio != 'CORRER' or tipoEjercicio != 'NATACIÓN' or tipoEjercicio != 'BICICLETA':
        return 0
    else:
        
  
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