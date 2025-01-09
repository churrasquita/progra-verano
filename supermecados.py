# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 10:20:51 2025

@author: LabCivil1-Pc34
"""
arch = open('problema1.txt', encoding='utf-8')
linea = arch.readline().strip()
cant_sucursales = int(linea)

sumaTotal = 0
mayorSucursal = -1111
nombreMayorSucursal = ''

masCaro = -111
sucursalMasCaro = ''
productoMasCaro = ''

for i in range(cant_sucursales):
    linea = arch.readline().strip()
    partes = linea.split(',')
    nombreSucursal = partes[0]
    cantProductos = int(partes[1])
    
    mayorVenta = -111
    productoMayor = ''
    ventasSucursal = 0
    ventasUnitarias = 0
    sumaSucursal = 0
    for j in range (cantProductos):
        linea = arch.readline().strip()
        partes2 = linea.split(',')
        producto = partes2[0]
        cantidad = int(partes2[1])
        valorUnitario = int(partes2[2])
        valorTotal =cantidad*valorUnitario
        if valorTotal > mayorVenta:
            mayorVenta = valorTotal
            productoMayor = producto
        if cantidad == 1:
            ventasUnitarias += 1
            ventasSucursal += 1 
        else: 
            ventasSucursal += 1
        sumaSucursal += valorTotal
        sumaTotal += valorTotal
        
        if valorUnitario>masCaro:
            masCaro = valorTotal
            sucursalMasCaro = nombreSucursal
            productoMasCaro = producto
    if sumaSucursal > mayorSucursal:
        mayorSurcursal = sumaSucursal
        nombreMayorSucursal = nombreSucursal
    
    print('     ')
            
    if ventasSucursal == 0: # para que no se indetermine la div cuando no hayan ventas
        print(f'No hubo ventas en la sucursal {nombreSucursal}')
    else: 
        porcUnitarias = ventasUnitarias/ventasSucursal * 100
        print(f'Producto con mayor venta en sucursal {nombreSucursal}')
        print(f'es {productoMayor} con un total de {mayorVenta}')
        print(f'procentaje de ventas unitarias es {porcUnitarias} %')   
    
    
print('           ')
print(f'Total de ventas {sumaTotal}')
print(f'La sucursal con más ventas es {nombreMayorSucursal}')
print(f'El producto más caro fue {productoMasCaro}')
print(f'Vendido en la sucursal {sucursalMasCaro}')
print(f'con un precio de {masCaro}')
            
        
