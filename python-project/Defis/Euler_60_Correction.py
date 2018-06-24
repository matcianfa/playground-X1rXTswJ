# Si vous trouvez une solution assez rapide pour ne pas obtenir un message d'erreur de temps, je serais très intéressé de la voir.

from functools import lru_cache

#  Ressortons de notre boite à outils la fonction qui permet de savoir si un nombre est premier (version mémoizée)
@lru_cache(maxsize=None)
def est_premier(n):
    global premiers_bis
    if n < 2 or n%2==0: return False
    for x in range(3, int(n**0.5) + 1,2):
        if n % x == 0:
            return False
    return True
    
# Ensemble des nombres premiers inférieurs à limite (pour gagner en vitesse lors de la recherche)
# On pourrait, pour aller plus vite, utiliser un crible d'Erathostene
limite = 10000 # Limite arbitraire pour notre recherche à modifier si besoin
premiers=set([ p for p in range(3,limite) if est_premier(p)])

somme_min=5*limite

# Fonction qui prend un entier, un ensemble et une liste des précédents nombres regardés et cherche ceux qui commutent dans l'ensemble avec l'entier
def chercher(p,ens,nb_precedents):
    global somme_min
    nb_precedents=nb_precedents+[p]
    somme = sum(nb_precedents)
    if somme <= somme_min : # Si on ne depasse pas la somme_min, alors on continue de chercher
        if len(nb_precedents)==5 : 
            somme_min=somme
        else :
            ens_commutant = set([])
            for q in ens:
                if q>p and est_premier(int(str(q)+str(p))) and est_premier(int(str(p)+str(q))) and somme+q < somme_min: # Si qp et pq sont premiers (au sens de la concaténation)
                    ens_commutant.add(q)
            for q in ens_commutant:
                chercher(q, ens_commutant, nb_precedents)
                
for p in premiers:
    chercher(p,premiers,[])
    
print(somme_min)
                    
    
