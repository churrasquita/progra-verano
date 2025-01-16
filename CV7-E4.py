# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 16:25:24 2025

@author: catal
"""
def leerArchivo():
    arch = open('numeros.txt', 'r', encoding = 'utf-8')
    linea = arch.readline().strip()
    lista = []
    while linea != '':
        lista.append(int(linea))
        linea = arch.readline().strip()
    return lista

def analizarLista(lista):
    minimo = 9999*99
    maximo = -1111*99
    sumador = 0
    contador = 0
    for i in range(len(lista)):
        contador += 1
        sumador += (lista[i])
        if lista[i] > maximo:
            maximo = lista[i]
        if lista[i] < minimo:
            minimo = lista[i]
    print(f'El minimo de la lista fue {minimo}')
    print(f'El maximo de la lista fue {maximo}')
    print(f'La suma de la lista fue {sumador}')
    print(f'El promedio de la lista fue {sumador/contador}')


numeros_ = leerArchivo()
analizarLista(numeros_)