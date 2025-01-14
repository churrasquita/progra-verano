# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 20:38:59 2025

@author: cata
"""
def esPrimo (num):
    if num == 0 or num == 1:
        return False
    cont = 0
    for i in range(1, num +1):
        if num%i == 0:
            cont += 1
    if cont > 2:
        return False
    else:
        return True
    
x = 0
while x != -1:
    x = int(input('Ingresa un número para ver si el número es primo!: '))
    print(esPrimo(x))
