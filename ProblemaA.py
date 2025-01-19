# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 16:30:52 2025

@author: Usuario
"""

def imprimir(lista1,lista2):
    for i in range(3):
        print(f'{lista1[i]} - {lista2[i]} días')
def calcularPorc(lista):
    premium = 0
    basica = 0
    total = 0
    for i in range(len(lista)):
        if lista[i] == 'P':
            premium += 1 
            total += 1
        else:
            basica += 1 
            total += 1 
    porcPremium = premium/total *100
    porcBasicas = basica/total *100
    return porcPremium, porcBasicas
   
def intercambiar(lista, a, b):
    aux = lista[a]
    lista[a] = lista[b]
    lista[b] = aux

def ordenar(lista1, lista2):
    for a in range(len(lista1)):
        for b in range(a+1, len(lista2)):
            if lista1[a] < lista1[b]:
                intercambiar(lista1, a, b)
                intercambiar(lista2, a, b)

arch = open('contratos.txt', encoding = 'utf-8')
linea = arch.readline().strip()

plataformas = []
frecuencias = []
rutsN = []
rutsA = []
rutsH = []
tiemposN= []
tiemposA = []
tiemposH = []
netflix = []
amazon = []
hbo = []
contadorVOD= 0
premiums = 0
basicas = 0
while linea != '': 
    partes = linea.split(',')
    plataforma = partes[0]
    rut = partes[1]
    tipoCuenta = partes[3]
    tiempo = int(partes[2])
    
    if plataforma == 'N':
        plataforma = 'Netflix'
        netflix.append(tipoCuenta)
        tiemposN.append(tiempo)
        rutsN.append(rut)
    elif plataforma == 'H':
        plataforma = 'Hbo'
        hbo.append(tipoCuenta)
        tiemposH.append(tiempo)
        rutsH.append(rut)
    elif plataforma == 'A':
        plataforma = 'Amazon'
        amazon.append(tipoCuenta)
        tiemposA.append(tiempo)
        rutsA.append(rut)
    if not plataforma in plataformas:
        plataformas.append(plataforma)
        frecuencias.append(1)
        contadorVOD +=1
    else:
        idx = plataformas.index(plataforma) # me encuentra el índice de la marca
        frecuencias[idx] += 1
        contadorVOD += 1
    if tipoCuenta == 'P':
        premiums += 1 
    else:
        basicas += 1
        
    linea = arch.readline().strip()

print('a)')
print('Porcentaje de clientes por cada servicio VOD:')
ordenar(frecuencias,plataformas)
for i in range(len(plataformas)):
    print(f'{plataformas[i]}: {(frecuencias[i]/contadorVOD*100)} %')

print('Porcentaje de clientes por tipo de servicio VOD:')
print('')
print(f'Cuentas básicas: {basicas/contadorVOD*100} %')
print(f'Cuentas premiums: {premiums/contadorVOD*100} %')

porcPremium, porcBasicas = calcularPorc(netflix)
print(f'Netflix: Básicas {porcBasicas} % - Premium {porcPremium} %')
porcPremium, porcBasicas = calcularPorc(amazon)
print(f'Amazon: Básicas {porcBasicas} % - Premium {porcPremium} %')
porcPremium, porcBasicas = calcularPorc(hbo)
print(f'Hbo: Básicas {porcBasicas} % - Premium {porcPremium} %')

print('b)')
print('Netflix: ')
ordenar(tiemposN, rutsN)
imprimir(rutsN, tiemposN)
print('Amazon:')

# arch = open('contratos.txt', encoding = 'utf-8')
# linea = arch.readline().strip()
# plataformas = []
# frecuencias = []
# tiempos = []
# tiposCuentas = []

ordenar(tiemposA, rutsA)
imprimir(rutsA, tiemposA)
print('HBO:')
ordenar(tiemposH,rutsH)
imprimir(rutsH, tiemposH)
