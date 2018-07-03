# Bienvenue pour cette nouvelle partie : Optimisation

Dans cette partie, nous allons présenter différentes manières d'améliorer vos programmes principalement en rapidité. Pour l'instant, il n'est pas prévu de faire une partie cours sur la complexité algorithmique (je vous renvoie vers internet) mais seulement de présenter des méthodes pour programmer efficacement dans certaines situations classiques.

Je profite de cette page pour mettre quelques astuces courtes qui ne méritent pas une page à elles seules mais qui peuvent faire gagner du temps.

### Préférer les variables locales aux globales quand c'est possible. 

Autrement dit, il vaut mieux créer des fonctions pour faire des boucles longues plutôt que les lancer directement.  
Exemple : Considérons les deux façons de programmer suivante  
``` python
# Méthode directe
n=0
for i in range(10**8):
    n+=1
```  
et
```python
# Méthode en mettant la boucle dans une fonction
def fonction():
    n=0
    for i in range(10**8):
        n+=1

fonction()
```  
A priori, on fait la même chose or la première méthode met 15 sec pour s'executer et la seconde seulement 10 sec. Ce qui est énorme comme différence pour faire exactement la même chose donc il vaut mieux, quand on a des boucles longues, les mettre dans une fonction.


### Savoir déterminer le temps mis par notre programme

Pour cela, on utilise la fonction time du module time. Cette fonction donne le nombre de seconde écoulée depuis l'instant 0 de l'informatique (qui est le 1 janvier 1970 à 00h00). Il suffit donc de faire la différence entre le temps final et le temps initial pour savoir combien de temps s'est écoulé. Voici la structure de son utilisation :

```python
from time import time

t_i = time()

# le code à executer
blablabla

t_f = time()

print(" Le temps mis en secondes est : ",t_f-t_i)
```

###### Compléments sur la mesure du temps
Comme on cherche souvent à connaitre le temps mis par nos programmes ou seulement d'une fonction, il peut être agréable de créer une bonne fois pour toute une fonction sous forme de décorateur qui nous donne le temps mis par une fonction. Le plus simple est de mettre le décorateur dans notre boite à outils perso. Pour plus de précisions sur les décorateurs, allez voir sur internet.

Voici le décorateur : 

``` python
from time import time 

def chrono(fonction):
    def lancer(*args, **kwargs):
        t_i = time()
        resultat = fonction(*args, **kwargs)
        t_f = time()
        print("temps d'execution (en s):", t_f-t_i)
        return resultat
    return lancer
```

Et sur un exemple à tester :
@[Mesure du temps avec décorateur]({"stubs": ["Optimisation/mesure_temps_deco.py"], "command": "python3 Optimisation/mesure_temps_deco.py"})

### Bien connaitre et choisir ses outils

Les données qu'on utilise ne sont pas toutes les mêmes et la façon dont elles sont gérées doit nous influer sur notre choix selon l'utilisation qu'on va en faire. Par exemple, si on travaille avec des entiers, il ne sert à rien d'utiliser des flottants qui sont beaucoup plus gourmands en mémoire et en calcul. Prenons un exemple un peu moins évident : quand on utilise des listes, ensembles ou dictionnaires.

Lancer les tests ci-dessous et analysons les résultats.
@[Mesure du temps : parcourt d'une liste/ensemble/dictionnaire]({"stubs": ["Optimisation/mesure_temps_parcourt.py"], "command": "python3 Optimisation/mesure_temps_parcourt.py"})

@[Mesure du temps : appartenance à une liste/ensemble/dictionnaire]({"stubs": ["Optimisation/mesure_temps_appartenance.py"], "command": "python3 Optimisation/mesure_temps_appartenance.py"})

Dans le premier exemple, on constate qu'il est beaucoup plus rapide de parcourir une liste et un dictionnaire qu'un ensemble. Par contre, on voit dans le deuxième exemple qu'il est beaucoup plus long de chercher un élément dans une liste que dans un ensemble ou un dictionnaire. Ainsi l'utilisation qu'on va faire des données stockées (parcourt ou appartenance ou ...) détermine grandement le choix à faire pour éviter d'avoir des programmes beaucoup trop long inutilement. 

Quand plusieurs choix s'offrent à vous pour programmer, il ne faut pas hésiter à tester comme dans les deux exemples précédents lequel serait le plus efficace et se faire une liste des préférences qu'il faut avoir selon les cas.
