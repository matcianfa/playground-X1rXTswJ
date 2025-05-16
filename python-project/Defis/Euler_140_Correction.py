# ProjectEuler 140

import math
from time import time


def resoudre_euler_140(N):
    compteur = 0
    solution = 0
    n = 1
    n_precedent = 1
    while compteur<N :
        delta = 5*n*n+14*n+1
        r = math.isqrt(delta)
        if r*r == delta :
            solution += n
            compteur += 1

            print(f"{compteur} : {n}    q = {n/n_precedent}")
            n_precedent = n
            # On remarque que les quotients des réponses convergent rapidement vers des valeurs donc on en profite pour gagner en rapidité
            if compteur%2 == 1:
                n = int(n*1.9387489019)
            else :
                n = int(n*3.5353221)
        n += 1
    return solution

t0 = time()
print(resoudre_euler_140(30))
print(f"Temps mis : {time()-t0}")
