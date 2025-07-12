# ProjectEuler 885

import math
from time import time
from numba import njit
import numpy as np
from itertools import combinations_with_replacement



# @njit("int64(int64[:],int32)")
def resoudre_euler_885(n):
    """
    Pour chaque nombre rangé, on le multiplie par le nombre de permutations possibles (c'est une anagramme) et on somme
    """
    reponse = 0
    fact_n = math.factorial(n)
    for combi in combinations_with_replacement("0123456789",n):
        # on calcule le produit des factorielles du nombre d'apparitions de chaque nombre
        produit_fact = 1
        facteur = 1
        for i in range(n-1):
            if combi[i] == combi[i+1]:
                facteur += 1
            else :
                facteur = 1
            produit_fact *= facteur

        reponse = (reponse + int("".join(combi))*fact_n//produit_fact)%1123455689

    return reponse


t0 = time()
sol = resoudre_euler_885(18)
print(f"La solution est {sol}")
print(f"Temps mis : {time()-t0}")
