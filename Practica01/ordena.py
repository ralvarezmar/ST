#!/usr/bin/python -tt
# -*- coding: utf-8 -*-

import types
import argparse

lista=[]

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

def mostrar_linea(linea):
	valor= linea[:-1].split(",")
	valor= [int(i) for i in valor]
	lista.append(valor)


def main():
	usage = "%prog [opciones] origen destino"
	parser= argparse.ArgumentParser(description="Short sample app")
	parser.add_argument("-i" , "--input", action="store", dest="input", help="Leer el fichero")  
	parser.add_argument("-o" , "--output", action="store", dest="output", help="Escribir en el fichero")  
	
	args = parser.parse_args()

	if args.input:
		fichero=open(args.input,"r")
		for linea in fichero:
			mostrar_linea(linea)
		fichero.close()	
		print "Lista sin ordenar: ", lista
		lista.sort(mi_ordena) 	
		print "Lista ordenada: ", lista
			
		
	elif args.output:
		fichero=open(args.output,"w")
		#coger digitos introducidos y escribirlos 
		for i in range(1,5):
			n=raw_input("Introduzca una serie de numeros separados por comas: ")
			fichero.write(n+'\n')
		fichero.close()		
		print "Archivo guardado"	




if __name__ == "__main__":
	main()		
