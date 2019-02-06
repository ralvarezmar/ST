#!/usr/bin/python -tt
# -*- coding: utf-8 -*-

import sys 
import os
import string
from os import listdir


def imprimir(fichero):
	lista=[]
	a=0

	for linea in fichero:	
		linea=linea.replace("\n","")
		if "/coches" in linea:
			print  "Marca\t", "Modelo\t", "Matricula"
			print "--------------------------"
		elif "Marca" in linea:	
			a=a+1
		elif "Modelo" in linea:
			a=a+1
		elif "Matricula" in linea:
			a=a+1		
		elif "\t" in linea:
			linea=linea.replace("\t","")
			lista.append(linea)	 
	a=0			
	while len(lista)>a:
		if len(lista)>a+2:
			print lista[a],"\t", lista[a+1],"\t",lista[a+2]
			a=a+3
		else:
			break
			
def main():

	if len(sys.argv) > 1:
		fichero=open(sys.argv[1],"r")	
	else:
		fichero=open(raw_input("Introduzca un nombre de fichero: "),"r")
	
	imprimir(fichero)

		
if __name__ == "__main__":
	main()		
