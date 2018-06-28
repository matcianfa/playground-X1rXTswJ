# Etant donné que le problème suivant tourne autour de la même idée, on va directement chercher une solution générale sans chercher d'astuces de calcul comme pour le problème précédent.
# On va donc créer un graphe dont les sommets sont les coordonnées des points et les fléches pondérées par le nombre qu'il faut ajouter pour aller de ce sommet à un autre (et rien quand on ne peut pas y aller)

from math import inf
from functools import lru_cache

matrice= # A copier coller

N=len(matrice)

# graphe sous forme de dictionnaire
graphe={}

# Création du graphe sous la forme (ligne, colonne) -> (valeur, [liste des points accessibles])
for ligne in range(N):
    for colonne in range(N):
        graphe[(ligne,colonne)]=(matrice[ligne][colonne],[])
        # Regardons déjà tous les déplacements à droite : 
        if colonne<N-1 :
            graphe[(ligne,colonne)][1].append((ligne,colonne+1))
        # Regardons maintenant tous les déplacements vers le haut : 
        if ligne>0 and 0<colonne<N-1: # C'est abérrant de monter ou descendre au debut ou à la fin
            graphe[(ligne,colonne)][1].append((ligne-1,colonne))
        # Regardons enfin tous les déplacements vers le bas : 
        if ligne<N-1 and 0<colonne<N-1 :
            graphe[(ligne,colonne)][1].append((ligne+1,colonne))
            
somme_min=inf

# Parcourons à présent notre graphe : 
# Précédent est la pour éviter les aller retour en boucle infinie
# On mémoize pour gagner énoooooooormément de temps
@lru_cache(maxsize=None)
def parcourir(point,précédent=(-1,-1)):
    ligne,colonne=point
    if colonne==N-1:
        return graphe[point][0]
    somme=inf
    for suivant in graphe[point][1]:
        if suivant!=précédent:
            somme=min(somme,parcourir(suivant,point))
    return somme+ graphe[point][0]
    
print(min([ parcourir((ligne,0)) for ligne in range(N)]))
