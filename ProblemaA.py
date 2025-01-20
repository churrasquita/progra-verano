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

# def agregarFrecuencias(e, li, fr):
#     if not e in li:
#        li.append(e)
#        fr.append(1)
#     else:
#         idx = li.index(e) # me encuentra el índice 
#         fr[idx] += 1
        

# def intercambiar(lista, a, b):
#     aux = lista[a]
#     lista[a] = lista[b]
#     lista[b] = aux

# def ordenar(lista1, lista2, direccion):
#     for a in range(len(lista1)):
#         for b in range(a+1, len(lista2)):
#             if direccion == False:
#                 if lista1[a] < lista1[b]:
#                     intercambiar(lista1, a, b)
#                     intercambiar(lista2, a, b)
#             elif direccion == True:
#                 if lista1[a] > lista1[b]:
#                     intercambiar(lista1, a, b)
#                     intercambiar(lista2, a, b)
                
# arch = open('contratos.txt', encoding = 'utf-8')
# linea = arch.readline().strip()

# plataformasUnicas = []
# plataformas = []
# frecuencias = []
# ruts = []
# tiempos = []
# tiposCuentas = []
# tipos = []
# frecuencias2 = []
# contVOD = 0

# while linea != '':
#     partes = linea.split(',')
#     plataforma = partes[0]
#     rut = int(partes[1])
#     tiempo = int(partes[2])
#     tipoCuenta = partes[3]
    
#     agregarFrecuencias (plataforma, plataformasUnicas, frecuencias)
#     agregarFrecuencias(tipoCuenta,tiposCuentas, frecuencias2)
    
#     plataformas.append(plataforma)
#     ruts.append(rut)
#     tiempos.append(tiempo)
#     tipos.append(tipoCuenta)
    
#     contVOD += 1
    
#     linea = arch.readline().strip()

# print('a)')
# print('Porcentaje de clientes por cada servicio VOD:')
# ordenar(frecuencias,plataformasUnicas, False)

# plataformas2 = ['Netflix', 'Amazon', 'Hbo']
# for i in range(len(plataformas2)):
#     print(f'{plataformas2[i]}: {(frecuencias[i]/contVOD*100)} %')

# print('')
# print('Porcentaje de clientes por tipo de servicio VOD:')
# ordenar(frecuencias2,tiposCuentas, True)
# for i in range(2):
#     if tiposCuentas[i] == 'B':
#         print(f'Cuentas básicas: {frecuencias2[i]/contVOD*100} %')
#     elif tiposCuentas[i] == 'P':
#         print(f'Cuentas premium: {frecuencias2[i]/contVOD*100} %')

# for i in range(len(plataformasUnicas)):
#     contBasicas= 0
#     contPremium=0
#     for j in range(len(plataformas)):
#         if plataformasUnicas[i] == plataformas[j]:
#             if tipos[j] == 'B':
#                 contBasicas += 1
#             else:
#                 contPremium += 1 
#     print(f'{plataformas2[i]}: Básicas {contBasicas/(contBasicas+contPremium)*100} % - Premium {contPremium/(contBasicas+contPremium)*100} % ')
    
    
# print('b)')
# for i in range(len(plataformas2)):
#     rutsClientes=[]
#     diasClientes = []
#     for j in range(len(plataformas)):
#         if plataformasUnicas[i] == plataformas[j]:
#             rutsClientes.append(ruts[j])
#             diasClientes.append(tiempos[j])
#     ordenar(diasClientes,rutsClientes,False)
#     print(f'{plataformas2[i]}:')
#     for k in range(3):
#         print(f'{rutsClientes[k]} - {diasClientes[k]} días')

# arch2 = open('renuncias.txt', encoding = 'utf-8')
# linea = arch2.readline().strip()

# renuncias = []
# contRenuncias = 0
# while linea != '':
#     renuncias.append(linea)
#     contRenuncias += 1
#     linea = arch2.readline().strip()
# print('c)')
# print(f'Clientes antes del impuesto: {contVOD}')
# print(f'Clientes después del impuesto: {contVOD-contRenuncias}')

# print('Ingresos antes del impuesto:')
# for i in range(len(plataformas2)):
#     cuentasBasicas=0
#     cuentasPremium=0

#     if plataformasUnicas[i]=="N":
#         precioBasico=5000*1.19
#         precioPremium=9000*1.19
#     elif plataformasUnicas[i]=="A":
#         precioBasico=3500*1.15
#         precioPremium=5500*1.15
#     elif plataformasUnicas[i]=="H":
#         precioBasico=3500*1.19
#         precioPremium=4500*1.19
#     for j in range(len(plataformas)):
#         if plataformasUnicas[i]==plataformas[j]:
#             if tipos[j]=="B":
#                 cuentasBasicas+=(precioBasico)
#             else:
#                 cuentasPremium+=(precioPremium)
#     #Ingreso total
#     print(plataformas2[i],':',(cuentasPremium+cuentasBasicas))

# print('Ingreso después del impuesto:')
# for i in range(len(plataformasUnicas)):
#     cuentasBasicas=0
#     cuentasPremium=0
#     if plataformasUnicas[i]=="N":
#         precioBasico=5000*1.19
#         precioPremium=9000*1.19
#     elif plataformasUnicas[i]=="A":
#         precioBasico=3500*1.15
#         precioPremium=5500*1.15
#     elif plataformasUnicas[i]=="H":
#         precioBasico=3500*1.19
#         precioPremium=4500*1.19

#     for j in range(len(renuncias)):
#         if plataformasUnicas[i]==plataformas[j] and ruts[j] not in renuncias:
#             if tipos[j]=="B":
#                 cuentasBasicas+=(precioBasico)
#             elif tipos[j] == 'P':
#                 cuentasPremium+=(precioPremium)
#     #Ingreso total
#     print(f"{plataformas2[i]}: {(cuentasPremium+cuentasBasicas)}")


    



