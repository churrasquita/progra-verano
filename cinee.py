# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 17:26:03 2025

@author: catal
"""
def porcOcupacion(cine):
    totalAsientos = cine.shape[0] * cine.shape[1]
    asientosOcupados = 0
    # recorremos la matriz
    for fila in range(8):
        for col in range(11):
            if cine[fila,col] == 1: # si es que está ocupado
                asientosOcupados += 1
    return asientosOcupados/totalAsientos *100 

def mayorLibre(cine):
    mayor = -11111*99
    mayorFila = 0
    for fila in range(8):
        suma = 0 # se debe reiniciar luego de cada fila
        for col in range(11):
            if cine[fila][col] == 0: # los que están vacios
                suma += 1
        if suma>mayor:
            mayor = suma
            mayorFila = fila
    return mayorFila

def recaudacionTotal(cine):
    precio = 5000
    recaudacion = 0
    for fila in range(8):
        for col in range(11):
            if cine[fila][col] == 1:
                recaudacion += precio
    return recaudacion

def reservar_asiento(cine, fila, col):
    if cine[fila, col] == 0:
       cine[fila, col] = 1 # ahora está reservado
       return True
    else: # si es -1
       return False
   
def mayorCliente(clientes,entradas):
    mayor = -111
    posc = 0
    # sólo necesito recorrer una lista ya que son paralelas
    for j in range(len(entradas)):
        if entradas[j] > mayor:
            mayor = entradas[j]
            posc = j
    return clientes[posc]

def tresMayores(cine,columnas):
    lista_total_columnas_usadas = []# creamos una lista para guardar todas las sumas
     #vamos cambiando primero las filas
           # se lo agregamos a la lista
    # recorremos la lista de las sumas para comparar y ordenamos la matriz
    for j in range(cine.shape[1]):
        cantidad = 0
        for i in range(cine.shape[0]):
            if cine[i, j] == 1:
                cantidad += 1
        lista_total_columnas_usadas.append(cantidad)

    for i in range(1, len(lista_total_columnas_usadas)):
        for j in range(0, len(lista_total_columnas_usadas) - i):
            if lista_total_columnas_usadas[j] < lista_total_columnas_usadas[j + 1]:
                lista_total_columnas_usadas[j], lista_total_columnas_usadas[j + 1] = lista_total_columnas_usadas[j + 1], lista_total_columnas_usadas[j]
                columnas[j], columnas[j + 1] = columnas[j + 1], columnas[j]

    print('Tres columnas con mayor cantidad de asientos ocupados:')
    for i in range(3):
        print(f'- Columna {columnas[i]}: {lista_total_columnas_usadas[i]}')
    print()

def mayorReservas(filas,mx):
    mayor = -111
    pos = 0
    for fila in range(len(filas)):
        suma = 0
        for col in range(11):
            suma += mx[fila][col]
        if suma > mayor:
            mayor = suma
            pos = fila 
        # podemos guardar la pos del elemento de la lista paralela
    print(f'La fila más popular es: {filas[pos]}')
            
    
def buscar_agregar(clientes, entradasCompradas, nombre):
    if nombre not in clientes:
        clientes.append(nombre)
        entradasCompradas.append(0)
    return clientes.index(nombre)

import numpy as np

cine = np.zeros([8,11])
arch = open('teatro.txt', 'r', encoding= 'utf-8')
linea = arch.readline().strip()
i = 0 # utilizamos un contador ya que no tenemos una lista paralela para guiarnos
# también cuando es en modo de juego o tablero
poT = ['S', 'P']
while linea != "":
    datos = linea.split(" ")
    for j in range(len(datos)): # para recorrer las columnas
        if datos[j] in poT:
            cine[i, j] = -1 # -1 para pasillo y pantalla
        else:
            cine[i, j] = int(datos[j])

    i += 1
    linea = arch.readline().strip()

mxreservas = np.zeros([8,11])

clientes = []

entradasCompradas = []

archReservas = open('reservas.txt', encoding = 'utf-8')
linea = archReservas.readline().strip()

while linea != '':
    partes = linea.split(';')
    nombre = partes[0]
    
    f = int(partes[1])
    c = int(partes[2])
    if reservar_asiento(cine, f, c):
        pos = buscar_agregar(clientes, entradasCompradas, nombre)
        entradasCompradas[pos] += 1 # sumamos 1 al cliente que corresponda
    else:
        if cine[f, c] != -1:
            mxreservas[f, c] += 1
    linea = archReservas.readline().strip()
    
print(f'Recaudación Total: {recaudacionTotal(cine)}')
filas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
columnas = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11']
porcOcupacion = porcOcupacion(cine)
print(f'Porcentaje de ocupación: {round(porcOcupacion,2)}% ')
print(f'Fila con mayor cantidad de asientos libres: {mayorLibre(cine)}')
print(f'El cliente con más entradas compradas es: {mayorCliente(clientes, entradasCompradas)}')

tresMayores(cine,columnas)

mayorReservas(filas,mxreservas)