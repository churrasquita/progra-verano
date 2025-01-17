# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 08:24:54 2025

@author: LabCivil1-Pc34
"""

def intercambiar(lista, a, b):
    aux = lista[a]
    lista[a] = lista[b]
    lista[b] = aux
    
hoy = int(input('Ingrese el número del día de hoy (1-365): '))
while hoy<1 and hoy>365:
    hoy = int(input('Día inválido. Ingrese el número del día de hoy (1-365): '))

arch = open('tareas.txt', encoding = 'utf-8')
linea = arch.readline().strip()

cursos = []
prioridades = []
eventos = []
diasRestantes_ = []
sumadorPrioridades = 0

while linea != '':
    partes = linea.split(',')
    curso = partes[0]
    evento = partes[1]
    prioridad = int(partes[2])
    dia = int(partes[3])
    if hoy < dia:
        diaRestante = dia-hoy
        cursos.append(curso)
        eventos.append(evento)
        diasRestantes_.append(diaRestante)
        if prioridad == 1:
            prioridad = 'B'
            sumadorPrioridades += 1
        elif prioridad == 2:
            prioridad = 'M'
            sumadorPrioridades += 3
        elif prioridad == 3:
            prioridad = 'A'
            sumadorPrioridades += 5
            
        prioridades.append(prioridad)
        
    linea = arch.readline().strip()

for a in range(len(cursos)):
    for b in range(a+1, len(eventos)):
        if diasRestantes_[a] > diasRestantes_[b]:
            intercambiar(diasRestantes_,a,b)
            intercambiar(cursos,a,b)
            intercambiar(eventos,a,b)
            intercambiar(prioridades,a,b)
        elif diasRestantes_[a] == diasRestantes_[b]:
            if prioridades[a] > prioridades[b]:
                intercambiar(diasRestantes_,a,b)
                intercambiar(cursos,a,b)
                intercambiar(eventos,a,b)
                intercambiar(prioridades,a,b)
            
for i in range(len(cursos)):
    print(f' > [Prioridad {prioridades[i]}] ({diasRestantes_[i]} días restantes) {cursos[i]}: {eventos[i]} ')

print(f'Tienes {sumadorPrioridades} horas restantes de trabajo estimado')