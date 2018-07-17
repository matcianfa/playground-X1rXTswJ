# L'idée est de chercher les puissances de sommes de chiffres possibles par tranche de nombre de chiffres puis regarder ceux qui sont effectivement somme de leurs chiffres

from math import log

# indice du nombre qu'on cherche (30 dans l'énoncé
long_max=30

# Fonction qui donne la somme des chiffres d'un nombre
# Par le calcul car c'est plus rapide qu'en passant par les chaines de caractère
def somme_chiffres(n):
    if n<10 : return n
    return n%10+somme_chiffres(n//10)
    
# Fonction mémoizée qui donne le log(10)/log(k)
def log_memo(k): return log(10)/log(k)
    
# Fonction qui cherche
def chercher():
    liste=[] #liste des nombres égaux à une puissance de leur somme de chiffres
    nb_chiffres=2 #On commence avec 2 chiffres
    while len(liste)<long_max : # Tant qu'on a pas trouvé long_max nombres qui marchent : 
        for s in range(2,9*nb_chiffres+1): # on teste pour toutes les sommes de chiffres possibles donc de 2 à 9*nombre de chiffres
            temp=log_memo(s)
            for exposant in range(int(temp*(nb_chiffres-1))+1,int(temp*nb_chiffres)+1):
                n=s**exposant
                if somme_chiffres(n)==s : 
                    liste.append(n)
        nb_chiffres+=1
    liste.sort()
    return liste[long_max-1]
    
    
print(chercher())
