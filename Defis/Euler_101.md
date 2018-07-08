# Polynôme optimal
`Difficulté : Moyen (35%)`
`Origine : Projet Euler n°101`

Si on nous donne les k premiers termes d'une suite, il est impossible de dire avec certitude la valeur du terme suivant car il y a une infinité de polynomes qui peut modéliser la suite.

Prenons comme exemple la suite des cubes. Elle est définie par la fonction génératrice  $`u_n=n^3`$ et donne :  1, 8, 27, 64, 125, 216, ...

Supponsons qu'on connaisse uniquement les 2 premiers termes de la suite. En utilisant le principe "le plus simple est le meilleurs", on peut considérer une relation linéaire et prédire que le terme suivant sera 15 (on ajoute 7 ). Mais si on nous avait donné les trois premiers termes de la suite, par le même principe de simplicité, on aurait pu supposer que la relation était du second degré.

On peut définir OP(k,n) comme étant le n-ieme terme de la suite associée au polynome optimal pour les k premier termes d'une suite donnée. Il est clair que OP(k,n) va exactement engendrer les termes de cette suite pour n ≤ k, et potentiellement le premier terme incorrect (PTI) sera OP(k,k+1) et dans ce cas, on l'appellera le mauvais OP (MOP).

Au départ, si on ne nous donne qu'un terme de la suite, le plus simple sera de considérer un constante. Donc pour n ≥ 2, OP(1, n) = u1.

Ainsi, on obtient les OP pour la suite des cubes :

 --- | ---
$`OP(1, n) = 1`$ |  1,***1***, 1, 1, ...  
$`OP(2, n) = 7n−6`$ | 1, 8, ***15***, ...  
$`OP(3, n) = 6n^2−11n+6`$ |	1, 8, 27, ***58***, ...  
$`OP(4, n) = n^3`$ | 1, 8, 27, 64, 125, ...  

Clairement, il n'y a pas de MOP pour k ≥ 4.

En considérant la somme des PTI engendrés par les MOP (indiqué en gras ci dessus), on obtient 1 + 15 + 58 = 74.

Considérons la suite engendré par le polynôme de degré 10 suivant :

$`u_n = 1 − n + n^2 − n^3 + n^4 − n^5 + n^6 − n^7 + n^8 − n^9 + n^{10}`$

Trouver la somme des PTI engendrés par les MOP.

On affichera le résultat avec `print`.

@[Polynôme optimal]({"stubs": ["Defis/Euler_101.py"], "command": "python3 Defis/Euler_101_Test.py"})

---

# Point à l'intérieur d'un triangle
`Difficulté : Moyen (15%)`
`Origine : Projet Euler n°102`

Trois points distincts sont placés au hasard sur un plan cartésien pour lesquelles -1000 ≤ x, y ≤ 1000, et tels qu'un triangle soit formé.

Considzrons les eux triangles suivants :

A(-340,495), B(-153,-910), C(835,-947)  

X(-175,41), Y(-421,-714), Z(574,-645)  

On peut vérifier que le triangle ABC contient l'origine alors que XYZ ne la contient pas.

On donne ci-dessous une liste contenant les coordonnées des trois sommets de mille triangles. Trouver le nombre de triangles qui contiennent l'origine à l'intérieur.

On affichera le résultat avec `print`.

@[Point à l'intérieur d'un triangle]({"stubs": ["Defis/Euler_102.py"], "command": "python3 Defis/Euler_102_Test.py"})

---

# Ensembles de sommes spéciaux : Optimum
`Difficulté : Difficile (45%)`
`Origine : Projet Euler n°103`

Notons S(A) la somme des éléments d'un ensemble A de taille n. On dira que A est un ensemble de sommes spécial si pour tous ensembles disjoints B et C, on a les deux propriétés suivantes qui sont vérifiées :

    S(B) ≠ S(C) : c'est à dire que les sommes de sous ensembles sont toutes différentes
    Si B contient plus d'éléments que C alors S(B) > S(C)

Si S(A) est minimisée pour un n donné, on dira que l'ensemble de somme spécial est optimum. Les cinq premiers de ces ensembles sont :

n = 1: {1}  
n = 2: {1, 2}  
n = 3: {2, 3, 4}  
n = 4: {3, 5, 6, 7}  
n = 5: {6, 9, 11, 12, 13}  

Il semble que pour un ensemble optimum donné, $`A = \{a_1, a_2, ... , a_n\}`$, l'ensemble optimum  suivant est de la forme $`B= \{b, a_1+b, a_2+b, ... ,a_n+b\}`$, où b est l'élément au "milieu" de A.

En appliquant cette règle, on devrait s'attent à ce que l'optimum pour n=6 soit A = {11, 17, 20, 22, 23, 24}, avec S(A) = 117. Cependant, ce n'est pas un ensemble optimum car on peut trouve que l'ensemble optimum pour n=6 est A = {11, 18, 19, 20, 22, 25}, avec S(A) = 115 et qu'on peut lui faire correspond le nombre(créé en concaténant les valeurs de l'ensemble) 111819202225.

Trouver le nombre associé à l'ensemble optimum pour n=7.

Note : Ce problème est en relation avec le problème 105 et 106.

On affichera le résultat avec `print`.

@[Ensembles de sommes spéciaux : Optimum]({"stubs": ["Defis/Euler_103.py"], "command": "python3 Defis/Euler_103_Test.py"})

---

# Nombres de Fibonacci pandigitaux
`Difficulté : Moyen (25%)`
`Origine : Projet Euler n°104`

La suite de Fibonacci est définie par la relation de récurrence :

    $`F_n = F_{n−1} + F_{n−2}`$, où $`F_1 = 1`$ and $`F_2 = 1`$.
    
Le nombre $`F_{541}`$ qui possède 113 chiffres et le premier nombre de Fibonacco qui a ses 9 derniers chiffres qui forment un nombre 1-9 pandigital (C'est à dire qu'il contient exactement les chiffres de 1 à 9 mais pas forcément dans l'ordre). Le nombre $`F_{2749}`$ qui possède 575 chiffres, est le premier nombre de Fibonacci qui a ses neuf premiers chiffres qui forment un nombre 1-9 pandigital.

Trouver l'indice k du premier nombre de Fibonacci $`F_k`$ qui a, à la fois, ses neuf premiers chiffres qui forment un nombre 1-9 pandigital et ses 9 derniers chiffres aussi.

On affichera le résultat avec `print`.

@[Nombres de Fibonacci pandigitaux]({"stubs": ["Defis/Euler_104.py"], "command": "python3 Defis/Euler_104_Test.py"})

---

# Ensembles de sommes spéciaux : Testing
`Difficulté : Difficile (45%)`
`Origine : Projet Euler n°105`

Notons S(A) la somme des éléments d'un ensemble A de taille n. On dira que A est un ensemble de sommes spécial si pour tous ensembles disjoints B et C, on a les deux propriétés suivantes qui sont vérifiées :

    S(B) ≠ S(C) : c'est à dire que les sommes de sous ensembles sont toutes différentes
    Si B contient plus d'éléments que C alors S(B) > S(C)

Par exemple, {81, 88, 75, 42, 87, 84, 86, 65} n'est pas un ensemble de somme spécial car 65 + 87 + 88 = 75 + 81 + 84, alors que  {157, 150, 164, 119, 79, 159, 161, 139, 158} satisfait les deux règles pour toutes les pairs de sous-ensembles et S(A) = 1286.

A partir de la liste de cent ensembles donnée ci-dessous contenant entre 7 et 12 éléments, identifier tous les ensembles de sommes spéciaux A1, A2, ..., Ak, et trouver la valeur de S(A1) + S(A2) + ... + S(Ak).

Note : Ce problème est en relation avec le problème 103 et 106.

On affichera le résultat avec `print`.

@[Ensembles de sommes spéciaux : Testing]({"stubs": ["Defis/Euler_105.py"], "command": "python3 Defis/Euler_105_Test.py"})

---
