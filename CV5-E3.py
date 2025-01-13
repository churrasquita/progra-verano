# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 20:38:59 2025

@author: catal
"""

def esPrimo (num):
    cont = 0
    for i in range(1, num +1):
        if num%i == 0:
            cont += 1
    if cont > 2:
        return False
    else:
        return True
    
print(esPrimo(7)) # retorna True
print(esPrimo(6)) # retorna False
print(esPrimo(7351)) # retorna True

