# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 11:20:58 2025

@author: LabCivil1-Pc34
"""
def agregar(e, li):
    if e not in li:
        li.append(e)
    return li

def maximos(edades, paises, listaMaximos):
    mayor = -111*99
    paisMayor = ''
    for i in range(len(paises)):
        suma = 0
        cont= 0
        for j in range(len(edades)):
            suma += edades[j]
            cont += 1
        promedio = suma/cont
        if promedio > mayor:
            mayor = promedio
            paisMayor = paises[i]
            listaMaximos.append(paisMayor)
        elif promedio == mayor:
            listaMaximos.append(paises[i])
    print(mayor)

def inmigracion(paises, ciudades, residencias, nacionalidades):
    
    for j in range(len(paises)): 
        inmigrantes = 0
        total = 0
        for i in range(len(nombres)):
            indicePais= paises.index(nacionalidades[i])
            ciudadResidencia= residencias[i]
            if ciudadResidencia!= ciudades[indicePais]:
                inmigrantes += 1
            total += 1
        print(f'{paises[j]}: {inmigrantes} inmigrantes, {inmigrantes/total*100}% del total')

print('Bienvenido al sistea de censo, ¿qué información desea saber?: ')
print('1. Mostrar inmigración por país')
print('2. Mostrar población más longeva')
print('3. Mostrar Población total por país')
print('4. Mostrar 3 ciudades más habitadas')
print('0. Salir')

arch = open('personas.txt', encoding = 'utf-8')
linea = arch.readline().strip()
ciudadesResidencias = []
nombres = []
nacionalidades = []
edades = []
while linea != '':
    partes = linea.split(',')
    nombre = partes[0]
    apellido = partes[1]
    ciudadResidencia = partes[2]
    edad = int(partes[3])
    nacionalidad = partes[4]
    nombres.append(nombre)
    ciudadesResidencias.append(ciudadResidencia)
    nacionalidades.append(nacionalidad)
    edades.append(edad)
    linea = arch.readline().strip()

arch2 = open('ciudades.txt', encoding = 'utf-8')
linea2 = arch2.readline().strip()

paises = []
ciudades = []
while linea2 != '':
    partes2 = linea2.split(',')
    pais = partes2[0]
    ciudad = partes2[1]
    paises = agregar(pais, paises)
    ciudades = agregar(ciudad, ciudades)
    
    linea2 = arch2.readline().strip()
    
inmigracion(paises, ciudades,ciudadesResidencias,nacionalidades)

listaMaximos = []
maximos = maximos(edades, paises, listaMaximos)