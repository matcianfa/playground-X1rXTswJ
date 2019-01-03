# Tout en une ligne !
`Difficulté : Moyenne`

Le but de cette fiche est de s'entrainer avec les créations de liste en compréhension. Voir le cours sur les listes pour plus de précision sur cette façon de créer des listes.

Tous les exercices qui suivent doivent se rédiger en une seule ligne à rajouter !

::: Aide
Pour afficher la liste tout en la créant, on peut écrire directement `print([n for n in range(10,21)])` ce qui affichera la liste des nombres entre 10 et 20.
:::

### Liste des différences des cubes des nombres et de leur carré

Faire un programme qui tient en une ligne donnant la liste des $`n^3-n^2`$ pour des entiers ***n*** compris entre ***a*** et ***b***.

> Entrée : Deux nombres entiers ***a*** et ***b***.

> Sortie : La liste des $`n^3-n^2`$ pour des entiers ***n*** compris entre ***a*** et ***b***.

@[Liste de nombres]({"stubs": ["Les_listes/Cube_moins_carre.py"], "command": "python3 Les_listes/Cube_moins_carre_Test.py"})

---

### Liste des multiples de 7

Faire un programme qui tient en une ligne donnant la liste des entiers compris entre ***a*** et ***b*** qui sont multiples de 7.

> Entrée : Deux nombres entiers ***a*** et ***b***.

> Sortie : La liste des entiers compris entre ***a*** et ***b*** qui sont multiples de 7.

@[Liste des multiples de 7]({"stubs": ["Les_listes/Multiples_de_7.py"], "command": "python3 Les_listes/Multiples_de_7_Test.py"})

---

### Somme des carrés des nombres impairs

Faire un programme qui tient en une ligne donnant la somme des carrés des nombres impairs compris entre ***a*** et ***b***.

> Entrée : Deux nombres entiers ***a*** et ***b***.

> Sortie : La somme des carrés des nombres impairs compris entre ***a*** et ***b***.

@[Somme des carrés des nombres impairs]({"stubs": ["Les_listes/Somme_carré_impairs.py"], "command": "python3 Les_listes/Somme_carré_impairs_Test.py"})

---

### Les mots de longueur donné.

Faire un programme qui tient en une ligne donnant la liste des mots de longueur ***n*** dans une ***liste*** de mots donnée.

> Entrée : Un entier ***n*** et une ***liste*** de mots

> Sortie : La liste des mots de ***liste*** de longueur ***n***.

@[Liste de mots]({"stubs": ["Les_listes/Mots_de_long_n.py"], "command": "python3 Les_listes/Mots_de_long_n_Test.py"})

---

### Liste des initiales

Un peu plus dur: 
Faire un programme qui tient en une ligne donnant la liste des initiales de la liste des prénoms et noms donnée en entrée.

> Entrée : Une ***liste*** de prénom et nom donné donnés sous la forme "Prénom Nom".

> Sortie : La liste des initiales sous la forme "PN".

Exemple: pour la ***liste***= ["Alain Verse", "Harry Cover", "Marc Assin"], il faudra afficher ["AV","HC","MA"].

@[Liste d'initiales]({"stubs": ["Les_listes/Liste_initiales.py"], "command": "python3 Les_listes/Liste_initiales_Test.py"})
