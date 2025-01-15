# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 09:44:02 2025

@author: LabCivil1-Pc34
"""

def esPrimo (num):
    if num <= 1:
        return False
    for i in range(2, num): 
        if num % i == 0:
            return False # es decir, no es primo
    return True
    
def impares(barCode):
    impares = 0
    pares = 0
    for num in str(barCode):
        if int(num)%2 != 0:
            impares += 1 
        else: 
            pares += 1
    if impares > pares:
        return True
    else:
        return False
            

def expired(d,m,yyyy, a_d, a_m, a_y): # para calcular si el producto está caducado según fecha

    if yyyy < a_yyyy: # False: bueno (no caducado) True: caducado
        return True
    elif yyyy == a_yyyy:
        if m < a_m:
            return True
        elif m == a_m:
            if d < a_d:
                return True 
    return False
        
arch = open('stock.txt', 'r', encoding= 'utf-8')
line = arch.readline().strip()
line = arch.readline().strip()

a_d = 15
a_m = 1
a_yyyy = 2025

highPrice = -111**9
nHighPrice = ''

contExpired = 0
total = 0

while line != '': 
    parts = line.split(',')
    if len(parts) == 10:
        product = parts[0]
        brand = parts[1]
        category = parts[2]
        price = float(parts[3])
        quantity = int(parts[4])
        expiration = parts[5].split('/')
        mm = int(expiration[0])
        dd = int(expiration[1])
        yyyy = int(expiration[2])
        weight = float(parts[6])
        organic = parts[7]
        originCountry = parts[8]
        barCode = int(parts[9])
        
        if price > highPrice:
            highPrice = price
            nHighPrice = f'{brand} {product}' # concatenar, así no utilizamos otra variable
        if expired(dd,mm,yyyy, a_d, a_m, a_yyyy): # ya que si está malo retorna True, entonces se ejecuta la condicion
            contExpired += quantity
            
            if impares(barCode): # si es verdadero
                percent = 0.5
                if esPrimo(int(weight)): # si es verdadero, vamos cambiando el porc de descuento 
                    percent = 0.8
                if organic == 'true':
                    percent = 0.2
                    
                print(f'{brand} {product} rebajó un {percent*100}% ($ {round((price*quantity*percent),2)}) ')
            else:
                print(f'{brand} {product} se regaló!')
            
        total += quantity
    line = arch.readline().strip()

expPercent = contExpired/total * 100

print('-'*20)
print(f'1) {nHighPrice} es el producto con mayor precio (${highPrice}) ')
print(f'2) {round(expPercent,2)}% de productos están caducados')
# vender los productos caducados al sig valor:
# si el valor entero de su peso es un numero primo: los venderemos al 80% de su valor
# si son productos orgánicos los venderemos al 20% de su valor
# si en el codigo de barra hay más numeros impares, se venderán a la mitad del precio, de lo contrario, se regalarán. 
# el último punto aplica antes que los dos primeros. 
    
