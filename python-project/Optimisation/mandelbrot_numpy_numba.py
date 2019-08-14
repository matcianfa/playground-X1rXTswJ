from time import time
from random import random
import numpy as np
from numba import jit,  guvectorize, complex128, int8, int32

#---------------------   Les constantes 

X_MIN,Y_MIN,X_MAX,Y_MAX = -2,-1,1,1 # Valeurs min et max pour les parties reelles et imaginaires
MAX_ITER = 500 # Le nombre d'itérations maximum avant de considérer que la suite ne diverge pas vers l'infini
NB_POINTS = 1000000 # Nombres de points aléatoires choisis pour la méthode de Monte Carlo

#---------------------   Les fonctions

@jit(int8(complex128),nopython=True)
def mandelbrot(c):
    """
    Renvoie 0 si la suite diverge avant MAX_ITER itérations et 1 sinon.
    Permet de compter les points de non divergence vers l'infini.
    """
    z = 0
    for n in range(MAX_ITER):
        z = z*z + c
        if abs(z) > 2 : return 0
    return 1
    
@guvectorize([(complex128[:], int8[:])], '(n)->(n)',target='parallel')
def mandelbrot_vectorise(c, output):
    for i in range(c.shape[0]):
        output[i] = mandelbrot(c[i])
      
 
def monte_carlo():
    """
    Compte le nombre de points dans l'ensemble de Mandelbrot
    """
    # On crée notre tableau de nombres complexes C
    X = (X_MAX-X_MIN)*np.random.random(NB_POINTS)+X_MIN  
    Y = (Y_MAX-Y_MIN)*np.random.random(NB_POINTS)+Y_MIN
    C = X + Y*1j
    # On renvoie la somme des éléments du tableau renvoyé par mandelbrot(C)
    return mandelbrot_vectorise(C.astype(np.complex128)).sum()
    
#----------------------   Execution

if __name__ == "__main__" :
    t0=time()
    aire = monte_carlo()*(X_MAX-X_MIN)*(Y_MAX-Y_MIN)/NB_POINTS # L'aire de la courbe est la proportion de points * aire totale du rectangle
    print("L'aire obtenue est {}".format(aire))
    print("Le temps de calcul est de {} s".format(time()-t0))
