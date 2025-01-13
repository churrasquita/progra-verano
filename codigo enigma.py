# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 00:18:08 2025

@author: catal
"""
arch = open('codigo_enigma.txt', 'r', encoding = 'utf-8')
linea = arch.readline().strip()

mensaje = ''

while linea != 'endwar':
    if len(linea)%2 != 0:
        partes = linea.split('?V=')
        partesSep = (partes[0]).split(':')
        separador = partesSep[1]
        posicion = int(partes[1])
        linea = arch.readline().strip()
        partesMensaje = linea.split(separador)
        for i in range (len(linea)):
            if i == posicion:
                mensaje += partesMensaje[i]
        
    linea = arch.readline().strip()
print(mensaje)