# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 00:39:25 2025

@author: bruno
"""

print("-------Menú-------")
print("Elige un filtro o fin para terminar")
choice = input("(T) Tipo (S) Sumergible (FIN): ")

total = 0 # para ir acumulando el total de los relojes

while choice.upper() != "FIN":
    while choice.upper()!="T" and choice.upper()!="S" and choice.upper()!="FIN":
        choice = input("(T) Tipo (S) Sumergible (FIN): ")
        if choice.upper()=="FIN":
            break
        
    # UNA VEZ SELECCIONADA LA OPCION LEEMOS EL ARCHIVO, YA QUE ES LA QUE NOS INDICA EL FILTRO
    if choice.upper()=="T":
        opt = input("(A) Analógico (D) Digital (AD) Ambos: ")
        #LEEMOS ARCHIVO Y BUSCAMOS SEGÚN PARÁMETRO OPT
        file = open("relojes.txt",encoding="utf-8")
        line = file.readline().strip()
       
        while line != "":
            p = line.split(",")
            posicion = int(p[0]) #QUEREMOS GUARDAR ESTO COMO UN ENTERO INMEDIATAMENTE
            nombre = p[1]
            precio = p[2]
            tipo = p[3]
            
            if (opt.upper() == "A" and tipo == "Analógico") or (opt.upper() == "D" and tipo == "Digital") or (opt.upper() == "AD" and tipo =="Analógico/Digital") :
                print(f"   {posicion} {nombre} {precio}")
                
            line = file.readline().strip()
            
        
    if choice.upper()=="S":
        opt = input("(S) Sumergible (N) No Sumergible: ")
        #LEEMOS ARCHIVO Y BUSCAMOS SEGÚN PARÁMETRO OPT
        file = open("relojes.txt",encoding="utf-8")
        line = file.readline().strip()
        
        while line != "":
            p = line.split(",")
            posicion = int(p[0]) #QUEREMOS GUARDAR ESTO COMO UN ENTERO INMEDIATAMENTE
            nombre = p[1]
            precio = p[2]
            sumergible = p[4]
            
            if (opt.upper() == "S" and sumergible == "Sí") or (opt.upper() == "N" and sumergible == "No"):
                print(f"   {posicion} {nombre} {precio}")
                
            line = file.readline().strip()
            
        
        
    #CUAL QUIERO COMPRAR, PREGUNTO
    compra = int(input("Seleccione número de reloj a comprar: "))
    
    file = open("relojes.txt",encoding="utf-8")
    line = file.readline().strip()
    while line != "":
        
        
        p = line.split(",")
        numero = int(p[0])
        nombre = p[1]
        precio = int(p[2])
        
        if numero == compra: # ya que las posiciones no se repiten, no es necesaria otra condicion
            print(f"COMPRADO {numero} {nombre} {precio}")
            total = total + precio 
            break # se deja de leer el archivo
        
        line = file.readline().strip()
    
    print("-------Menú-------")
    print("Elige un filtro o fin para terminar")
    choice = input("(T) Tipo (S) Sumergible (FIN): ") # para que se reinicie el ciclo
        
print(f"Total recaudado: ${total}")
