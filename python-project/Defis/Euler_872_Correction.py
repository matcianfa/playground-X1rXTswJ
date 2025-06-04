# ProjectEuler 872

import math
from time import time
from numba import njit

# @njit("int64(int32)")
def resoudre_euler_872(n,k):
    """
    On remarque que se déplacer dans l'arbre revient à utiliser l'écriture binaire de n-k
    """
    reponse = n
    bin_n_k = bin(n-k)[2::]
    bin_n_k = bin_n_k[::-1] # On renverse
    puiss_2 =1
    valeur_noeud = n
    for bit in bin_n_k :
        if bit == "1":
            valeur_noeud -= puiss_2
            reponse += valeur_noeud
        puiss_2 *=2
    return reponse


t0 = time()
sol =resoudre_euler_872(10**17,9**17)
print(f"La solution est {sol}")
print(f"Temps mis : {time()-t0}")
