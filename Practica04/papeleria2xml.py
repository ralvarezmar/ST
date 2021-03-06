#!/usr/bin/python -tt
# -*- coding: utf-8 -*-

import unicodedata
import json
import xml.etree.cElementTree as ET
def main():
	fichero=open("papeleria.txt","r")	
	root = ET.Element(u"papeleria")
	root.attrib={u"fecha":u"abril 2016"}
	root.text=u"Hola, mundo!"
	for linea in fichero:
		linea=json.loads(linea)	
	for componente in linea:
		claves=componente.keys()
		i=0
		while i<len(claves):	
			elemento=ET.SubElement(root, unicode(claves[i]))
			atributos={u"fecha":u"abril 2016"}
			elemento.attrib=atributos
			elemento.text=unicode(componente[claves[i]])
			i=i+1
	print ET.tostring(root, encoding="utf-8", method="xml")
				
if __name__ == "__main__":
	main()	

	
