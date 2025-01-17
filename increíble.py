# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 16:45:11 2025

@author: catal
"""

def frecuenciaMarcas(e, li):
    for i in range(len(li)):
        if li[i] == e:
            contMarcas[i] += 1
    return contMarcas

def intercambiar(lista, a, b):
    aux = lista[a]
    lista[a] = lista[b]
    lista[b] = aux

def burbuja(lista1, lista2, direccion):
    for a in range(len(lista1)-1):
        for b in range(a+1,len(lista2)):
            if direccion == True: # de menor a mayor
                if lista2[a] > lista2[b]:
                    intercambiar(lista1, a, b)
                    intercambiar(lista2, a, b)
            elif direccion == False: # de mayor a menor
                if lista2[a] < lista2[b]:
                    intercambiar(lista1, a, b)
                    intercambiar(lista2, a, b)
                
        
def obtenerMayor(mayor, nombreMayor, valor, nombreValor, marca):
    if valor > mayor:
        mayor = valor
        nombreMayor = f'{marca} {nombreValor}'
    return mayor, nombreMayor

def obtenerDensidad(resPantalla, tamañoPantalla):
    partesP = resPantalla.split('x')
    diagonalPixeles = (((int(partesP[0]))**2) + ((int(partesP[1]))**2))**(1/2)
    ppi = diagonalPixeles/tamañoPantalla
    return ppi


arch = open('celulares.txt', 'r', encoding = 'utf-8')
linea = arch.readline().strip()
marcas_ = ['Samsung', 'Sony', 'Motorola', 'Huawei', 'Apple', 'Xiaomi', 'LG','Nokia']
contMarcas = [0,0,0,0,0,0,0,0]
baterias_ =[]
modelosBaterias_ = []

mayorRes = -1111
nombreMayorRes = ''

mayorPantalla = -1111
nombreMayorPantalla = ''

while linea != '': 
    partes = linea.split('-')
    marca = partes[0]
    modelo = partes[1]
    resCamara = int(partes[2])
    resPantalla = partes[3]
    tamañoPantalla = float(partes[4])
    amperaje = int(partes[5])
    
    contMarcas = frecuenciaMarcas(marca,marcas_)
    mayorRes, nombreMayorRes = obtenerMayor(mayorRes, nombreMayorRes, resCamara, modelo, marca)
    densidad  = obtenerDensidad(resPantalla, tamañoPantalla)
    mayorPantalla, nombreMayorPantalla = obtenerMayor(mayorPantalla, nombreMayorPantalla, densidad, modelo, marca)
    if amperaje > 4000:
        baterias_.append(amperaje)
        modelosBaterias_.append(f'{marca} {modelo}')
    
    linea = arch.readline().strip()

print('1) Celulares analizados') 
burbuja(marcas_, contMarcas, True)
for i in range(len(marcas_)):
    print(f'{marcas_[i]}: {contMarcas[i]}')
print(f'2) Cámara increíble: {nombreMayorRes}')
print(f'2) Pantalla increíble: {nombreMayorPantalla} ({round(mayorPantalla)} ppi)')
burbuja(modelosBaterias_, baterias_, False)
print('4) Baterías que duran mucho más:')
for i in range(len(baterias_)):
    print(f'{modelosBaterias_[i]} ({baterias_[i]} mAh)')


# OTRA FORMA DE ENCUNTRAR LA FRECUENCIA 

# arch = open('celulares.txt', 'r', encoding = 'utf-8')
# linea = arch.readline().strip()

# marcas = []
# frecuencias = []
# while linea != '': 
#     partes = linea.split('-')
#     marca = partes[0]
#     if not marca in marcas:
#         marcas.append(marca)
#         frecuencias.append(1) # cuenta la marca que acaba de ingresar
#     else:
#         idx = marcas.index(marca) # me encuentra el índice de la marca
#         frecuencias[idx] += 1
#     linea = arch.readline().strip()
