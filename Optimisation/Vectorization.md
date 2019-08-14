# Exemple de vectorisation : Aire de l'ensemble de Mandelbrot

Le but de cette page est de présenter sur un exemple un aspect propre à python : La vectorisation. En effet, python a de nombreux avantages mais en contrepartie, c'est un langage qui est très lent (sur les boucles par exemple). Cependant de nombreux modules, pour gagner en rapidité, sont programmés directement dans un autre langage (le C). C'est le cas du module `numpy` qui permet, entre autres, des calculs sur des vecteurs/tableaux très rapides. On appelle donc vectorisation le fait d'utiliser des vecteurs (arrays) Numpy pour éviter un maximum de boucles python.

Une fois cette vectorisation faite, on utilisera le module Numba qui permet d'accélérer encore davantage les calculs. 

Cette page est une simple présentation sans exercice. Il suffira de valider pour voir le résultat. Vous pouvez bien sûr modifier ces exemples pour voir ce que donnent vos modifications. Les constantes seront toujours les mêmes pour bien voir le gain en rapidité. vous pourrez donc les modifier pour affiner la précision du résultat.


## Présentation de l'exemple : Calcul de l'aire de l'ensemble de Mandelbrot

On peut trouver une présentation de l'ensemble de Mandelbrot sur [Wikipédia](https://fr.wikipedia.org/wiki/Ensemble_de_Mandelbrot) très complète. Une remarque : une [page](https://tech.io/playgrounds/17176/recueil-dexercices-pour-apprendre-python-au-lycee/ensembles-de-mandelbrot-et-julia) est dédiée dans ce recueil sur les ensembles de Mandelbrot et Julia mais avec une définition un peu différente et moins classique. Nous revenons ici à la définition à partir de la fonction $`f(z)=z^2+c`$.

Résumons la définition de l'ensemble de Mandelbrot : Un complexe $`c`$ est dans l'ensemble de Mandelbrot si et seulement si la suite définie par $`z_0=0`$ et $`z_{n+1} = z_n^2+c`$ ne tend pas vers l'infini. Voici sa représentation : ![Figure](outputNB.png)

Pour déterminer son aire, nous allons utiliser une méthode dite de Monte Carlo : Prendre des points au hasard dans le rectangle $`-2\leq x \leq 1`$ et $`-1\leq y \leq 1`$ et compter le nombre de points qui font partie de l'ensemble de Mandelbrot. On peut trouver un exemple d'utilisation de cette méthode pour le calcul d'intégrales [ici](https://tech.io/playgrounds/e48b2dfc5efc85659bceec666e771ffe67171/recueil-dexercices-pour-apprendre-python-au-lycee/la-methode-de-monte-carlo).

Dans la pratique, si un terme de la suite a un module plus grand que 2, cela suffit pour savoir si la suite tend vers l'infini.
Voici à quoi ressemblerait un programme directement inspiré des définitions pour calculer cette aire :

::: Dérouler pour voir le programme
``` python runnable
from time import time
from random import random

#---------------------   Les constantes 

X_MIN,Y_MIN,X_MAX,Y_MAX = -2,-1,1,1 # Valeurs min et max pour les parties reelles et imaginaires
MAX_ITER = 500 # Le nombre d'itérations maximum avant de considérer que la suite ne diverge pas vers l'infini
NB_POINTS = 1000000 # Nombres de points aléatoires choisis pour la méthode de Monte Carlo

#---------------------   Les fonctions

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
    
def monte_carlo():
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
```
:::

---

## Première amélioration

Avant de passer à la vectorization, commençons par optimiser un peu notre code. On peut remarquer que ce qui coûte cher en temps, ce sont les points qui sont dans l'ensemble car il faut calculer `MAX_ITER` termes de la suite pour constater qu'elle ne diverge pas. Or, si on observe l'ensemble de Mandelbrot, on constate qu'un grosse partie de sa surface provient d'une cardioide et du cercle situé à sa gauche. L'idée est donc de vérifier d'abord si $`c`$ appartient à cette cardioide ou ce cercle avant de calculer les termes de la suite. On pourra trouver les équations de ces ensembles [ici](https://fr.wikipedia.org/wiki/Ensemble_de_Mandelbrot#Cardio%C3%AFde_/_bourgeon_principal). On obtiendrait le programme suivant :

::: Dérouler pour voir les modifications de `mandelbrot(c)`
``` python runnable
from time import time
from random import random

#---------------------   Les constantes 

X_MIN,Y_MIN,X_MAX,Y_MAX = -2,-1,1,1 # Valeurs min et max pour les parties reelles et imaginaires
MAX_ITER = 400 # Le nombre d'itérations maximum avant de considérer que la suite ne diverge pas vers l'infini
NB_POINTS = 1000000 # Nombres de points aléatoires choisis pour la méthode de Monte Carlo

#---------------------   Les fonctions
    
def mandelbrot(c):
    """
    Renvoie 0 si la suite diverge avant MAX_ITER itérations et 1 sinon.
    Permet de compter les points de non divergence vers l'infini.
    """
    # On regarde d'abrod si c est dans la cardioide ou le cercle principal
    p = abs(c-0.25)
    if c.real < p - 2*p*p + 0.25 or (c.real+1)**2 + c.imag**2 < 0.0625 : return 1
    # Sinon, on étudie la suite
    z = 0
    for n in range(MAX_ITER):
        z = z*z + c
        if abs(z) > 2 : return 0
    return 1    
    
def monte_carlo():
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
```
:::



## brouillon

 Nous pouvons faire plusieurs remarques :

- La première est classique lorsqu'on veut optimiser des calculs : Eviter les calculs inutiles.  On ne s'en rend pas vraiment compte en regardant le programme précédent mais on choisit 1 million de points au hasard et pour chacun, il faut calculer dans le pire des cas 400 termes de la suite. Cela fait beaucoup de calculs mais en plus, certains sont faits plusieurs fois. En effet, lorqu'on calcule $`z^2`$ on calcule en réalité $`x^2 - y^2`$ et $`2xy`$ (si on note $`z=x+yi`$). De plus on vérifie à chaque fois si $`abs(z)\geq 2`$ or ce calcul est très gourmand car il faut calculer $`\sqrt{x^2+y^2}`$. Il est donc plus sage de vérifier simplement que $`x^2+y^2\geq 4`$ et on voit ainsi qu'on a intérêt à ne pas passer par les complexes mais plutôt faire soi-même les calculs des parties réelles et imaginaires.  
On obtiendrait le programme suivant :

::: Dérouler pour voir les modifications de `mandelbrot(c)`
```python runnable
from time import time
from random import random

#---------------------   Les constantes 

X_MIN,Y_MIN,X_MAX,Y_MAX = -2,-1,1,1 # Valeurs min et max pour les parties reelles et imaginaires
MAX_ITER = 500 # Le nombre d'itérations maximum avant de considérer que la suite ne diverge pas vers l'infini
NB_POINTS = 1000000 # Nombres de points aléatoires choisis pour la méthode de Monte Carlo

#---------------------   Les fonctions

def mandelbrot(c):
    """
    Renvoie 0 si la suite diverge avant MAX_ITER itérations et 1 sinon.
    Permet de compter les points de non divergence vers l'infini.
    """
    x,y = 0,0
    for n in range(MAX_ITER):
        # On calcule les carrés une seule fois
        x2 = x*x
        y2 = y*y
        if x2 + y2 > 4 : return 0
        y = 2 * x * y + c.imag
        x = x2 - y2 + c.real
    return 1
    
def monte_carlo():
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
```
:::

