<h1> <center>Cours : Le module random</center></h1>

# Présentation du module `random`

Le module `random` est un module qui regroupe des fonctions permettant de  simuler le hasard. Nous avons déjà croisé des modules (comme le module `math`) et comme tous les module, pour pouvoir l'utiliser, il faut l'importer pour le mettre en mémoire. Donc dès qu'on voudra utiliser les fonctions qui suivent pour simuler le hasard, on devra mettre en entête la commande `from random import *`.

Commençons par les fonctions les plus utiles :

+ `randint(a,b)` : Donne un entier choisit au hasard entre a et b compris.
  Très pratique pour simuler un dés par exemple (appuyez plusieurs fois sur Run pour voir que le résultat change à chaque fois):
  ```python runnable
  from random import *
  
  n = randint(1,6)
  print(n)
  ```
  
+ `random()` : Donne un flottant au hasard dans l'intervalle [0 ; 1[.  
  `uniform(a,b)` : Donne un flottant au hasard entre a et b.
  Appuyez plusieurs fois sur Run pour voir le résultat.
  ```python runnable
  from random import *
  
  n = random()
  print(n)
  x = uniform(12, 18)
  print(x)
  ```
  
+ `choice(liste)` : Choisit un élément au hasard dans une liste.
  Par exemple :
  ```python runnable
  from random import *
  
  liste = [ "Pierre", "Caillou", "Ciseaux"]
  résultat = choice(liste)
  print(résultat)
  ```
  
+ `shuffle(liste)` : Mélange la liste sur place (c'est à dire qu'il modifie la liste d'origine).
  Exemple : 
  ```python runnable
  from random import *
  
  lettres = ["a" , "b", "c", "d", "e"]
  shuffle(lettres)
  print(lettres)
  ```
  On remarquera bien que contrairement à d'habitude, on ne met par le résultat de `shuffle` dans une variable car il agit directement sur la liste qu'on lui donne en entrée.
  
+ `choices(liste, k=nombre)` et `sample(liste, k=nombre)` : Ce sont deux fonctions qui permettent de simuler un tirage de `nombre` éléments dans une liste (Attention de bien mettre `k =` avant) mais la première est un tirage avec répétition (on remet l'objet tiré avant de retirer) alors que la seconde est sans répétition (comme si on tirer `nombre` éléments en même temps).  
  On peut rajouter des poids avec la fonction `choices(liste, weights = liste_poids, k= nombre)`.  
  Exemple :  
  ```python runnable
  from random import *
  
  lettres = ["a" , "b", "c", "d", "e"]
  résultat = choices(lettres, weights=[3,1,2,1,5], k=30)
  print(résultat)
  
  résultat2 = sample(lettres, weights=[3,1,2,1,5], k=3)
  print(résultat2)
  ```  
  Le premier résultat est un choix de 30 éléments parmi les `lettres` avec répétition et les poids qui font comme s'il y avait 3 'a', 1 'b', 2 'c', 1 'd' et 5 'e'.  
  Pour le second, on tire simplement 3 lettres parmi les 5 sans répétitions possibles. Forcément, il faudra que `k` soit inférieure à la longueur de la liste.
  

# QCM

Voici quelques QCM pour voir si vous avez bien compris. N'hésitez pas à relire ce qui précède si vous avez un doute.

###### QCM 1
```python
from random import *

n = randint(10,19)
print(n)
``` 
?[Cochez les nombres qu'on peut obtenir si on execute le code précédent. ]
-[x] 13 
-[ ] 3 
-[x] 10
-[ ] 21
-[x] 17
-[x] 19

---

###### QCM 2
```python
from random import *

n = uniform(10,19)
print(n)
``` 
?[Cochez les nombres qu'on peut obtenir si on execute le code précédent. ]
-[ ] 13 
-[x] 14.4 
-[x] 10.9
-[ ] 21.3
-[ ] 0.15
-[ ] 19.001 

---

###### QCM 3
```python 
from random import *

prénoms = [ "Pierre", "Marie", "Paul", "Elisa", "Léa", "Baptiste"]
résultat = ...
print(résultat)
```
?[Par quoi remplacer les ... pour que le programme précédent affiche un des prénoms de la liste au hasard ? ]
-[x] prénoms[randint(0,5)]
-[ ] shuffle(prénoms)
-[x] choice(prénoms)
-[ ] random(prénoms)

---


# Entrainement 

### Exercice 1

Créez un programme qui simule le lancer de deux dés, fait la somme et affiche le résultat de cette somme.

On affichera le résultat avec `print`.

@[Exercice 1]({"stubs": ["Maths/random_exo_1.py"], "command": "python3 Maths/random_exo_1_Test.py"})

---

### Exercice 2

Affichez une liste de de 200 nombres entiers aléatoires compris entre 5 et 17. 

On affichera le résultat avec `print`.

@[Exercice 2]({"stubs": ["Maths/random_exo_2.py"], "command": "python3 Maths/random_exo_2_Test.py"})

---

### Exercice 3

On donne les résultats du jeu Pierre Caillou Ciseaux sous forme de liste. On veut simuler 100 résultats sous forme d'une liste.

Faire un programme qui crée cette liste de 100 résultats aléatoires parmi "Pierre", "Caillou" et "Ciseaux" et l'affiche.

On affichera le résultat avec `print`.

@[Exercice 3]({"stubs": ["Maths/random_exo_3.py"], "command": "python3 Maths/random_exo_3_Test.py"})
