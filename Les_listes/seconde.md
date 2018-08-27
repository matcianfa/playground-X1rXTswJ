# Exercices de niveau Seconde

Voici des exercices sur le chapitre Listes qui nécessitent un niveau de Seconde en mathématique.

# Tours connectées
`Difficulté : Facile`  
`Notion : Arbres`  
`Origine :` [`Hackerrank`](https://www.hackerrank.com/challenges/connecting-towns/problem)

Gandalf voyage de Rohan vers Rivendell pour rencontrer Frodon mais il n'y a pas de route directe de Rohan ($`T_1`$) vers Rivendell ($`T_n`$).

Cependant, il y a des tours $`T_2`$,$`T_3`$,$`T_4`$,... $`T_{n-1}`$ et entre chaque tours consécutives, il y a un certain nombre de routes. Plus précisément : entre la tour $`T_1`$ et $`T_2`$, il y a $`N_1`$ routes, et de manière générale, il y a $`N_i`$ routes entre $`T_i`$ et $`T_{i+1}`$, pour i allant de 1 à n-1. Il n'y a pas de routes entre $`T_i`$ et $`T_j`$ pour j ≠ i+1.

Trouver le nombre total de trajets différents que Gandalf peut prendre pour rejoindre Rivendell en partant de Rohan.

Remarque : Gandalf parcourt les tours dans l'ordre croissant des indices. Autrement dit, il ne rebrousse pas chemin pour retourner à une tour déjà visitée.

> Entrée : Le nombre ***n*** de tours ainsi que la ***liste*** contenant les nombres $`N_i`$ de chemins entre les tours $`T_i`$ et $`T_{i+1}`$.

> Sortie : Le nombre total de trajets différents que Gandalf peut prendre pour rejoindre Rivendell en partant de Rohan, affiché avec `print`.

@[Tours connectées]({"stubs": ["Les_listes/Tours_connectees.py"], "command": "python3 Les_listes/Tours_connectees_Test.py"})
