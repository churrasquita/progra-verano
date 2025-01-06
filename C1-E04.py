# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 10:51:56 2025
cata
"""

# obtener datos
print('Calculemos la nota final de la asignatura!')
nota_1 = float(input('Ingresa la nota 1: '))
resiliencia = (input('Rendiste resiliencia?:')).lower()
if resiliencia == 'si':
    nota_resiliencia = float(input('Ingresa la nota de resiliencia:'))
    if nota_1 < 4 and nota_resiliencia >= 4:
        nota_1 = 4
    elif nota_1 >= 4:
        nota_1 = (nota_1+nota_resiliencia)/2
    else:
        nota_1 = nota_1
        
nota_2 = float(input('Ingresa la nota 2: '))

control_1 = float(input('Ingresa la nota del control 1: '))
control_2 = float(input('Ingresa la nota del control 2: '))
desaf_1 = float(input('Ingresa la nota del desafío 1: '))
desaf_2 = float(input('Ingresa la nota del control 2: '))

porc_asistencia = float(input('Ingresa tu porcentaje de asistencia: '))

#calculos 
promedio_notas = (nota_1*0.45)+(nota_2*0.55)
promedio_controles = (control_1 + control_2 + desaf_1 + desaf_2)/4

promedio_final = (promedio_notas* 0.7)+(promedio_controles*0.3)

if porc_asistencia >= 70:
    if (promedio_notas>= 4 and promedio_controles>= 4):
        print('Aprobaste!')
        print(f'Tu promedio es de: {promedio_final}')
    elif (promedio_notas and promedio_controles)>= 3.4 and (promedio_notas and promedio_controles)<= 4:
        print('Debes dar examen recuperativo!')
        nota_recuperativo = float(input('Ingresa nota de tu examen recuperativo!:'))
        if nota_recuperativo >= 4:
            promedio_final = (promedio_controles * 0.30) + (4 * 0.70)
            print(f'Aprobaste el ramo con un promedio de: {promedio_final}')
        else: 
            print('Reprobaste el ramo!')
    else:
        print('reprobaste:(')
else:
    print('reprobaste por asistencia')