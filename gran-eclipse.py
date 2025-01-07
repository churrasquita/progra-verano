# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 11:10:10 2025

@author: LabCivil1-Pc34
"""
cant_clientes = int(input('Cantidad de clientes por confirmar: '))

clientes_totales = 0 
clientes_confirmados = 0

mas_dias = -11111111
n_mayoReserva = ''

ingreso_confirmado = 0
ingreso_extra = 0
ingreso_libre = 0

h_premium = 0
h_standard = 0

if cant_clientes == 0:
    print('Hoy no se han realizado llamados')
else: 

    for i in range(cant_clientes):
        nombre = input('Nombre del cliente: ')
        dias = int(input('Días reservados por el cliente: '))
        
        tarifa = input('Tarifa (S/P): ').upper()
        while tarifa!= 'S' and tarifa!='P':
            tarifa = input('Ingrese opción válida (S/P): ').upper()
        if tarifa == 'S':
            valor_dia = 120
            total = valor_dia * dias
            h_standard += 1
        elif tarifa == 'P':
            valor_dia = 250
            total = valor_dia * dias
            h_premium += 1
        
        confirmacion = input('Confirmación (S/N): ').upper()
        while confirmacion!='S' and confirmacion!='N':
            confirmacion = input('Ingrese opción válida (S/N): ').upper()
        
        if confirmacion == 'S':
            d_adicionales = int(input('Desea agregar más días a la reserva (ingrese 0 si no agreaga): '))
            valor_adicional = (d_adicionales*valor_dia)
            total += valor_adicional
            print(f'Reserva confirmada, total: USD {total}')
            clientes_confirmados += 1
            clientes_totales += 1
            dias += d_adicionales
            ingreso_confirmado += total
            ingreso_extra += valor_adicional
            
            
        else:
            devolucion = total*0.75
            print(f'Reserva cancelada, devolución: USD {devolucion}')
            clientes_totales += 1
            ingreso_libre += total
            
        
        if dias > mas_dias:
            mas_dias = dias
            n_mayoReserva = nombre
            
            
    print('-------------------------------------------------')
    
    porc_confirmados = (clientes_confirmados/clientes_totales)*100
    
    ingresos_totales = ingreso_confirmado*680 +(ingreso_libre*680*0.25)
    
    
    print(f'Hoy se ha confirmado a {clientes_confirmados} clientes(s) {porc_confirmados}')
    print(f'El cliente confirmado que más días reservó fue: {n_mayoReserva}')
    print(f'El ingreso confirmado de hoy es: CLP {ingresos_totales}')
    print(f'El ingreso por días extra agregados es: CLP {ingreso_extra*680}')
    print(f'El ingreso por habitaciones libres es: CLP {ingreso_libre*680}')
    print(f'Habitaciones reservadas {h_standard} Standard {h_premium} Premium ')
