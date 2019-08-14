from time import time
from random import random
import numpy as np

#---------------------   Les constantes 

X_MIN,Y_MIN,X_MAX,Y_MAX = -2,-1,1,1 # Valeurs min et max pour les parties reelles et imaginaires
MAX_ITER = 500 # Le nombre d'itérations maximum avant de considérer que la suite ne diverge pas vers l'infini
NB_POINTS = 1000000 # Nombres de points aléatoires choisis pour la méthode de Monte Carlo

#---------------------   Les fonctions

    
def mandelbrot(c):
    """
    Version Numpy 
    Prend en entrée une np.array de valeurs de c
    Renvoie une np.array composée 0 si la suite diverge avant MAX_ITER itérations et 1 sinon.
    """
    resultats = np.zeros(c.shape) # On initialise à 0.
    z = np.zeros(c.shape, dtype = np.complex64) # On initialise les z
    p = np.abs(c-0.25)
    cardioide = (c.real < p - 2*p*p + 0.25) | ((c.real+1)**2 + c.imag**2 < 0.0625) # Pour garder en mémoire les éléments dans la cardioide
    resultats[cardioide]=1 # Les points de la cardioides et du cercles sont sur l'ensemble de Mandelbrot
    pas_fini =  ~(cardioide) # Un tableau pour savoir pour quels indices il y a encore des calculs à faire. Initialisation à True sauf pour les c qui sont dans la cardioide ou le cercle.
    for n in range(MAX_ITER):
        # Pour éviter de calculer pour tous les z, on cherche ceux qui ont encore un module inférieur à 2
        pas_fini = pas_fini & (np.abs(z)< 2)
        z[pas_fini] = z[pas_fini]**2 + c[pas_fini] # On ne calcule que pour les indices où il y a encore des calculs à faire (indiqué par la tableau pas_fini)
    resultats[pas_fini] = 1 # Si pas fini c'est qu'on est dans l'ensemble de Mandelbrot
    return resultats
      
    
def monte_carlo():
    """
    Compte le nombre de points dans l'ensemble de Mandelbrot
    """
    # On crée notre tableau de nombres complexes C
    X = (X_MAX-X_MIN)*np.random.random(NB_POINTS)+X_MIN  
    Y = (Y_MAX-Y_MIN)*np.random.random(NB_POINTS)+Y_MIN
    C = X + Y*1j
    # On renvoie la somme des éléments du tableau renvoyé par mandelbrot(C)
    return mandelbrot(C).sum()
    
#----------------------   Execution

if __name__ == "__main__" :
    t0=time()
    aire = monte_carlo()*(X_MAX-X_MIN)*(Y_MAX-Y_MIN)/NB_POINTS # L'aire de la courbe est la proportion de points * aire totale du rectangle
    print("L'aire obtenue est {}".format(aire))
    print("Le temps de calcul est de {} s".format(time()-t0))
