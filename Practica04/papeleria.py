#!/usr/bin/python -tt
# -*- coding: utf-8 -*-

import json

def main():
	fichero=open("papeleria.txt","r")	
	for linea in fichero:
		linea=json.loads(linea)	
	print "Ref.\tPrecio\tDescripcion"
	print "----------------------------"
	for elemento in linea:
		claves=elemento.keys()
		print elemento[claves[1]],"\t",elemento[claves[2]],"\t",elemento[claves[0]]
			
if __name__ == "__main__":
	main()		
