# On va utiliser la fonction permutations
from itertools import permutations

#  Ressortons de notre boite à outils la fonction qui permet de savoir si un nombre est premier
def est_premier(n):
    if n < 2 or n%2==0: return False
    for x in range(3, int(n**0.5) + 1,2):
        if n % x == 0:
            return False
    return True

# On met dans une fonction pour aller plus vite
def chercher():
    for n in range(1000,10000):
        if n==1487 : continue # Il faut trouver l'autre
        if est_premier(n):
            liste_permutations = [] # On va créer une liste des permutations de n plus grandes que n et qui sont des nombres premiers
            for perm in permutations(str(n)):
                perm = int("".join(perm))
                if perm>n and est_premier(perm): # On ne garde que les permutations plus grandes et première.
                    liste_permutations.append(perm)
            if len(liste_permutations)>1 :
                for k in liste_permutations : 
                    if k + (k-n) in liste_permutations :
                        return str(n)+str(k)+str(2*k-n)
                        
print(chercher())
