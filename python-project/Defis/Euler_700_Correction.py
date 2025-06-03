# ProjectEuler 700

import math
from time import time
from numba import njit
import numpy as np

limite_methode = 11714782

@njit("int64()")
def resoudre_euler_700_partiel_1():
    """
    On cherche les eulercoins en itérant les premiers cas. Comme c'est trop long,
    quand on a trouvé un nombre relativement bas ( stocké dans limite_methode )
    On calcule le reste avec l'autre méthode
    """
    a = 1504170715041707
    b = 4503599627370517
    reponse = a
    resultat = a
    eulercoin_prec =a
    while resultat != limite_methode :
        resultat = (resultat+a)%b
        if resultat<eulercoin_prec :
            print(resultat)
            eulercoin_prec = resultat
            reponse += resultat
    return reponse

@njit("int64()")
def resoudre_euler_700_partiel_2():
    """
    Calcule tous les n correspondants (en multipliant par l'inverse de a modulo b) aux nombres inférieurs à limite_methode
    ce qui permet de les classer dans l'ordre d'apparition
    puis on ne garde que ceux qui sont plus petits que le précédent eulercoin
    """
    reponse = 0
    liste_n_k = []
    inverse_a = 3451657199285664
    b = 4503599627370517
    for k in range(1,limite_methode):
        liste_n_k.append(((k*inverse_a)%b,k))
    liste_n_k.sort()

    # On cherche les eulercoins
    eulercoin_en_cours = limite_methode
    for (n,k) in liste_n_k:
        if k < eulercoin_en_cours :
            eulercoin_en_cours = k
            reponse += k
    return reponse




t0 = time()
sol =resoudre_euler_700_partiel_1()
print(f"La solution est {sol}")
print(f"Temps mis : {time()-t0}")

t0 = time()
sol2 =resoudre_euler_700_partiel_2()
print(f"La solution est {sol2}")
print(f"Temps mis : {time()-t0}")

print(f"La solution finale est {sol + sol2}")
