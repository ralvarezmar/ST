#!/usr/bin/python -tt
# -*- coding: utf-8 -*-

import json

inflacion=3


def main():
	fichero=open(raw_input("Introduzca un nombre de fichero: "),"r")	
	for linea in fichero:
		linea=json.loads(linea)
	for elemento in linea:
		claves=elemento.keys()
		elemento[claves[2]]=elemento[claves[2]]*(1+inflacion*0.01)
		print json.dumps(elemento)
			
if __name__ == "__main__":
	main()		
