# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 08:27:35 2025

@author: LabCivil1-Pc34
"""
# En la lista se pueden mezclar los tipos de datos
# no es necesario guardar una variable dentro de la funcion par retornarla, podemos retornar una operacion
# como suma/num

def leerArchivo():
    nombres = []
    archivo = open('nombres.txt', encoding= 'utf-8')
    linea = archivo.readline().strip()
    while linea != '':
        nombres.append(linea)
        linea = archivo.readline().strip()
    return nombres


def obtenerUnicos(lista):
    listaUnicos = []
    for i in lista:
        if not i in listaUnicos: # verifica si el elemento está en la lista
            listaUnicos.append(i)
    return listaUnicos
            
            
def imprimir(lista):
    print('Los nombres únicos son:')
    for i in lista:
        print(i)
            

nombres = leerArchivo() # guardamos la lista con todos los datos del arch
unicos = obtenerUnicos(nombres) # guardamos solamente los únicos en la lista 
imprimir(unicos)