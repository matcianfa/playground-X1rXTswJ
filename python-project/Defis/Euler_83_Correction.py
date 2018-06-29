# On va cette fois ci utiliser une technique générale pour ce genre de problème en mettant en place l'algorithme de Djikstra qui pouvait marcher pour les problèmes précédents aussi.


from math import inf
import heapq as hq # Pour gagner du temps dans la gestion de la liste des points à regarder (Voir sur internet Heap Queue)

matrice= # A Copier Coller

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
        if ligne>0: 
            graphe[(ligne,colonne)][1].append((ligne-1,colonne))
        # Regardons enfin tous les déplacements vers le bas : 
        if ligne<N-1 :
            graphe[(ligne,colonne)][1].append((ligne+1,colonne))
        # Regardons déjà tous les déplacements à gauche : 
        if colonne>0 :
            graphe[(ligne,colonne)][1].append((ligne,colonne-1))
            
somme_min=inf

# Parcourons à présent notre graphe en utilisant l'algorithme de Djisktra :
def chercher():
    open_l=[(graphe[(0,0)][0],(0,0))] # La liste des points à regarder sous la forme (valeur, point) pour que le classement se fasse automatiquement du plus petit au plus grand avec la heap queue
    hq.heapify(open_l)
    closed_l=set([]) # Ensemble des points déjà considérés et donc à ne plus étudier
    while open_l:
        (val,point)=hq.heappop(open_l) 
        if point==(N-1,N-1) : # Si on est arrivé au point final 
            return val
        for suivant in graphe[point][1]:
            if suivant not in closed_l : # On ne considère plus les points qu'on a déjà évalué avec leur plus court chemin
                hq.heappush(open_l,(val+graphe[suivant][0],suivant))
        closed_l.add(point)
    return [] # Au cas ou le graphe ne mène pas à la fin
    
print(chercher())
