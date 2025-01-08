# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 11:57:34 2025

@author: LabCivil1-Pc34
"""

nombreProducto = input('Ingrese el nombre del producto (FIN para terminar): ').upper()

masCostoso = -1111111
nombreMasCostoso = ''
menorDesc = 99999999
nombreMenorDesc = ''
mastiendas = -111
nombreMasTiendas = ''

contadorUtiles = 0

while nombreProducto != 'FIN':
    tipoProducto = input('Ingrese el tipo de producto (ELECTRÓNICA,ROPA,MUEBLE): ').upper()
    while tipoProducto != 'ELECTRÓNICA' and tipoProducto != 'ROPA' and tipoProducto != 'MUEBLE':
        tipoProducto = input('Ingrese el tipo de producto (ELECTRÓNICA,ROPA,MUEBLE): ').upper()
    descuentoMinimo = 0 # lo definimos altiro para después utilizarlo
    if tipoProducto =='ELECTRÓNICA':
        descuentoMinimo = 0.05
        descuentoMaximo = 0.30
    elif tipoProducto == 'ROPA':
        descuentoMinimo = 0.20
        descuentoMaximo = 0.80
    else:
        descuentoMinimo = 0.10
        descuentoMaximo = 0.5
    
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
        precio_oferta = int(precio_normal*(1-descuentoMinimo)) # para que me entregue el restante 
        descuento = descuentoMinimo*100
        print(f'PRECIO OFERTA SUGERIDO: $ {precio_oferta}')
        print(f'DESCUENTO: {descuento} %')
    else: 
        precio_oferta = int(promedio_ofertas*0.95)
        descuento = ((precio_normal-precio_oferta)/precio_normal)*100 # regla de tres simple
        print(f'PRECIO OFERTA SUGERIDO: $ {precio_oferta}')
        print(f'DESCUENTO: {descuento} %')
    
    if precio_normal > masCostoso:
        masCostoso = precio_normal
        nombreMasCostoso = nombreProducto
    if descuento < menorDesc:
        menorDesc = descuento
        nombreMenorDesc = nombreProducto
    if cant_tiendas > mastiendas:
        mastiendas = cant_tiendas
        nombreMasTiendas = nombreProducto
    
    if (descuento) > (descuentoMaximo*100):
        print('NO VALE LA PENA OFRECER ESTE PRODUCTO EN EL EVENTO')
    else:
        contadorUtiles += 1
        
    print('---------------------------------------------------')
    

    nombreProducto = input('Ingrese el nombre del producto (FIN para terminar): ').upper()

print('---------------------------------------')
print(f'PRODUCTO MAS COSTOSO INGRESADO: {nombreMasCostoso}')
print(f'PRODUCTO CON MENOR DESCUENTO: {nombreMenorDesc}')
print(f'PRODUCTO CON MÁS TIENDAS COMPARADAS: {nombreMasTiendas}')
print(f'CANTIDAD DE PRODUCTOS ÚTILES PARA EL EVENTO: {contadorUtiles}')
