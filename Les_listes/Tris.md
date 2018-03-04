# Méthodes de tri
`Difficulté : Moyenne`

Le but de ces exercices est de présenter quelques méthodes classiques de tris. Bien sur, il existe déjà des fonctions qui trient en Python mais le but ici est s'entrainer à manipuler les listes et aussi de découvrir des idées qui peuvent resservir dans d'autres contextes.

### Le tri à bulles

L'idée est de faire aller vers la fin de la liste les éléments les plus grands en les déplaçant de la manière suivante :
1. On considère le premier élément de notre liste et on le compare au second. S'il est plus grand on les intervertit.
2. On considère maintenant le second élément et on le compare au troisième. S'il est plus grand on les intervertit.
3. On continue comme ça jusqu'à arriver à la fin de la liste. A cet étape, on a mis forcément l'élément le plus grand en fin de liste.
4. On recommence les 3 premières étapes mais cette fois-ci en n'allant que jusqu'à l'avant-dernière position (puisque le plus grand est déjà en dernière position)
5. On continue ainsi en diminuant à chaque fois l'endroit où on arrête les comparaisons.

Ce tri s'appelle à bulles car à chaque étape, on fait remonter "la bulle" la plus grosse vers la fin de la liste.

Pour des explications peut-être plus claires et des exemples on peut aller voir [Wikipédia](https://fr.wikipedia.org/wiki/Tri_%C3%A0_bulles#Exemple_%C3%A9tape_par_%C3%A9tape)

Le but de cet exercice est de faire un programme qui tri une liste en utilisant le tri à bulles.

::: Aide
Pour inverser les valeurs continuent dans deux variables, on peut écrire simplement : `a,b = b,a`.
Cela marche aussi avec les éléments d'une liste : `liste[i],liste[j]=liste[j],liste[i]`
:::

@[Tri à bulles]({"stubs": ["Les_listes/Tri_a_bulles.py"], "command": "python3 Les_listes/Tri_a_bulles_Test.py"})
