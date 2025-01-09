# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 08:26:27 2025

@author: LabCivil1-Pc34
"""
año = int(input('Ingrese un año específico (2022 a 2024): '))
while año<2022 or año>2024:
    año = int(input('Ingrese un año específico (2022 a 2024): '))

arch = open('datos.txt', 'r', encoding ='utf-8')
linea = arch.readline().strip()

cPuntaje = 0
aPuntaje = 0
cDuracion = 0
aDuracion = 0

mayorPuntaje = -111
nombreMayorPuntaje = ''
segundoMayor = -11
nombreSegundoMayor = ''
ultimoJugador = ''
añoUltimoJugador = 0
c2022= 0 
c2023 = 0 
c2024= 0 
añoMasPartidas = -111

while linea != '':
    
    partes = linea.split(',')
    nombre = partes[0]
    partes2 = (partes[1]).split(';')
    puntaje = int(partes2[0])
    añoJugado = int(partes2[1])
    duracion = int(partes[2])
    if añoJugado>=2022 and añoJugado<=2024: 
        cPuntaje += 1
        aPuntaje += puntaje
        cDuracion += 1
        aDuracion += duracion
        
        if puntaje > mayorPuntaje:
            segundoMayor = mayorPuntaje
            nombreSegundoMayor = nombreMayorPuntaje
            mayorPuntaje = puntaje
            nombreMayorPuntaje = nombre
        elif puntaje > segundoMayor:
            segundoMayor = puntaje
            nombreSegundoMayor = nombre
            
        if año%2==0 and año == añoJugado:
            ultimoJugador = 'Último jugador del año ' + nombre 
            añoUltimoJugador = año
        elif año%2==0 and año!= añoJugado:
            ultimoJugador = 'No hay registro del año'
            añoUltimoJugador = año
        
        if añoJugado == 2022:
            c2022 += 1
        if añoJugado == 2023:
            c2023 += 1
        if añoJugado == 2024:
            c2024 += 1 
            
    
    linea = arch.readline().strip()
    
promPuntaje = aPuntaje/cPuntaje
promDuracion = aDuracion/cDuracion

if c2022>c2023 and c2022>c2024:
    añoMasPartidas = 2022 
elif c2023>c2022 and c2023>c2024:
    añoMasPartidas = 2023 
elif c2024>c2022 and c2024>c2023:
    añoMasPartidas = 2024
    
print(f'- Puntaje promedio: {promPuntaje}')
print(f'- Duración promedio: {promDuracion}')
print(f'- Jugador con mayor puntaje: {nombreMayorPuntaje} con {mayorPuntaje} puntos.')
print(f'- Jugador con segundo mayor puntaje: {nombreSegundoMayor} con {segundoMayor} puntos.')
if año%2 == 0:
    print(f'- {ultimoJugador} {añoUltimoJugador}')

print(f'- Año con mayor cantidad de partidas: {añoMasPartidas}')