# Polynôme optimal
`Difficulté : Moyen (35%)`
`Origine : Projet Euler n°101`

Si on nous donne les k premiers termes d'une suite, il est impossible de dire avec certitude la valeur du terme suivant car il y a une infinité de polynomes qui peut modéliser la suite.

Prenons comme exemple la suite des cubes. Elle est définie par la fonction génératrice  $`u_n=n^3`$ et donne :  1, 8, 27, 64, 125, 216, ...

Supponsons qu'on connaisse uniquement les 2 premiers termes de la suite. En utilisant le principe "le plus simple est le meilleurs", on peut considérer une relation linéaire et prédire que le terme suivant sera 15 (on ajoute 7 ). Mais si on nous avait donné les trois premiers termes de la suite, par le même principe de simplicité, on aurait pu supposer que la relation était du second degré.

On peut définir OP(k,n) comme étant le n-ieme terme de la suite associée au polynome optimal pour les k premier termes d'une suite donnée. Il est clair que OP(k,n) va exactement engendrer les termes de cette suite pour n ≤ k, et potentiellement le premier terme incorrect (PTI) sera OP(k,k+1) et dans ce cas, on l'appellera le mauvais OP (MOP).

Au départ, si on ne nous donne qu'un terme de la suite, le plus simple sera de considérer un constante. Donc pour n ≥ 2, OP(1, n) = u1.

Ainsi, on obtient les OP pour la suite des cubes :

$`OP(1, n) = 1`$ 	              ***1***, 1, 1, 1, ...  
$`OP(2, n) = 7n−6`$ 	          1, 8, ***15***, ...  
$`OP(3, n) = 6n^2−11n+6`$      	1, 8, 27, ***58***, ...  
$`OP(4, n) = n^3`$ 	            1, 8, 27, 64, 125, ...  

Clairement, il n'y a pas de MOP pour k ≥ 4.

En considérant la somme des PTI engendrés par les MOP (indiqué en gras ci dessus), on obtient 1 + 15 + 58 = 74.

Considérons la suite engendré par le polynôme de degré 10 suivant :

$`u_n = 1 − n + n^2 − n^3 + n^4 − n^5 + n^6 − n^7 + n^8 − n^9 + n^{10}`$

Trouver la somme des PTI engendrés par les MOP.

On affichera le résultat avec `print`.

@[Polynôme optimal]({"stubs": ["Defis/Euler_101.py"], "command": "python3 Defis/Euler_101_Test.py"})

---
