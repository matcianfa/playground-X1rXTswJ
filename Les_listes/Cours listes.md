<h1> <center>Cours : Les listes</center></h1>

# Présentation des listes

Les listes sont des incontournables de la programmation. Tant qu'on a que quelques informations à stocker, on peut les mettre dans des variables mais on ne peut pas s'amuser à rentrer une à une 1000 informations dans une variable individuelle... A la place, on les met dans une liste que l'on pourra manipuler et c'est cette liste qu'on sauvegarde dans une variable.

# Création d'une liste

Commençons par les bases : Créer une liste. Il y a plusieurs façons d'en créer :

+ En rentrant les données à la main :
  Par exemple :
  ```python
  ma_liste_de_nombres = [ 1, 4, 9, 3, 1, 2 ]
  ma_liste_de_courses = [ "stylos rouges" , "piles" , "souris pour la salle info" , "claviers" ]
  ma_liste_de_coordonnées_de_vecteurs = [ (1,1) , (0,1) , (1,6)]
  ma_liste_bordélique = ["un texte", 18, 5.4, True, (1,0)]
  ```
  On remarquera qu'on peut mettre un peu de tout dans une liste et en plus mélanger les types (chaines de caractères, nombres, booléens ...).
  Un dernier exemple qui est celui que vous allez utiliser le plus : la liste qui ne contient rien !
  ```python
  la_liste_vide = []
  ```
  
+ En ajoutant des objets dans une liste :  
  Il y a plusieurs façons de s'y prendre :
    - `.append(obj)` : à rajouter derrière la liste à qui on veut rajouter `obj`. Important : Elle modifie directement la liste et ne renvoie rien.
      ```python runnable
      ma_liste_de_courses = [ "stylos rouges" , "piles" , "souris pour la salle info" , "claviers" ]
      ma_liste_de_courses.append("brosse pour effacer")
      print(ma_liste_de_course)
      ```
      Je suis obligé de retaper le nom de ma liste pour la voir car elle a été modifiée directement.  
      En partant de la liste vide, on peut ainsi créer un nouvelle liste en ajoutant élément par élément. Cela peut sembler absurde ou du moins très long  mais dans une boucle for ou while, c'est une manière très pratique de créer une liste de données qu'on calcule ou qui nous arrive au fur et à mesure.
      
    - `.extend(autre_liste)` : à rajouter derrière la liste à qui on veut rajouter à la suite la deuxième_liste. Comme pour append, elle modifie directement la liste et ne renvoie rien.
      ```python runnable
      ma_liste_de_nombres = [ 1, 4, 9, 3, 1, 2 ]
      ma_liste_de_nombres.extend([ 6, 12, 14])
      print(ma_liste_de_nombres)
      ```

    - `liste1 + liste2` : Comme pour les chaines de caractères, le signe + va permettre de mettre les deux listes bout à bout, tout comme extend mais à un énorme différence près : avec extend, la première liste devient le résultat alors que dans ce cas ci, il faut mettre le résultat dans une variable pour le sauvegarder. C'est comme pour 3+5, si on ne met pas le résultat dans une variable, on ne pourra rien en faire.
      Pour résumer, la fonction `extend(autre_liste)` correspond à `liste = liste + autre_liste` mais du coup, on perd les informations qui sont dans `liste` à l'origine ce qui n'est pas toujours ce que l'on veut. Il faudra donc choisir au mieux la façon dont on rajoute les éléments dans une liste.
      ```python runnable
      liste_chiffres_pairs=[0 ,2 ,4 ,6 ,8 ]
      liste_chiffres_impairs=[1, 3, 5, 7 ,9]
      print(liste_chiffres_pairs + liste_chiffres_impairs)
      ```
      Le résultat s'affiche contrairement au cas où on aurait utilisé .extend mais comme on n'a pas mis le résultat dans une variable, on ne pourrait pas l'utiliser ensuite...

+ `liste * n` : crée une nouvelle liste où la liste est répétée en boucle n fois.
  ```python runnable
  print([1] * 5)
  print([1, 2, 3]* 3)
  ```
+ Utiliser `list(obj)` : Cette fonction transforme quand c'est possible `obj` en liste. Par exemple un ensemble, un tuple, un itérateur. On va voir un exemple juste après avec `range`.
  
+ En utilisant la fonction range :
  C'est une fonction qui donne une énumération de nombres. Petit rappel :
  - range(n) : crée une énumération de n nombres allant de 0 à n-1. Et oui en informatique, il va falloir prendre l'habitude de toujours commencer à 0 et du coup finir à n-1 si on veut n nombres en tout.
  - range(n1,n2) : crée une énumération de nombres allant de n1 à n2-1.
  - range(n1,n2,pas) : crée une énumération de nombres allant de n1 à n2-1 en sautant de pas en pas.
  
  Remarque importante : On a précisé ici que `range` fournit une *énumération*. En effet, ce n'est pas directement une liste de nombre comme on pourrait le penser quand on l'utilise avec `for`. On peut cependant très facilement en faire une liste en lui appliquant `list()`.  
  Par exemple :
  ```python runnable
  print(range(4))
  print(list(range(4)))
  print(list(range(3,6)))
  print(list(range(1,9,3)))
  print(list(range(3,0,-1)))
  ```
  On remarquera que le premier exemple ne donne pas une liste et qu'il faut absolument rajouter `list()` pour l'obtenir.
  
+ Création de liste par compréhension :
  On peut s'en passer dans un premier temps mais c'est de loin la manière la plus puissante de créer une nouvelle liste à partir de listes existantes. Voir le paragraphe dédié plus bas.
  
# Opérations sur les listes

Maintenant qu'on sait créer des listes, encore faut-il pouvoir les manipuler. Voici un résumé des principales actions sur les listes.
+ `liste[n]` : Permet de récupérer l'élément d'indice n. Attention : le premier élément est d'indice 0 !
  ```python runnable
  ma_liste_de_courses = [ "stylos rouges" , "piles" , "souris pour la salle info" , "claviers" ]
  ma_liste_de_courses[1]
  ma_liste_de_courses[-1]
  ```
  Comme pour les chaines de caractères, un nombre négatif nous permet de partir de la fin.
  
+ `liste[n1:n2]` : Permet de récupérer la liste des éléments d'indice compris entre n1 et n2-1.
  ```python runnable
  ma_liste_de_courses = [ "stylos rouges" , "piles" , "souris pour la salle info" , "claviers" ]
  ma_liste_de_courses[1 : 3]  
  ma_liste_de_courses[:3]
  ```
  Comme pour les chaines de caractères, si on omet  n1, on part du début et si on omet n2, on va jusqu'à la fin de la liste.
  
+ `liste[n]= val` : Permet de modifier la valeur de l'élément d'indice n.
  ```python runnable
  ma_liste_de_courses = [ "stylos rouges" , "piles" , "souris pour la salle info" , "claviers" ]
  ma_liste_de_courses[1] = "piles rechargeables"
  print(ma_liste_de_courses)
  ```
  
+ `len(liste)` : Donne la longueur de la liste (le nombre d'éléments).
  ```python runnable
  ma_liste_de_courses = [ "stylos rouges" , "piles" , "souris pour la salle info" , "claviers" ]
  len(ma_liste_de_courses)
  ```

+ `liste.remove(element)` : Retire `element` de la liste. Attention, il ne retire que la première occurrence, si `element` apparait plusieurs fois, il faut l'enlever plusieurs fois.
  ```python runnable
  ma_liste_de_courses = [ "stylos rouges" , "piles" , "souris pour la salle info" , "claviers" ]
  ma_liste_de_courses.remove("piles")
  print(ma_liste_de_courses)
  ```

+ `liste.reverse()` : Renverse l'ordre de la liste.

+ `liste.count(element)` : Donne le nombre de fois où element se trouve dans la liste.

+ `sum(liste)` : Donne la somme des éléments de la liste lorsque c'est une liste de nombres bien entendu. Extremement pratique car elle évite une boucle `for` et sert très souvent.

+ `liste.sort()` : Trie liste dans l'ordre croissant. Si on veux avoir un tri dans l'ordre décroissant il faut écrire `liste.sort(reverse=True)`.

+ `sorted(liste)` : Renvoie liste triée dans l'ordre croissant. Si on veux avoir un tri dans l'ordre décroissant il faut écrire `sorted(liste,reverse=True)`.
  Ces deux fonctions font semblablement la même à une grosse différence près : liste.sort() modifie liste ce qui veut dire qu'on perd notre liste de départ alors que sorted(liste) ne modifie pas liste, elle crée une nouvelle liste des éléments de `liste` triés.
  
+ `element in liste` : Renvoie True si element est dans la liste et False sinon.
  ```python runnable
  ma_liste_de_courses = [ "stylos rouges" , "piles" , "souris pour la salle info" , "claviers" ]
  print("claviers" in ma_liste_de_courses)
  print("stylos" in ma_liste_de_courses)
  ```
  Remarquez bien que "stylos" n'est pas dans la liste car c'est "stylos rouges" qui y est, ce qui n'est pas la même chaine de caractères.
  

# QCM

Voici quelques QCM pour voir si vous avez bien compris. N'hésitez pas à relire ce qui précède si vous avez un doute.

###### QCM 1
```python
texte = "Un chasseur sachant chasser doit savoir chasser sans son chien."
print(texte[5])
```  
?[Que va afficher ce programme ? ]
-[x] "a" 
-[ ] "s"
-[ ] "Un ch"
-[ ] "h"

---

###### QCM 2
```python
texte = "Un chasseur sachant chasser doit savoir chasser sans son chien."
print(texte[:5])
```  
?[Que va afficher ce programme ? ]
-[ ] "Un cha" 
-[ ] "Un chasseur sachant chasser doit"
-[x] "Un ch"
-[ ] "asseur sachant chasser doit savoir chasser sans son chien."

---

###### QCM 3
```python
texte = "Un chasseur sachant chasser doit savoir chasser sans son chien."
print(texte[5:10])
```  
?[Que va afficher ce programme ? ]
-[x] "asseu" 
-[ ] "hasseu"
-[ ] "asseur"
-[ ] "ar"

---

###### QCM 4
```python
texte = "Un chasseur sachant chasser doit savoir chasser sans son chien."
print(texte[-2])
```  
?[Que va afficher ce programme ? ]
-[ ] "i" 
-[ ] "e"
-[x] "n"
-[ ] "."


---

###### QCM 5
```python
texte = "Un chasseur sachant chasser doit savoir chasser sans son chien."
print(texte[:2]+texte[6:8])
```  
?[Que va afficher ce programme ? ]
-[ ] "Un sse" 
-[ ] "Un ss"
-[ ] "Unsse"
-[x] "Unss"


---

###### QCM 6
```python
texte = "Un chasseur sachant chasser doit savoir chasser sans son chien."
print(...)
```  
?[Que faut-il mettre à la place des ... pour afficher "sachant"? ]
-[ ] texte[12:18] 
-[ ] texte[11:18]
-[x] texte[12:19]
-[ ] texte[12]+texte[18]

---

###### QCM 7
```python
texte = "Un chasseur sachant chasser doit savoir chasser sans son chien."
print(...)
```  
?[Que faut-il mettre à la place des ... pour afficher le nombre de "e" dans ce texte ? ]
-[x] texte.count("e")
-[ ] count("e")
-[ ] count(texte,"e")
-[ ] texte.count(e)

---

###### QCM 8
```python
texte = "Un chasseur sachant chasser doit savoir chasser sans son chien."
print(texte.find("ch"))
```  
?[Que va afficher ce programme ? ]
-[x] 3
-[ ] 4
-[ ] 5
-[ ] 3, 13, 19, 39, 57

---

###### QCM 9
```python
texte = "Un chasseur sachant chasser doit savoir chasser sans son chien."
print(texte.replace("ss","ch"))
```  
?[Que va afficher ce programme ? ]
-[ ] "Un ssasseur sassant ssasser doit savoir ssasser sans son ssien."
-[ ] "Un chacheur sachant chacher doit savoir chacher sanchon chien."
-[ ] "Un chacheur chachant chacher doit chavoir chacher chanch chon chien."
-[x] "Un chacheur sachant chacher doit savoir chacher sans son chien."

---

###### QCM 10
```python
texte = "Un chasseur sachant chasser doit savoir chasser sans son chien."
print("ch" in texte)
print("chant" in texte)
print("Un chien" in texte)
print("r s" in texte)
print("u" in texte)
```  
?[Cochez les cases correspondant au numéro des lignes qui vont afficher True ]
-[x] 2
-[x] 3
-[ ] 4
-[x] 5
-[ ] 6

# Entrainement 

### Exercice 1

Pour le nombre `n` donné dans la fenêtre ci-dessous, énumérez ses chiffres.

Pour l'affichage, on utilisera `print` et les chiffres seront affichés en allant à la ligne à chaque fois.

@[Exercice 1]({"stubs": ["Chaines_caracteres/chaine_exo_1bis.py"], "command": "python3 Chaines_caracteres/chaine_exo_1bis_Test.py"})

---

### Exercice 2

Pour le texte donné dans la fenêtre ci-dessous, créer un programme qui affiche le nombre de voyelle.

Pour l'affichage, on utilisera `print`.

@[Exercice 2]({"stubs": ["Chaines_caracteres/chaine_exo_2.py"], "command": "python3 Chaines_caracteres/chaine_exo_2_Test.py"})

---

### Exercice 3

Pour le texte donné dans la fenêtre ci-dessous, créer un programme qui affiche l'indice de tous les "e" dans ce texte.

Pour l'affichage, on utilisera `print` et les indices seront affichés en allant à la ligne à chaque fois.

@[Exercice 3]({"stubs": ["Chaines_caracteres/chaine_exo_1.py"], "command": "python3 Chaines_caracteres/chaine_exo_1_Test.py"})
