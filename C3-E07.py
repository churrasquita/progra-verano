# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 10:09:42 2025

@author: LabCivil1-Pc34
"""

contNotas = 0
cant_aprobatoria= 0
menor_aprobatoria = 9999
nombreMenorApro = ''
cant_reprobatoria = 0
mayor_reprobatoria = -111
nombreMayorAprobatoria = ''

nombre = input('Ingrese nombre: ').upper()

while nombre != 'FIN':
    nota = float(input('Ingrese nota: '))
    if nota >= 4:
        cant_aprobatoria += 1
        contNotas += 1
        if nota < menor_aprobatoria:
            menor_aprobatoria = nota
            nombreMenorApro = nombre
    else:
        cant_reprobatoria += 1
        contNotas += 1
        if nota > mayor_reprobatoria:
            mayor_reprobatoria = nota
            nombreMayorAprobatoria = nombre
    
    nombre = input('Ingrese el nombre: ').upper()

porc_aprobatorias = int(cant_aprobatoria/contNotas *100)
porc_reprobatorias = int(cant_reprobatoria/contNotas *100)
print(f'Total de notas ingresadas: {contNotas}')
print(f'Cantidad de notas mayores o iguales a 4.0: {cant_aprobatoria} ({porc_aprobatorias}%)')
print(f'     La menor fue: {menor_aprobatoria} ({nombreMenorApro})')
print(f'Cantidad e notas menores a 4.0: {cant_reprobatoria} ({porc_reprobatorias}%)')
print(f'     La mayor fue: {mayor_reprobatoria} ({nombreMayorAprobatoria})')

    
