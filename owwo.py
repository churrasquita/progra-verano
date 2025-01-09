# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 20:23:33 2025

@author: catal
"""

mayorImpuesto = -11111
nombreMayor = ''
menorImpuesto = 9999
nombreMenor = ''

impuestosTotales = 0
contTotal = 0
contB = 0
contL= 0
contC = 0

total = 0

categoria = input('Ingrese categoría del producto, Belleza=B, Limpieza=L, Comida = C: ').upper()

while categoria != 'FIN':
    
    while categoria!= 'L' and categoria!= 'B' and categoria !='C':
        categoria = input('Ingrese categoría del producto, Belleza=B, Limpieza=L, Comida = C: ').upper()
    precioProducto = int(input('Ingrese el precio del producto: '))
    while precioProducto < 0:
        precioProducto = int(input('Ingrese el precio del producto: '))
    
    if categoria == 'B':
        impuesto = precioProducto*0.20
        contB += 1
        contTotal += 1
        producto = 'Belleza'
        
    elif categoria == 'L':
        impuesto = precioProducto*0.10
        contL += 1
        contTotal += 1
        producto = 'Limpieza'
        
    else:
        impuesto = precioProducto*0.15
        contC += 1
        contTotal += 1
        producto = 'Comida'
        
    if impuesto > mayorImpuesto:
        mayorImpuesto = impuesto
        nombreMayor = producto
        
    if impuesto < menorImpuesto:
        menorImpuesto = impuesto
        nombreMenor = producto
        
    impuestosTotales += impuesto
    
    valorFinal = precioProducto + (impuesto)
    total += valorFinal
    
    print(f'Valor del impuesto a pagar: {impuesto}')
    print(f'Valor final por pagar por el producto: {valorFinal}')
    print('           ')
    
    categoria = input('Ingrese categoría del producto, Belleza=B, Limpieza=L, Comida = C: ').upper()
    
    
porcB = int(contB/contTotal*100) 
porcL = int(contL/contTotal*100)   
porcC = int(contC/contTotal*100)      

print('           ')
print(f' a) El impuesto más alto fue de: {mayorImpuesto} En un producto de {nombreMayor}')
print(f' b) El impuesto más bajo fue de: {menorImpuesto} En un producto de {nombreMenor}')
print(f' c) El monto total de impuesto es: {impuestosTotales}')
print(f' d) El porcentaje de productos de Belleza es: {porcB} %')
print(f'    El porcentaje de productos de Limpieza es: {porcL} %')
print(f'    El porcentaje de productos de Comida es: {porcC} %')
print(f' e) Total a pagar: {total}')
