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

# Triplets de puissances de nombres premiers
`Difficulté : Moyen (20%)`
`Origine : Projet Euler n°87`

Le plus petit nombre qu'on peut exprimer comme la somme d'un carré d'un nombre premier, d'un cube d'un nombre premier et d'une puissance quatrième d'un nombre premier est 28. En fait, il y a exactement quatre nombres inférieurs à 50 qui peuvent s'exprimer d'une telle façon :

$`28 = 2^2 + 2^3 + 2^4  `$  
$`33 = 3^2 + 2^3 + 2^4  `$  
$`49 = 5^2 + 2^3 + 2^4 `$   
$`47 = 2^2 + 3^3 + 2^4`$  

Combien de nombres inférieurs à 50 million peuvent s'exprimer comme la somme d'un nombre premier au carré, d'un autre au cube et d'un troisième à la puissance quatre ?

On affichera le résultat avec `print`.

@[Triplets de puissances de nombres premiers]({"stubs": ["Defis/Euler_87.py"], "command": "python3 Defis/Euler_87_Test.py"})

---

# Nombres produits-sommes
`Difficulté : Difficile (40%)`
`Origine : Projet Euler n°88`

Un entier naturel N qui peut s'écrire comme somme et produit d'une liste d'au moins deux nombres $`\{a_1, a_2, \dots, a_k\}`$ est appelé un nombre produit-somme : $`N = a_1 + a_2 + ... + a_k = a_1 × a_2 × ... × a_k`$.

Par exemple, 6 = 1 + 2 + 3 = 1 × 2 × 3.

Pour un ensemble donné de taille k, on peut appelé le plus petit N avec cette propriété un nombre produit-somme minimal. Les nombres produits-sommes minimaux pour les ensembles de taille k= 2, 3, 4, 5, et 6 sont les suivants :

k=2: 4 = 2 × 2 = 2 + 2  
k=3: 6 = 1 × 2 × 3 = 1 + 2 + 3  
k=4: 8 = 1 × 1 × 2 × 4 = 1 + 1 + 2 + 4  
k=5: 8 = 1 × 1 × 2 × 2 × 2 = 1 + 1 + 2 + 2 + 2  
k=6: 12 = 1 × 1 × 1 × 1 × 2 × 6 = 1 + 1 + 1 + 1 + 2 + 6  

Ainsi pour 2≤k≤6, la somme de tous les nombres produits-sommes- minimaux est 4+6+8+12 = 30; On notera que 8 n'est conmpté qu'une sseule fois dans la somme.

De plus, la somme des nombres produits-sommes pour 2≤k≤12 est {4, 6, 8, 12, 15, 16}, la somme est donc 61.

Quelle est la somme de tous les nombres produits-sommes minimaux pour 2≤k≤12000 ?

On affichera le résultat avec `print`.

@[Nombres produits-sommes]({"stubs": ["Defis/Euler_88.py"], "command": "python3 Defis/Euler_88_Test.py"})

---

# Chiffres romains
`Difficulté : Moyen (20%)`
`Origine : Projet Euler n°89`

Pour qu'un nombre écrit en chiffres romains soit considéré valide, il y a quelques règles de base qu'il faut suivre. Cependant, les règles laissent la possibilité pour certains nombres d'être représentés de plusieurs façons mais il y en a toujours une "meilleure".

Par exemple, il ya au moins 6 façons d'écrire le nombre 16 :

IIIIIIIIIIIIIIII  
VIIIIIIIIIII  
VVIIIIII  
XIIIIII  
VVVI  
XVI  

Cependant, d'après les règles, seules XIIIIII et XVI sont valides et cette dernière est considérée comme la plus efficiente car elle utilise le moins de caractères.

On pourra trouver les règles complètes ici : [règles](https://projecteuler.net/about=roman_numerals).

On donne ci-dessous la liste d'un millier de nombre en chiffres romains dont l'écriture est valide mais pas necessairement minimale.

Trouver le nombre de caractères economisé en ecrivant chacun sous leur forme minimale.

Note: On pourra admettre que chaque nombre dans la liste ne contient pas plus de 4 caractères identiques consécutifs.

On affichera le résultat avec `print`.

@[Chiffres romains]({"stubs": ["Defis/Euler_89.py"], "command": "python3 Defis/Euler_89_Test.py"})

---

# Paire de chiffres sur un cube
`Difficulté : Moyen (40%)`
`Origine : Projet Euler n°90`

Chacune des six faces d'un cube a un chiffre différent (de 0 à 9) écrit dessus. De même sur un second cube. En plaça,t les deux cubes cote à cote dans différentes positions, on peut former une variété de nombres de 2 chiffres.

Par exemple, le nombre 64 peut être formé :

![cube](https://projecteuler.net/project/images/p090.gif)

En choisissant bien les nombres sur les deux cubes, il est possible de retrouver tous les nombres qui sont des carrés inférieurs à 100 : 01, 04, 09, 16, 25, 36, 49, 64, and 81.

Par exemple, une manière d'y arriver est en plaçant {0, 5, 6, 7, 8, 9} sur un cube et {1, 2, 3, 4, 8, 9} sur l'autre.

De plus, pour ce problème, on pourra tourner le 6 pour obtenir un 9 et inversement ce qui veut dire qu'un arrangement comme {0, 5, 6, 7, 8, 9} et  {1, 2, 3, 4, 6, 7} permet aux 9 carrés d'être obtenus aussi non le carré 09 ne pourrait pas être obtenu.

Pour déterminer des arrangement distincts, on s'intéresse aux nombres de chaque cube, pas à leur ordre.

{1, 2, 3, 4, 5, 6} est equivalent à {3, 6, 4, 1, 2, 5}
{1, 2, 3, 4, 5, 6} est distinct de {1, 2, 3, 4, 5, 9}

Combien d'arrangements distincts de deux cubes permet à tous les nombres carrés inférieurs à 100 d'être obtenus ? 

On affichera le résultat avec `print`.

@[Paire de chiffres sur un cube]({"stubs": ["Defis/Euler_90.py"], "command": "python3 Defis/Euler_90_Test.py"})

---
