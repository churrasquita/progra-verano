# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 17:06:55 2025

@author: catal
"""

def entre (v1, v2, proceso):
    if proceso == 'suma':
        resultado = 0
    elif proceso == 'multiplicacion':
        resultado = 1
    for i in range(v1, v2 +1):
        if proceso == 'suma':
            resultado += i
        elif proceso == 'multiplicacion':
            resultado *= i
    return resultado

print(entre(1, 3, "suma")) # retorna 6
print(entre(3, 5, "suma")) # retorna 12
print(entre(1, 2, "multiplicacion")) # retorna 2
print(entre(5, 8, "multiplicacion")) 
