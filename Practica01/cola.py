#!/usr/bin/python -tt
# -*- coding: utf-8 -*-

caja01=[]
caja02=[]
caja01.append("Eva")
caja02.append("Pepe")
caja01.append("Ernesto")
caja02.append("Manuel")
print "Caja 1"
print caja01
print "Caja 2"
print caja02
print "-------------------------------------------------"
print 
caja01.append("Juan")
caja02.append("Maria")
caja02.append("Miguel")
caja01.remove("Eva")
caja01.insert(0,"Javier")
print "-------------------------------------------------"
print "Caja 1"
print caja01
print "Caja 2"
print caja02
print  
print "-------------------------------------------------"
caja03=[]
caja03.append(caja02[1])
caja03.append(caja02[3])
print "Caja 3"
print caja03
print "-------------------------------------------------"
caja02.reverse()
print "Caja 2"
print caja02
print
print "-------------------------------------------------"
if "Ernesto" in caja01:	
	caja01.remove("Ernesto")	
	caja01.insert(0,"Ernesto")
	#numero=caja01.index("Ernesto")
	#caja01.insert(0,caja01[numero])
print "Caja 1"
print caja01

print "-------------------------------------------------"
linea_de_cajas= (caja01,caja02,caja03)

print "Linea de Cajas"
print linea_de_cajas

print "-------------------------------------------------"
for x in linea_de_cajas:
	print "Caja con ", len(x), " clientes: ", x

print "-------------------------------------------------"	
linea_de_cajas= caja01+caja02+caja03
print "Linea de cajas como lista: "
print " ; ".join(linea_de_cajas)
	



	


