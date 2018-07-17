# L'idée est simple : 
# -On découpe "123456789" en laissant les chiffres dans leur ordre d'apparition donc par exemple un découpage de la forme ["2","5","47","89","631"]
# -Puis on compte sur chaque ensemble de chiffres le nombre de nombres premiers qu'on peut former et on multiplie ces nombres pour savoir combien d'ensembles avec que des nombres premiers on peut former. Pour notre exemple : "2", "5", "47" et "89" on ne peut former qu'un nombre premier avec ces chiffres et avec "631", on peut en former 3 : 631, 613 et 163. Donc en tout on pourra former 3 ensembles composés que de nombres premiers comme le veut l'énoncé.


from functools import lru_cache
from itertools import permutations

# fonction qui dit si un nombre est premier ou pas 
# Version un peu améliorée en remarquant qu'un nombre premier ne peut être que de la forme 6k-1 ou 6k+1 (à part pour 2 et 3). donc on teste si n est divisible par les nombres de cette forme la uniquement
@lru_cache(maxsize=None)
def est_premier(n):
    if n==2 or n==3 : return True
    if n==0 or n==1 or n%2==0 or n%3==0: return False
    k=5
    while k*k<=n :
        if n%k==0 : return False
        k+=2
        if n%k==0 : return False
        k+=4
    return True
    
# Fonction qui donne l'ensemble des façons de couper 123456789
# Pour les créer, on part de ["1"] 
# Puis on ajoute "2" soit à 1, soit à part. On a donc 2 ensembles ["12"] et ["1","2"].
# Puis on rajoute le 3 : Pour chaque ensemble précédent, soit on le rajoute à un des éléments présents soit à part ce qui donne ['123'], ['12', '3'], ['13', '2'], ['1', '23'], ['1', '2', '3']
# etc.
def couper(n="123456789",liste=[]):
    if n=="" : return liste
    chiffre=n[0]
    if chiffre == "1" : 
        liste.append(["1"])
        return couper(n[1:],liste)
    liste_temp=[]
    for ens in liste: #On prend une liste de début de découpage avec les valeurs de 1 à chiffre-1
        for i,el in enumerate(ens): # le nouveau chiffre on l'ajoute soit au premier élément, soit au second...
            ens_temp=ens.copy()
            ens_temp[i]=el+chiffre
            liste_temp.append(ens_temp)
        # soit on le rajoute à part
        liste_temp.append(ens+[chiffre])
    return couper(n[1:],liste_temp)    

# Fonction qui pour un découpage de 123456789, regarde le nombre de nombres premiers qu'on peut former avec chaque nombre du découpage et on multiplie ces nombres pour obtenir le nombre d'ensemble dont tous les nombres sont premiers à partir de ce découpage.
def compter(decoupage):
    produit=1
    for chiffres in decoupage:
        somme=0 # On compte le nombre de nombres premiers qu'on peut former avec ces chiffres
        for perm in permutations(chiffres):
            n=int("".join(perm))
            if est_premier(n): 
                somme +=1
        if somme==0 : # Si on ne peut former aucun nombre premier avec ces chiffres, ca ne sert à rien de chercher pour le reste
            return 0
        else : # Sinon on les compte
            produit*=somme
    return produit
            
# Fonction qui cherche sur l'ensemble des permutations
def chercher():
    somme=0
    for decoupage in couper():
        somme+=compter(decoupage)
    return(somme)
    
print(chercher())
