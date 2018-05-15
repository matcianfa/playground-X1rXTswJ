# Remplacement de chiffres dans un nombre premier
`Difficulté : Moyen (15%)`
`Origine : Projet Euler n°51`

En remplaçant le premier chiffre dans un nombre de 2 chiffres de la forme *3, on peut trouver six sur les neufs possibles qui sont des nombres premiers : 13, 23, 43, 53, 73 et 83.

En remplaçant le troisième et le quatrième chiffres dans un nombre de la forme 56**3 par un même chiffre, ce nombre de cinq chiffre est le premier exemple ayant sept nombres premiers sur les dix générés : 56003, 56113, 56333, 56443, 56663, 56773, et 56993.  Ainsi, 56003 est le plus petit nombre premier ayant cette propriété.

Trouver le plus petit nombre premier qui, en remplaçant une partie de ce nombre (pas forcément des chiffres adjacents) avec un même chiffre engendre une famille de huit nombres premiers.

On affichera le résultat avec `print`.

@[Remplacement de chiffres dans un nombre premier]({"stubs": ["Defis/Euler_51.py"], "command": "python3 Defis/Euler_51_Test.py"})

---

# Multiples permutés
`Difficulté : Facile`
`Origine : Projet Euler n°52`

On peut voir que le nombres 125874 et son double 251748 contiennent exactement les mêmes chiffres mais dans un ordre différent.

Trouver le plus petit entier positif x tel que 2x, 3x, 4x, 5x, et 6x contiennent les mêmes chiffres.

On affichera le résultat avec `print`.

@[Multiples permutés]({"stubs": ["Defis/Euler_52.py"], "command": "python3 Defis/Euler_52_Test.py"})

---

# Selection combinatoire
`Difficulté : Facile`
`Origine : Projet Euler n°53`

Il y a exactement 10 façon de selectionner 3 chiffres parmi 5, 12345 :

123, 124, 125, 134, 135, 145, 234, 235, 245, et 345
En combinatoire, on utilise la notation $`C_5^3 = 10`$.

En général, on a la formule : $`C^r_n= \dfrac{n!}{r!(n-r)!}`$ où $`r\leq n`$, et $`n!=n\times(n-1)\times...\times 3\times 2\times 1`$, et la convention $`0!=1`$.

Ce n'est que pour n=23 qu'une valeur dépasse un million : $`C_{23}{10}=1144066`$.

Combien de valeur de $`C_n^r`$ (non necessairement distincts) pour 1 ≤ n ≤ 100, sont supérieurs à un million ?

On affichera le résultat avec `print`.

@[Selection combinatoire]({"stubs": ["Defis/Euler_53.py"], "command": "python3 Defis/Euler_53_Test.py"})

---
