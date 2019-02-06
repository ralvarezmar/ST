#!/usr/bin/python -tt
# -*- coding: utf-8 -*-

comunidades={"Madrid": ["Churros"], "Valencia": ["Naranjas"], "Asturias": ["Sidra","Fabada"]}
print comunidades
print comunidades["Madrid"]
comunidades["Extremadura"]=["Migas"]
print "-------------"
print comunidades
comunidades["Castilla La Mancha"]=["Pisto manchego"]
comunidades["Alicante"]=["Turron"]
print "-------------"
print comunidades
comunidades["Extremadura"].append("Torta del casar")
comunidades["Extremadura"].append("Vino")
print "-------------"
print comunidades

alcoholicas={"Vino", "Sidra", "cerveza"}
print "-------------------------------------------------"

i=0
j=0
for x in alcoholicas:
    while len(comunidades.values())>i:
        while len(comunidades.values()[i]) > j:
            if comunidades.values()[i][j] == x:               
                print "Borro ", x
                del (comunidades.values()[i][j])
            j=j+1
        j=0
        i=i+1
    i=0    

print comunidades


print "-------------------------------------------------"

comunidad_valenciana={"Valencia","Alicante","Castellon"}

for x in comunidades:
    for i in comunidad_valenciana:
        if i==x:
            comunidades[x].append("Paella")
            print "Añado paella"
print comunidades

print "-------------------------------------------------"

claves=comunidades.keys()
for clave in claves:
    for x in comunidad_valenciana:
        if clave == x:
            print "Borro ", x
            del comunidades[x]        
print comunidades

print "-------------------------------------------------"

def muestra_alfabetico(comunidades):
    claves=comunidades.keys()
    claves.sort()
    for clave in claves:
        print clave, " : ", " , ".join(comunidades[clave])
muestra_alfabetico(comunidades)

print "-------------------------------------------------"

def muestra_por_longitud(comunidades):
    claves=comunidades.keys()
    claves.sort()
    for clave in claves:
        print clave, ":", len(comunidades[clave]), " elemento/s"

muestra_por_longitud(comunidades)

