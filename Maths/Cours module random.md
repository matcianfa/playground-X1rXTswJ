<h1> <center>Cours : Le module random</center></h1>

# Présentation du module `random`

Le module `random` est un module qui regroupe des fonctions permettant de  simuler le hasard. Nous avons déjà croisé des modules (comme le module `math`) et comme tous les module, pour pouvoir l'utiliser, il faut l'importer pour le mettre en mémoire. Donc dès qu'on voudra utiliser les fonctions qui suivent pour simuler le hasard, on devra mettre en entête la commande `from random import *`.

Commençons par les fonctions les plus utiles :

+ `randint(a,b)` : Donne un entier choisit au hasard entre a et b compris.
  Très pratique pour simuler un dés par exemple (appuyez plusieurs fois sur Run pour voir que le résultat change à chaque fois):
  ```python runnable
  n = randint(1,6)
  print(n)
  ```
  
+ `random()` : Donne un flottant au hasard dans l'intervalle [0 ; 1[.  
  `uniform(a,b)` : Donne un flottant au hasard entre a et b.
  Appuyez plusieurs fois sur Run pour voir le résultat.
  ```python runnable
  n = random()
  print(n)
  x = uniform(12, 18)
  print(x)
  ```
  
+ `choice(liste)` : Choisit un élément au hasard dans une liste.
  Par exemple :
  ```python runnable
  liste = [ "Pierre", "Caillou", "Ciseaux"]
  résultat = choice(liste)
  print(résultat)
  ```
  
+ `shuffle(liste)` : Mélange la liste sur place (c'est à dire qu'il modifie la liste d'origine).
  Exemple : 
  ```python runnable
  lettres = ["a" , "b", "c", "d", "e"]
  shuffle(lettres)
  print(lettres)
  ```
  On remarquera bien que contrairement à d'habitude, on ne met par le résultat de `shuffle` dans une variable car il agit directement sur la liste qu'on lui donne en entrée.
  

# QCM

Voici quelques QCM pour voir si vous avez bien compris. N'hésitez pas à relire ce qui précède si vous avez un doute.

###### QCM 1
```python
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
```python runnable
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

@[Exercice 1]({"stubs": ["Maths/random_exo_1.py"], "command": "python3 Maths/random_exo_1_Test.py"})

---

### Exercice 2

En vous inspirant des exemples donnés dans la partie cours, écrire un programme qui affiche le plus petit entier n tel que 4 + 5 + 6 + ... + n dépasse 12345.

@[Exercice 2]({"stubs": ["Les_boucles/while_exo_2.py"], "command": "python3 Les_boucles/while_exo_2_Test.py"})

---

### Exercice 3

En vous inspirant des exemples donnés dans la partie cours, écrire un programme qui affiche le plus petit entier n tel que 1² + 2² + 3² + ... + n² dépasse 12345.

@[Exercice 3]({"stubs": ["Les_boucles/while_exo_3.py"], "command": "python3 Les_boucles/while_exo_3_Test.py"})
