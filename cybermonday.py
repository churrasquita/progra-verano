# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 11:57:34 2025

@author: LabCivil1-Pc34
"""

nombreProducto = input('Ingrese el nombre del producto (FIN para terminar): ').upper()

while nombreProducto != 'FIN':
    tipoProducto = input('Ingrese el tipo de producto (ELECTRÓNICA,ROPA,MUEBLE): ').upper()
    descuentoMinimo = 0
    if tipoProducto =='ELECTRÓNICA':
        descuentoMinimo = 0.05
    elif tipoProducto == 'ROPA':
        descuentoMinimo = 0.20
    else:
        descuentoMinimo = 0.10
    
    precio_normal = int(input('Ingrese el precio normal del producto: $ '))
    while precio_normal < 0:
        precio_normal = int(input('Ingrese el precio normal del producto: $ '))
    
    cant_tiendas = int(input('Ingrese la cantidad de tiendas a comparar: '))
    while cant_tiendas < 0:
        cant_tiendas = int(input('Ingrese la cantidad de tiendas a comparar: '))
    
    suma_tiendas = 0
    for i in range(1, cant_tiendas+1):
        precio_comparar = int(input(f'Ingrese el precio visto en la tienda {i}: $'))
        suma_tiendas += precio_comparar
    promedio_ofertas = suma_tiendas/cant_tiendas
    
    
    
    if promedio_ofertas > precio_normal:
        precio_oferta = (precio_normal - precio_normal*descuentoMinimo)
        print(f'PRECIO OFERTA SUGERIDO: $ {precio_oferta}')
        print(f'DESCUENTO: {descuentoMinimo*100} %')
    else: 
        precio_oferta = (promedio_ofertas - promedio_ofertas*0.5)
        descuento = (precio_oferta*precio_normal)/100
   

    nombreProducto = input('Ingrese el nombre del producto (FIN para terminar): ').upper()
