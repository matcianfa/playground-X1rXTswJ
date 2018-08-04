# Inversion en croix
`Difficulté : Extrême (100%)`
`Origine : Projet Euler n°331`

NxN disques sont placés sur un grille carrée. Chaque disque a une face blanche et une face noire.

A chaque tour, on peut choisir un disque et tourner alors tous les disques de la même ligne et colonne : Il y a donc 2N-1 disques retournés. Le jeu fini quand tous les disques montrent la face blanche. Voici un exemple de jeu sur une grille 5x5.

![Jeu](https://projecteuler.net/project/images/p331_crossflips3.gif)

On peut prouver que 3 est le nombre minimum de tours pour finir le jeu.

Le disque en bas à gauche de la grille a pour coordonnées (0,0), celui en bas à droite (N-1,0) et en haut à gauche (0,N-1).

On pose $`C_n`$ la configuration de la grille avec NxN disques suivante : Un disque de coordonnées (x,y) vérifiant $`(N-1)^2\leq x^2 + y^2 \leq N^2`$ montre sa face noire. Sinon, il montre sa face blanche. $`C_5`$ est l'exemple ci-dessus.

On pose $`T_N)`$ le nombre minimal de tours pour finir le jeu qui commence à la configuration $`C_N`$ or 0 if configuration $`C_N`$ n'a pas de solution. On a $`T(5)=3`$. On peut montrer que T(10)=29 et T(1 000)=395253.

Trouver $`\Sum\limits_{i=3}^{31}T(2^i-i)`$

On affichera le résultat avec `print`.

Remarque : Si vous trouvez une solution qui met moins de 50 sec pour s'exécuter, je suis très intéressé !

@[Inversion en croix]({"stubs": ["Defis/Euler_331.py"], "command": "python3 Defis/Euler_331_Test.py"})

---
