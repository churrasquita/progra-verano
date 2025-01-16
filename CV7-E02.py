# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 09:29:39 2025

@author: LabCivil1-Pc34
"""
def obtenerLista(arch):
    arch = open(arch, encoding = 'utf-8')
    linea = arch.readline().strip()
    lista = []
    while linea != '':
        lista.append(linea)
        linea = arch.readline().strip()
    return lista

def obtenerUnicos(lista):
    unicos = []
    for i in (lista):
        if not i in unicos:
            unicos.append(i)
    return unicos        

def determinarPresentes(lista1, lista2):
    presentes = []
    for i in lista1:
        for j in lista2: 
            if i in lista1 and j in lista2 and (i == j):
                presentes.append(i)
    unicos = obtenerUnicos(presentes)
    return unicos

def imprimir(lista):
    print('Los nombres ya presentes en la lista son: ')
    for i in lista:
        print(i)
    

nombres1 = obtenerLista('nombres1.txt')
nombres2 = obtenerLista('nombres2.txt')
presentes = determinarPresentes(nombres1, nombres2)
imprimir(presentes)

# tengo que sacar los únicos primero y despues comparar o 
# puedo comparar ambas listas y despues eliminar los que se repiten
# tengo que hacer un for dentro de otro para comparar