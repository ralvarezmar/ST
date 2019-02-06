#!/usr/bin/python -tt
# -*- coding: utf-8 -*-
import requests,sys
import argparse
import json
usage = "%prog [opciones] origen destino"
parser= argparse.ArgumentParser(description="Short sample app")
parser.add_argument("-u" , "--users", action="store", dest="users", help="-u [usuario] para mostrar los mensajes de [usuario]") 
args = parser.parse_args()
i=1
url_comments="http://jsonplaceholder.typicode.com/posts"
url_users="http://jsonplaceholder.typicode.com/users"
comments=requests.get(url_comments)
users=requests.get(url_users)
if comments.status_code==200:
	c=comments.json()
	u=users.json()
	for comentario in c:
		ID=comentario["userId"]
		for usuario in u:
			if usuario["id"]==ID:
				if args.users:
						if args.users.lower()==usuario["username"].lower():
							i=0
							print "De:", usuario["username"]
							print comentario["title"]
							print "------------------------------"
							print comentario["body"], "\n"
				else:
					i=0
					print "De:", usuario["username"]
					print comentario["title"]
					print "--------------------------"
					print comentario["body"], "\n"

	if i==1:
		print "Usuario no existente"
else:
	print "error "+str(r.status_code)
#if args.users:
		
	

