# @lru_cache(maxsize=None) avant une fonction permet de sauvegarder automatiquement les valeurs déjà calculées de cette fonction... Très très pratique!
from functools import lru_cache

# Essayons de trouver la réponse grace à une fonction récursive
# nombre_chemins donne le nombre de chemins de (0,0) jusqu'à (ligne,colonne)
@lru_cache(maxsize=None)
def nombre_chemins(ligne,colonne):
    if ligne == 0 : #Si on est en haut, on ne peut aller qu'horizontalement donc il n'y a qu'un chemin
        return 1
    if colonne == 0 : # Si on est à gauche, on ne peut qu'aller verticalement donc il n'y a qu'un chemin
        return 1
    # Pour arriver à un point, on vient soit d'au-dessus soit de la gauche d'où :
    return nombre_chemins(ligne-1,colonne) + nombre_chemins(ligne,colonne-1)

print(nombre_chemins(20,20))
