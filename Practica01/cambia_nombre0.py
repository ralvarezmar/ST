#!/usr/bin/python -tt
# -*- coding: utf-8 -*-

import sys 
import os
import string
from os import listdir

def cambia_nombre(argumentos):	
	char=argumentos		
	i=0
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

	while os.path.exists(char):
		char=char+str(i)

	os.rename(argumentos,char)
	print "Cambiado el directorio a: ", char
	
i=0
if len(sys.argv) >= 2:
	print "La cadena tiene", len(sys.argv), "argumentos" 
	for argumentos in sys.argv:
		if os.path.exists(argumentos):
			print "Recibido directorio", argumentos
			if os.path.isdir(argumentos):					
				cambia_nombre(argumentos)

		else:
			sys.exit("Introduzca un directorio valido");
			raise SystemExit 			
else:
	print "Solo introducido un argumento: ", os.getcwd()
	#argumentos=os.getcwd()
	for carpeta in listdir("."):
		if os.path.isdir(carpeta):
			cambia_nombre(carpeta)
		

	
		
		 
		
	
	
