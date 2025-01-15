# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 10:40:42 2025

@author: LabCivil1-Pc34
"""
def leerArch(arch):
    linea = arch.readline().strip()
    while linea != '':
        partes = linea.split(',')
        nombreRefugio = partes[0]
        distancia = int(partes[1])
        capacidad = int(partes[2])
        radiacion = partes[3]
        actividad = partes[4] == True
        masConveniente()
        linea = arch.readline().strip()

seleccion = ''
while seleccion != 'FIN': 
    seleccion = input('Ingrese A para Norte o B para sur: ').upper()
    while seleccion != 'A' and seleccion != 'B':
        seleccion = input('Error, Ingrese A para Norte o B para sur: ').upper()
    if seleccion == 'A':
        arch = open('A.txt', 'r', encoding = 'utf-8')
    else: 
        arch = open('B.txt', 'r', encoding = 'utf-8')
    leerArch(arch)
