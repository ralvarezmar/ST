#!/usr/bin/python -tt
# -*- coding: utf-8 -*-

def redondea_nota(nota, modo):
    if modo =="laxo":
        if nota < 4:
            return "suspenso"
        if nota < 6:
            return "aprobado"
        if nota > 8:
            return "notable"
        if nota > 9:
            return "matricula de honor"
    elif modo == "estricto":
        if nota < 5:
            return "suspenso"
        if nota < 8:
            return "aprobado"
        if nota < 9:
            return "notable"
        if nota > 9:
            return " sobresaliente"
    elif modo == "normal":
        if nota < 5:
            return "suspenso"
        if nota < 6:
            return "aprobado"
        if nota < 9:
            return "notable"
        if nota > 9:
            return " sobresaliente"

print "nota = 5", redondea_nota(5,"normal")
print "nota = 4", redondea_nota(4,"estricto")
print "nota = 9", redondea_nota(9,"laxo")
        
    
