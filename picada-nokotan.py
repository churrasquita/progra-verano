# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 21:14:53 2025

@author: catalina
"""
contador_pedidos = 1 
print('Bienvenido a la picada de Nokotan!')

procesar_pedidos = 'SI' 
ganancias = 0
mas_costoso = -11111
valor_mascostoso = -111
aplica_descuento = 0

# contadores de cada plato para poder sacar el menor global
cont_arroz= 0
cont_sopa = 0
cont_galletas= 0
menor_global= 9999999
plato_menos_pedido = ''

while procesar_pedidos != 'NO': # mientras el usuario no ingrese esta palabra
    print('     ')
    print(f'PEDIDO #{contador_pedidos}!')
    print('MENU DE LA PICADA')
    print('[ARROZ] Arroz de Bashame ($2500)')
    print('[SOPA] Sopa de Astas ($1500)')
    print('[GALLETAS] Galletas Shika ($1000)')
    print('[PAGAR] Realizar pago del pedido')
    
    plato = input('Selecciona un plato: ').upper()
    valor_pedido = 0
    
    while plato != 'PAGAR':
        if plato == 'ARROZ':
            valor_pedido += 2500
            cont_arroz += 1
    
        elif plato == 'SOPA':
            valor_pedido +=1500
            cont_sopa += 1
        
        else: # no necesita condición ya que es la única opción que queda
            valor_pedido += 1000
            cont_galletas += 1
        
        plato = input('Selecciona un plato: ').upper()
    
    ganancias += valor_pedido
    print(f'Total del pedido: ${valor_pedido}')
    procesar_pedidos = input('Desea seguir procesando pedidos: ').upper() #sólo preguntamos una vez
    if procesar_pedidos == 'NUN!': 
        ganancias -= (valor_pedido*0.10)
        valor_pedido*=0.90
        print('Excelente! Se ha aplicado el descuento del 10%')
        print(f'Nuevo total del pedido: ${valor_pedido}')
        aplica_descuento += 1
        procesar_pedidos = input('Desea seguir procesando pedidos: ').upper()
        
    if valor_pedido>valor_mascostoso:
        mas_costoso = contador_pedidos
        valor_mascostoso = valor_pedido
    
    contador_pedidos += 1 
    
# sacar el menor pedido
if cont_arroz < cont_sopa and cont_arroz < cont_galletas:
    plato_menos_pedido = "Arroz"
    menor_global = cont_arroz
elif cont_sopa< cont_arroz and cont_sopa<cont_galletas:
    plato_menos_pedido = "Sopa de Astas"
    menor_global = cont_sopa
else:
    plato_menos_pedido = "Galletas Shika"
    menor_global = cont_galletas

print('     ')
print('RESUMEN DEL DIA!')
print(f'Pedidos realizados: {contador_pedidos-1}')
print(f'Ganancia: ${ganancias}')
print(f'Pedido más costoso: #{mas_costoso} (${valor_mascostoso})')
print(f'Plato menos pedido: {plato_menos_pedido} ({menor_global})')
print(f'Num. veces canje de descuento: {aplica_descuento}')
