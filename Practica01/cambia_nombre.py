#!/usr/bin/python -tt
# -*- coding: utf-8 -*-

import sys 
import os
import argparse
from os import listdir
import string 
import errno

def acciones(argumentos,args):
		
	char=argumentos			
	if args.recursive: 
		for x in os.walk("."):
			print x, "\n"	
	if args.spaces:
		char=char.replace(" ","_")
	if args.case:
		char=char.lower()
	if args.accent:
		if 'á' in char:
			char= char.replace("á","a")
		if 'é' in char:
			char=char.replace("é","e")		
		if 'í' in char:
			char=char.replace("í","i")
		if 'ó' in char:
			char= char.replace("ó","o")
		if 'ú' in char:
			char=char.replace("ú","u")
	if args.weird:
		trad= string.maketrans('!@|&%$ ', '.______')
		char= char.translate(trad)
	if args.enne:
		char= char.replace("ñ","nn")
	if (not args.enne and not args.weird and not args.spaces and not args.accent and not args.recursive):
		for letra in char:
			if letra>='A' and letra<='Z':
				char=char.lower()
				break
		if 'á' in char:
			char= char.replace("á","a")
		if 'é' in char:
			char=char.replace("é","e")		
		if 'í' in char:
			char=char.replace("í","i")
		if 'ó' in char:
			char= char.replace("ó","o")
		if 'ú' in char:
			char=char.replace("ú","u")
		if 'ñ' in char:
			char=char.replace("ñ","nn")
		if '@' or '|' or '&' or '%' or '$' in char:
			trad= string.maketrans('!@|&%$ ', '.______')
			char= char.translate(trad)		
		
	os.rename(argumentos,char)	
	print "Cambiada la carpeta a: ", char
	return char

def main():
	usage = "%prog [opciones] origen destino"
	parser= argparse.ArgumentParser(description="Short sample app")
	parser.add_argument("-r" , "--recursive", action="store_true", dest="recursive", help="Recorrer los directorios recursivamente")  
	parser.add_argument("-s" , "--spaces", action="store_true", dest="spaces", help="Reemplazar los espacios por barra baja")  
	parser.add_argument("-c" , "--case", action="store_true", dest="case", help="Reemplazar las mayusculas por minusculas")  
	parser.add_argument("-n" , "--enne", action="store_true", dest="enne", help="Reemplazar la eñe por otra combinacion de letras")  
	parser.add_argument("-t" , "--accent", action="store_true", dest="accent", help="Reemplazar las vocales con acento")  
	parser.add_argument("-w" , "--weird", action="store_true", dest="weird", help="Reemplazar los caracteres raros")
	if len(sys.argv) > 2:
		parser.add_argument("ficheros",help="lista de ficheros",metavar="N",nargs="+")
	
	args = parser.parse_args()

	if len(sys.argv) > 2:
		print sys.argv
		if args.ficheros:
			if os.path.exists(sys.argv[1]):
				print sys.argv[1]
				if os.path.isdir(sys.argv[1]):	
					print "Recibido directorio"
					acciones(sys.argv[1],args)
			else:
				print "Introduzca un directorio valido"
	else:
		print "Trabajamos en el directorio: ", os.getcwd()
		
		args = parser.parse_args()
		for carpeta in listdir("."):
			if os.path.isdir(carpeta):				
				acciones(carpeta,args)

	
if __name__ == "__main__":
	main()		
		 
		
	
	
