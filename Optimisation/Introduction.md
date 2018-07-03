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

##### Compléments 
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
@[Mesure du temps avec décorateur]({"stubs": ["Optimisation/mesure_temps_deco.py"], "command": "python3 Defis/mesure_temps_deco.py"})
