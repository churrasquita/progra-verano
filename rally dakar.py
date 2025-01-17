# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 16:17:13 2025

@author: catal
"""
def intercambiar(lista, a,b):
    aux= lista[a]
    lista[a]=lista[b]
    lista[b]=aux

def ordenarParalelas(lista,lista2,lista3,lista4):
    for i in range(len(lista)-1):
        for j in range( i+1,len(lista)):
            if lista[i]>lista[j]:
                intercambiar(lista, i, j)
                intercambiar(lista2, i, j)
                intercambiar(lista3, i, j)
                intercambiar(lista4, i, j)
    

# es mejor dejarlas vacías ya que son listas paralelas
pilotos = []
categorias = []
etapas = []
tiempos = []

# guardar datos
arch = open('tiempos.txt', 'r', encoding= 'utf-8')
linea = arch.readline().strip()
while linea != '':
    partes = linea.split(',')
    nombre = partes[0]
    categ = partes[1]
    etapa = partes[2]
    h = int(partes[3])
    m = int(partes[4])
    s = int(partes[5])
    tiempo = (h*3600) + (m*60) + s
    pilotos.append(nombre)
    etapas.append(etapa)
    categorias.append(categ)
    tiempos.append(tiempo)
    
    linea = arch.readline().strip()

# preguntar al usuario
etapa_solicitada = input('Que etapa desea analizar? ').upper()
while etapa_solicitada not in etapas:
    etapa_solicitada = input('La etapa no existe, reingrese la etapa a analizar ').upper()

categoria_solicitada = input('Motos o SxS? ').upper()
while categoria_solicitada!= 'MOTOS' and categoria_solicitada!= 'SXS':
    categoria_solicitada = input('La categoría no existe, reingrese categoría ')
   
# lectura de datos según lo solicitado
sumador = 0
contador = 0

for i in range(len(pilotos)):
    if etapa_solicitada == etapas[i] and categoria_solicitada == categorias[i].upper():
        sumador += tiempos[i]
        contador += 1
        
promedio = sumador/contador
print('a)')
print(f'El tiempo promedio de la etapa seleccionada {promedio}')
for i in range(len(pilotos)):
    if tiempos[i]>promedio and etapa_solicitada == etapas[i] and categoria_solicitada == categorias[i].upper():
        print(pilotos[i])

print('b)')
categs = ['Motos', 'SxS'] # definimos nuevamente la lista para imprimir según categoría
for i in range(len(categs)): # se repite 2 veces
    categoria = categs[i] 
    # nuevas listas que se reinician al cambiar de categoría
    pilotosCateg = []
    categoriasCateg=[]
    etapasCateg=[]
    tiemposCateg=[]
    for j in range(len(pilotos)): # recorremos los pilotos 
        if categorias[j]==categoria and etapas[j]==etapa_solicitada:
            # guardamos los que cumplen con la categoría en otras listas
            pilotosCateg.append(pilotos[j])
            categoriasCateg.append(categorias[j])
            etapasCateg.append(etapas[j])
            tiemposCateg.append(tiempos[j])
    print("En la categoria:", categoria) # se imprime primero 1 y después la otra
    # ordenamos las listas: 
    ordenarParalelas(tiemposCateg,categoriasCateg,etapasCateg,pilotosCateg)
    for k in range(3): # para los tres primeros
        print(pilotosCateg[k],"con un tiempo de:", tiemposCateg[k])
