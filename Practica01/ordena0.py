#!/usr/bin/python -tt
# -*- coding: utf-8 -*-

import types
lista = [[1,3],[5,1,8],[5],[0],[2,2,2],[2,4]]
print "Lista sin ordenar: ", lista
def mi_ordena(a,b):
	suma_a=0
	suma_b=0
	for x in a:
		if type(x) == types.IntType: 
			suma_a=suma_a+x
		else:
			print "Caracter no permitido"
			raise SystemExit			
	for i in b:
		if type(i) == types.IntType: 
			suma_b=suma_b+i
		else:			
			print "Caracter no permitido"
			raise SystemExit
	if suma_a>suma_b:
		return 1
	elif suma_a<suma_b:
		return -1
	else:
		if len(a)>len(b):
			return 1
		elif len(a)<len(b):
			return -1
		else:
			return 0
		

lista.sort(mi_ordena) 
print "Lista ordenada: ", lista
