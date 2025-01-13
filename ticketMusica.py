# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 16:55:20 2025

@author: catal
"""
def ventas(cantidad, tipo):
    valorVenta = 0
    for i in range (cantidad):
        if tipo =='CANCHA':
            valorVenta += 20_000
        elif tipo == 'PLATEA':
            valorVenta += 30_000
        else:
            valorVenta += 40_000
    print(f'El valor de la venta fue de ${valorVenta}')


cantEntradas = int(input('Ingrese la cantidad de entradas que desea comprar (-1 para salir): '))
while cantEntradas != -1:
    
    tipoEntrada = input('Ingrese el tipo de entrada que desea comprar: ').upper()
    if tipoEntrada != 'CANCHA' and tipoEntrada != 'PLATEA' and tipoEntrada != 'VIP':
        tipoEntrada = input('Error! Ingrese el tipo de entrada que desea comprar: ').upper()
    ventas(cantEntradas, tipoEntrada)
    
    cantEntradas = int(input('Ingrese la cantidad de entradas que desea comprar (-1 para salir): '))