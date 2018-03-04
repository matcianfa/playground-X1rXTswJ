# Trouver les plus petits éléments d'une liste
`Difficulté : Moyenne`

Le but de cet exercice est de créer un programme qui prend en entrée une ***liste*** de nombres et qui affiche en sortie une liste des indices où se trouvent le minimum de la liste donnée en entrée.

Par exemple : si ***liste=[1, 4, 5, 2, 1, 6, 1, 2, 1, 10, 9, 1, 4]*** alors comme le minimum est 1, la liste des indices où on trouve 1 est [0, 4, 6, 8, 11].

> Entrée : Une ***liste*** de nombre.

> Sortie : Une liste des indices où se trouve le minimum de ***liste***. Cette liste d'indices sera donnée rangée dans l'ordre croissant.

:::Aide
Pour énumérer dans une boucle `for`à la fois les éléments et leur indice, on peut utiliser 
```Python
for indice, élément in enumerate(liste) :
```
:::

@[Indices du plus petit élément]({"stubs": ["Les_listes/Plus_petit_element.py"], "command": "python3 Les_listes/Plus_petit_element_Test.py"})
