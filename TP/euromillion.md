# Simulations de l'Euromillion

Le but de cette page est de simuler nos potentiels gains à l'Euromillion après un certain nombre de tirages. Je rappelle que la loi interdit les jeux d'argent aux moins de 18 ans et peuvent qu'ils peuvent causer des addictions etc. mais normalement, après avoir fini les simulations sur cette page, cela devrait vous convaincre qu'il ne vaut mieux pas jouer.

Commençons par rappeler les règles : On choisit 5 numéros entre 1 et 50 (compris) ainsi que 2 étoiles (deux nombres entre 1 et 11 compris). Un tirage est effectué, en fonction du nombre de bons numéros et étoiles, on gagne une certaine somme. Le prix d'un ticket est de 2,50 euros.

Nous allons créer au fur et à mesure les fonctions necessaires à nos simulations.

## Simuler un tirage

Commençons par simuler un tirage de 5 numéros (entre 1 et 50 compris) et deux étoiles (entre 1 et 11 compris).

Pour cela, l'idée est simple : On s'intéresse d'abord aux 5 premiers numéros, on choisit un numéro au hasard (avec la fonction `randint` du module `random`), on met notre numéro dans la liste nommée `tirage` et on recommence 5 fois. Le problème c'est qu'en choisissant au hasard, on peut tomber plusieurs fois sur les mêmes numéros donc si c'est le cas, il faut relancer tant qu'on a pas un nouveau numéro. Puis on fait de même avec les étoiles.

Compléter la fonction `tirages()` ci-contre pour qu'elle renvoie un tirage de l'Euromillion puis appuyer sur Run ci-dessous pour voir si elle fonctionne correctement.

@[ ]({"stubs":["TP/Euromillion.py"], "command": "python3 TP/tirages_Test.py", "layout": "aside"})


