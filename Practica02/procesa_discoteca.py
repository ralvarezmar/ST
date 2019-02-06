#!/usr/bin/python -tt
# -*- coding: utf-8 -*-

import sys 
import os
import string
from os import listdir

def imprimir(fichero):
	disco=[]
	canciones=[]
	a=0
	b=0
	for linea in fichero.readlines():
		if "discoteca" in linea:
			a=0
		elif "\t\t\t\t<" in linea:
			a=3
		elif "\t\t\t<" in linea:
			a=2
		elif "\t\t<" in linea:
			a=1 
		elif "\t<" in linea:
			a=0
			b=b+1
		elif "\t" in linea:
			linea=linea.replace("\t","")
			linea=linea.replace("\n","")
			if a==0:	
				disco.append(linea)
			if a==1:
				disco.append(linea)
			if a==2:
				if b%3==0:
					canciones.append("\n")
					canciones.append(linea)
				else:
					canciones.append(linea)
			if a==3:
				canciones.append(linea)
	b=0
	a=0
	while len(disco)>b:
		if len(disco)>b+2:
			print disco[b]," / ", disco[b+1]
			print "-------------------------"
			b=b+2
		else:
			break
		while len(canciones)>a:
			if "\n" in canciones[a]:
				break				 
			else:
				print canciones[a], canciones[a+1]
				a=a+2
	
	while len(canciones)>a:
		if "\n" in canciones[a]:
			canciones.remove("\n")
		else:
			print canciones[a], canciones[a+1]
			a=a+2
def main():

	if len(sys.argv) > 1:
		fichero=open(sys.argv[1],"r")	
	else:
		fichero=open(raw_input("Introduzca un nombre de fichero: "),"r")
	
	imprimir(fichero)

		
if __name__ == "__main__":
	main()		
