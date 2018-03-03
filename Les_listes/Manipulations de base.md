# Manipulations de base

### Afficher les éléments d'une liste

::: Point du cours
Les boucles `for` utilisées avec les listes.
:::

Faire un programme qui prend en entrée une ***liste*** de mots et affiche chaque mot de la liste indépendamment.

> Entrée : Une ***liste*** de mots

> Sortie : Les mots affichés (avec simplement `print(mot)` à chaque fois)

@[Affichage d'une liste de mots]({"stubs": ["Les_listes/affichage_elements.py"], "command": "python3 Les_listes/affichage_elements_Test.py"})

---

### Afficher les mots d'un texte

::: Point du cours
La fonction `.split()`
:::

Faire un programme qui sera très similaire au précédent mais cette fois ci l'entrée sera un ***texte*** dont vous devez afficher chaque mot indépendamment.

> Entrée : Un ***texte***.

> Sortie : Les mots affichés (avec simplement `print(mot)` à chaque fois)

@[Affichage d'un texte mot à mot]({"stubs": ["Les_listes/affichage_mot_texte.py"], "command": "python3 Les_listes/affichage_mot_texte_Test.py"})

---

### Sommes des éléments de deux listes

::: Point de cours
Créer une liste vide et ajouter des éléments au fur et à mesure.
:::

Créer un programme qui prend en entrée deux listes de nombres de même longueur et qui affiche la liste de l'addition terme à terme de ces deux listes. C'est à dire que le premier élément sera la somme des premiers éléments de chaque liste, de même pour le deuxième etc.

Par exemple: Si liste_1=[1, 2, 3] et liste_2=[2, 4, 6] alors le résultat à afficher sera [3, 6, 9].

> Entrée : Deux listes ***liste_1*** et ***liste_2***

> Sortie : La liste où on a additionné terme à terme les deux listes données en entrée. (On pourra utiliser directement print(liste) pour afficher la liste)


@[Somme terme à terme]({"stubs": ["Les_listes/Somme_terme_a_terme.py"], "command": "python3 Les_listes/Somme_terme_a_terme_Test.py"})

