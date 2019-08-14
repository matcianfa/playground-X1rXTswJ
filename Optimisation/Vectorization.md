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
```
:::

---

## Utilisation de Numpy pour vectoriser

L'idée de la vectorisation est de remplacer une (ou plusieurs) boucle par des calculs sur un tableau/ vecteur numpy. Par exemple ici, au lieu de choisir une par une les valeurs aleatoires de `c`, on va créer directement un tableau contenant tous les `c` choisis aléatoirement et faire les calculs directement en utilisant le tableau. C'est a priori plus compliqué et demande plus de ressources mais les boucles en python sont tellement lentes que faire ainsi permet de gagner en vitesse. Voici le programme :

::: Dérouler pour voir les modifications
@[Utilisation de Numpy]({"stubs": ["Optimisation/mandelbrot_numpy.py"], "command": "python3 Optimisation/mandelbrot_numpy.py"})
:::

Donnons quelques explications :

- Pour la fonction `mandelbrot(c)`, elle va agir directement sur un vecteur contenant tous les `c` choisis aléatoirement. Ainsi, au lieu de renvoyer juste 0 ou 1 selon que le `c` est dans l'ensemble ou pas, la fonction va renvoyer un vecteur de 0 ou de 1 correspondant à la même chose mais pour tous les `c` d'un coup.  
Toute la fonction est donc repensée pour faire tous les calculs d'un coup sur le vecteur et en utilisant les propriétés des tableaux numpy (par exemple les opérations comme `z*z` sont faites coordonnées par coordonnées tout comme `np.abs(z)` applique `abs` à chaque coordonnée).

- Pour la fonction `monte_carlo()`, on ne fait plus une boucle pour créer à chaque fois un `c` mais on crée un vecteur de tous les `c` qu'on va considérer.

---

## Interlude : Utilisation de numba

Attention, ce qui suit va ressembler à un tour de magie :  
- Prenez le premier code (celui qui met presque 30 sec)
- Rajoutez `from numba import jit`
- Rajoutez `@jit` sur la ligne précédent les fonctions `mandelbrot` et `monte_carlo`
- Admirez : vous obtenez le même résultat en moins de 2 sec...

En voici la preuve :

::: Dérouler pour voir les modifications
@[Utilisation de Numba]({"stubs": ["Optimisation/mandelbrot_numba.py"], "command": "python3 Optimisation/mandelbrot_numba.py"})
:::

Si j'ai bien compris, Numba traduit plus ou moins le langage python pour directement traduire notre programme en code machine. Ce qui le rend, dans notre cas, aussi rapide que des langages comme le C. Malheureusement la magie n'opère pas toujours car certaines fonctions sont propres au langage python (les listes en compréhension par exemple) mais en tout cas cela marche très bien avec les fonctions de bases et numpy pour peu que cela soit fait proprement. 

## Vectorisation en utilisant numpy et numba




## brouillon
## Première amélioration

Avant de passer à la vectorization, commençons par optimiser un peu notre code. On peut remarquer que ce qui coûte cher en temps, ce sont les points qui sont dans l'ensemble car il faut calculer `MAX_ITER` termes de la suite pour constater qu'elle ne diverge pas. Or, si on observe l'ensemble de Mandelbrot, on constate qu'un grosse partie de sa surface provient d'une cardioide et du cercle situé à sa gauche. L'idée est donc de vérifier d'abord si $`c`$ appartient à cette cardioide ou ce cercle avant de calculer les termes de la suite. On pourra trouver les équations de ces ensembles [ici](https://fr.wikipedia.org/wiki/Ensemble_de_Mandelbrot#Cardio%C3%AFde_/_bourgeon_principal). On obtiendrait le programme suivant :

::: Dérouler pour voir les modifications de `mandelbrot(c)`
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
    # On regarde d'abord si c est dans la cardioide ou le cercle principal
    p = abs(c-0.25)
    if c.real < p - 2*p*p + 0.25 or (c.real+1)**2 + c.imag**2 < 0.0625 : return 1
    # Sinon, on étudie la suite
    z = 0
    for n in range(MAX_ITER):
        z = z*z + c
        if abs(z) > 2 : return 0
    return 1    
    
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
```
:::
 Nous pouvons faire plusieurs remarques :

- La première est classique lorsqu'on veut optimiser des calculs : Eviter les calculs inutiles.  On ne s'en rend pas vraiment compte en regardant le programme précédent mais on choisit 1 million de points au hasard et pour chacun, il faut calculer dans le pire des cas 400 termes de la suite. Cela fait beaucoup de calculs mais en plus, certains sont faits plusieurs fois. En effet, lorqu'on calcule $`z^2`$ on calcule en réalité $`x^2 - y^2`$ et $`2xy`$ (si on note $`z=x+yi`$). De plus on vérifie à chaque fois si $`abs(z)\geq 2`$ or ce calcul est très gourmand car il faut calculer $`\sqrt{x^2+y^2}`$. Il est donc plus sage de vérifier simplement que $`x^2+y^2\geq 4`$ et on voit ainsi qu'on a intérêt à ne pas passer par les complexes mais plutôt faire soi-même les calculs des parties réelles et imaginaires.  
On obtiendrait le programme suivant :

::: Dérouler pour voir les modifications de `mandelbrot(c)`
```python runnable
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
```
:::

