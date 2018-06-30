# Chemin sur un pavé
`Difficulté : Moyen (35%)`
`Origine : Projet Euler n°86`

Une araignée, S, est dans un coin d'une pièce en forme de pavé mesurant 6 par 5 par 3. Une mouche est dans le coin opposé. En se déplaçant sur la surface de la pièce par le plus court chemin "en ligne droite" de S vers F, la distance est 10 et le chemin est représenté sur la figure.

![plus court chemin](https://projecteuler.net/project/images/p086.gif)

Il y a jusqu'à trois candidats possibles pour le chemin le plus court pour chaque pavé et le chemin le plus court n'a pas toujours une longueur qui est un entier. 

On peut montrer qu'il y a exactement 2060 pavés différents (à rotation près) de dimension entière jusqu'à une dimension maximale de M par M par M, pour lesquels la route la plus courte à une longueur entière lorsque M=100. C'est la plus petite valeur de M pour laquelle le nombre de solutions dépasse pour la première fois 2000; le nombre de solutions pour M=99 étant de 1975.

Trouver la plus petite valeur telle que le nombre de solutions dépasse pour la première fois un million.

On affichera le résultat avec `print`.

@[Chemin sur un pavé]({"stubs": ["Defis/Euler_86.py"], "command": "python3 Defis/Euler_86_Test.py"})

---
