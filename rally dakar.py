# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 11:49:42 2025

@author: LabCivil1-Pc34
"""
def buscarAgregar(e, li):
    if e not in li:
        li.append(e)

def obtenerTiempo(h, m, s):
    h = h * 3600
    m = m * 60
    tiempo = h + m + s 
    return tiempo
    

arch = open('tiempos.txt', encoding = 'utf-8')
linea = arch.readline().strip()
categorias_ = []
etapas_ = []
pilotos = []
tiempos = []
while linea != '':
    partes = linea.split(',')
    categoria = partes[1].upper()
    etapa = partes[2].upper()
    hora = int(partes[3])
    minutos = int(partes[4])
    segundos = int(partes[5])
    tiempo = obtenerTiempo(hora, minutos, segundos)
    etapas_.append(etapa)
    categorias_.append(categoria)
    pilotos.append(partes[0])
    tiempos.append(tiempo)
    
    linea = arch.readline().strip()

analizar = input('Que etapa desea analizar?').upper()
while analizar not in etapas_:
    analizar = input('La etapa no existe, reingrese la etapa a analizar ').upper()
    
categoriaS = input('Motos o SxS?').upper()
while categoriaS not in categorias_:
    categoriaS = input('La categoria no existe, reingrese categoría ').upper()

arch = open('tiempos.txt', encoding = 'utf-8')
linea = arch.readline().strip()

# for i in range(len(pilotos)):
    