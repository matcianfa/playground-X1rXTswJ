# Triangles rectangles de coordonnées entières
`Difficulté : Moyen (25%)`
`Origine : Projet Euler n°91`

Les points P (x1, y1) and Q (x2, y2) ont des coordonnées entières et sont reliés à l'origine pour former le triangle OPQ.

![Triangle](https://projecteuler.net/project/images/p091_1.gif)

Il y a exactement 14 triangles rectangles formés à partir de deux points de coordonnées entières entre 0 et 2 inclus (0 ≤ x1, y1, x2, y2 ≤ 2).

![ Cas ou n=2](https://projecteuler.net/project/images/p091_2.gif)

Si on choisit 0 ≤ x1, y1, x2, y2 ≤ 50, combien de triangles rectangles peut-on former ?

On affichera le résultat avec `print`.

@[Triangles rectangles de coordonnées entières]({"stubs": ["Defis/Euler_91.py"], "command": "python3 Defis/Euler_91_Test.py"})

---

# Chaine de carrés de chiffres 
`Difficulté : Facile (5%)`
`Origine : Projet Euler n°92`

Une chaine de nombre peut être crée en ajoutant à chaque fois le carré des chiffres du nombre précédent.

Par exemple : 

44 → 32 → 13 → 10 → 1 → 1  
85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89  

Une chaine qui arrive sur 1 ou 89 sera bloquée dans une boucle sans fin. Ce qui est remarquable est que pour n'importe quel nombre de départ, on arrivera sur 1 ou 89.

Combien de nombres de départ inférieurs à dix million vont arriver à 89 ?

On affichera le résultat avec `print`.

@[Chaine de carrés de chiffres]({"stubs": ["Defis/Euler_92.py"], "command": "python3 Defis/Euler_92_Test.py"})

---

# Expressions arithmétiques
`Difficulté : Moyen (35%)`
`Origine : Projet Euler n°93`

En utilisant chaque chiffre de l'ensemble {1, 2, 3, 4} exactement une fois, et en utilisant les quatre opérations arithmétiques  (+, −, *, /) et des parenthèses, il est possible d'obtenir différents entiers positifs.

Par exemple :

8 = (4 * (1 + 3)) / 2  
14 = 4 * (3 + 1 / 2)  
19 = 4 * (2 + 3) − 1  
36 = 3 * 4 * (2 + 1)  

La concaténation des chiffres n'est pas permise comme 12+34.

En utilisant l'ensemble {1, 2, 3, 4}, il est possible d'obtenir 31 nombres distincts parmi lesquels 36 est le maximum et chaque nombres de 1 à 28 est obtenu mais pas 29.

Trouver l'ensemble de 4 chiffres distincts a < b < c < d, pour lesquels la liste des nombres consécutifs de 1 à n qu'on puisse obtenir avec des opérations arithmétiques est la plus longue. On donnera la réponse sous la forme d'un mot : abcd.

On affichera le résultat avec `print`.

@[Expressions arithmétiques]({"stubs": ["Defis/Euler_93.py"], "command": "python3 Defis/Euler_93_Test.py"})

---

# Triangles presque équilatéraux
`Difficulté : Moyen (35%)`
`Origine : Projet Euler n°94`

Il est facile de prouver qu'aucun triangle equilatéral n'a à la fois  les longueurs des cotés entières et son aire entière. Cependant, le triangle presque équilatéral 5-5-6 a une aire de 12 unité d'aire.

On définit un triangle presque équilatéral comme un triangle qui a deux cotés égaux et le troisième diffère de moins de 1 des deux autres.

Trouver la somme des périmètres de tous les triangles presque equilatéraux qui ont les longueurs des cotés entières ainsi que leur aire et dont le périmètre n'exède pas un milliard.

On affichera le résultat avec `print`.

@[Triangles presque équilatéraux]({"stubs": ["Defis/Euler_94.py"], "command": "python3 Defis/Euler_94_Test.py"})

---
