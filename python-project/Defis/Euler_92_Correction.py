# Rien de particulier dans la méthode... on fait ce qui est demandé
# Sauf qu'il faut grapiller à droite à gauche pour gagner en vitesse pour passer le test du temps
# D'où la mémoization, le calcul des carrés par des méthodes arithmétiques et non pas le passage en string qui est plus court à rédiger...

from functools import lru_cache

liste_carrés= [x**2 for x in range(10)]

# Fonction qui calcule la somme des carrés des chiffres :
def carrés(number):
    total = 0
    while number:
        total += liste_carrés[(number % 10)]
        number //= 10
    return total
    
#Fonction qui prend en entrée un nombre et qui renvoie Vrai si la chaine fini par 89 et Faux sinon
# On mémoize pour gagner en temps
@lru_cache(maxsize=None)
def limite(n):
    if n==1: return False
    if n==89 : return True
    return limite(carrés(n))
    
# On met dans une fonction pour gagner en vitesse
def chercher():
    somme=0
    for n in range(1,10**7+1):
        if limite(n): somme+=1
    return somme
    
print(chercher())
