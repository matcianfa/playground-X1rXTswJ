from random import randint

premier_choix=0

def mon_programme(numéro):
    global premier_choix
    if numéro==0 : 
        premier_choix=randint(1,3)
        return premier_choix
    else:
        return [n for n in range(1,4) if n!=premier_choix and n!= numéro][0]
   
