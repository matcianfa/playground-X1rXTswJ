from time import time
from random import random
from numba import jit

#---------------------   Les constantes 

X_MIN,Y_MIN,X_MAX,Y_MAX = -2,-1,1,1 # Valeurs min et max pour les parties reelles et imaginaires
MAX_ITER = 500 # Le nombre d'itérations maximum avant de considérer que la suite ne diverge pas vers l'infini
NB_POINTS = 1000000 # Nombres de points aléatoires choisis pour la méthode de Monte Carlo

#---------------------   Les fonctions
@jit
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

@jit    
def monte_carlo():
    """
    Compte le nombre de points dans l'ensemble de Mandelbrot
    """
    compteur = 0 # Pour compter le nombre de points dans l'ensemble de Mandelbrot
    for i in range(NB_POINTS):
        c = complex((X_MAX-X_MIN)*random()+X_MIN ,(Y_MAX-Y_MIN)*random()+Y_MIN) # On choisit un nombre complexe aléatoire dont la partie réelle est entre X_MIN et X_MAX et la partie imaginaire entre Y_MIN et Y_MAX
        compteur += mandelbrot(c)
    return compteur
    
#----------------------   Execution

if __name__ == "__main__" :
    t0=time()
    aire = monte_carlo()*(X_MAX-X_MIN)*(Y_MAX-Y_MIN)/NB_POINTS # L'aire de la courbe est la proportion de points * aire totale du rectangle
    print("L'aire obtenue est {}".format(aire))
    print("Le temps de calcul est de {} s".format(time()-t0))
