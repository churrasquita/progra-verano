# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 10:28:37 2025

@author: LabCivil1-Pc34
"""
propiedad = 1
mayor_puntaje= -1
nombreMayorPuntaje = 0
segunda_mayor = -111
nombreSegundaMayor = 0
puntos_propiedad = 0

cant_condicion = 0
puntajes_totales = 0

cant_habitaciones= int(input('Ingrese la cantidad de habitaciones de la propiedad (ingrese -1 para salir): '))

while cant_habitaciones != -1:
    area_total_construida = 0
    print(f'PROPIEDAD {propiedad}')
    print('----------------')
    print('Cáculo del área construida:')
    for i in range(1, cant_habitaciones+1):
        ancho = int(input(f'- Ancho de la habitación {i} (m): '))
        alto = int(input(f'- Alto de la habitación {i} (m): '))
        area_construida = ancho * alto
        area_total_construida += area_construida
    print(f'El área total construida de la propiedad es de {area_total_construida} (m2)')
    
    if area_total_construida > 200:
        puntos_propiedad += 15
    elif area_total_construida<200 and area_total_construida >100:
        puntos_propiedad += 5
    
    print('-----------------')
    area_total = float(input('Indique el área total de la propiedad (incluyendo jardín, patio, área construida, etc): '))
    porc_construido = area_total_construida/area_total *100
    if porc_construido < (area_total/2*100):
        puntos_propiedad += 5
        if area_total_construida > 200:
            puntos_propiedad += 10
    
        tiene_piscina = input('La propiedad tiene piscina? (SI/NO): ').upper()
        if tiene_piscina =='SI':
            puntos_propiedad += 5
        tiene_parrilla = input('La propiedad tiene parrilla? (SI/NO): ').upper()
        if tiene_parrilla == 'SI':
            puntos_propiedad += 5
        if tiene_parrilla == 'SI' and tiene_piscina == 'SI':
            puntos_propiedad += 5
    
    colegio_cercano = float(input('Indique la distancia al colegio más cercano: '))
    if colegio_cercano <= 3000:
        puntos_propiedad += 5
    elif colegio_cercano > 3000 and colegio_cercano < 10000:
        puntos_propiedad += 2
    else: 
        puntos_propiedad -= 2
    
    cant_supers = int(input('Cuántos supermercados cercanos hay?: '))
    if cant_supers>2:
        puntos_propiedad += 5
    elif cant_supers>=1 and cant_supers<=2:
        puntos_propiedad += 2
    else:
        puntos_propiedad -= 5
    
    if colegio_cercano<= 3000 and cant_supers >2:
        puntos_propiedad += 5
    print('-----------------------------')
    print('RESULTADOS:')
    print(f'El puntaje de la propiedad {propiedad} es de {puntos_propiedad} puntos.')
    
    if puntos_propiedad>mayor_puntaje:
        segunda_mayor = mayor_puntaje
        nombreSegundaMayor = nombreSegundaMayor 
        mayor_puntaje = puntos_propiedad
        nombreMayorPuntaje = propiedad
    elif puntos_propiedad> segunda_mayor:
        segunda_mayor = puntos_propiedad
        nombreSegundaMayor = propiedad
    
    if puntos_propiedad>=0 and puntos_propiedad<= 20:
        cant_condicion += 1
    
    if puntos_propiedad > 40:
        print(f'SE RECOMIENDA SU COMPRA (Propiedad n° {propiedad})')
    
    propiedad += 1
    puntajes_totales += puntos_propiedad
    cant_habitaciones= int(input('Ingrese la cantidad de habitaciones de la propiedad (ingrese -1 para salir): '))

porc_condicion = cant_condicion/propiedad*100
promedio_puntajes = puntajes_totales/propiedad

print('--------------------------------------')
print('RESUMEN')
print(f'- La propiedad con mayor puntaje fue {nombreMayorPuntaje} con {mayor_puntaje} pts.')
print(f'- La segunda propiedad con mayor puntaje fue {nombreSegundaMayor} con {segunda_mayor} pts. ')
print(f'- La cantidad de propiedades entre 0 y 20 pts fue de:  {cant_condicion} ({porc_condicion}%)')
print(f'- El promedio de puntajes de todas las propiedades fue de: {promedio_puntajes}')

