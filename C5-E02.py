# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 20:38:59 2025

@author: cata
"""
def esPrimo (num):
    if num <= 1:
        return False
    resto = 0
    for i in range(2, num): 
        if num%i == 0:
            resto += 1
    print(resto) # cantidad de divisores encontrados
    if resto > 0 : # ya que se podría dividir por otros numeros
        return False
    else:
        return True
    
# otra forma sin resto: 
def esPrimo2 (num):
    if num <= 1:
        return False
    for i in range(2, num): 
        if num % i == 0:
            return False # no se sigue ejecutando la funcion
    return True
    
x = 0
while x != -1:
    x = int(input('Ingresa un número para ver si el número es primo! (-1 para salir): '))
    print(esPrimo(x))

print(esPrimo2(5))
