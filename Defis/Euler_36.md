# Palindromes dans deux bases
`Difficulté : Facile`
`Origine : Projet Euler n°36`

Le nombre (en base 10) 585 vaut 1001001001 en base 2. C'est palindrome dans les deux bases.

Trouver la somme de tous les nombres inférieurs à un million qui sont des palindromes dans les bases 10 et 2.

( On pourra remarquer qu'un nombre palindrome ne peut pas avoir de 0 en début de nombre, et ce dans aucune base.)

On affichera le résultat avec `print`.

@[Palindromes dans deux bases]({"stubs": ["Defis/Euler_36.py"], "command": "python3 Defis/Euler_36_Test.py"})

---

# Nombres premiers troncables
`Difficulté : Facile`
`Origine : Projet Euler n°37`

Le nombre 3797 a une propriété intéressante : Il est premier et en enlevant au fur et à mesure les chiffres de gauche à droite, on obtient encore des nombres premiers (797, 97 et 7) et de même en enlevant les chiffres de droite à gauche (379, 37 et 3).

Trouver la somme des onze nombres premiers qu'on peut ainsi tronquer de gauche à droite et de droite à gauche et qui donnent à chaque fois des nombres premiers.

NOTE: 2, 3, 5, et 7 ne sont pas considérés comme des nombres premiers troncables.

On affichera le résultat avec `print`.

@[Nombres premiers troncables]({"stubs": ["Defis/Euler_37.py"], "command": "python3 Defis/Euler_37_Test.py"})

---

# Multiples pandigitals (pandigitaux ?)
`Difficulté : Facile`
`Origine : Projet Euler n°38`

Prenons le nombre 192 et multiplions le par 1, 2 et 3. On obtient 

    192 × 1 = 192
    192 × 2 = 384
    192 × 3 = 576

En concaténant chaque produit, on obtient le nombre 1 à 9 pandigital 192384576. On va appeler 192384576 le produit concaténé de 192 et de (1,2,3)

On peut faire la même chose en commençant par 9 et en multipliant par 1, 2 ,3, 4 et 5 ce qui donne le nombre 1 à 9  pandigital  918273645, qui est le poduit concaténé de 9 et de (1,2,3,4,5).

Quel est le plus grand nombre 1 à 9 pandigital qui peut être formé comme un produit concaténé d'un entier et de (1,2, ... , n) où n > 1?

On affichera le résultat avec `print`.

@[Multiples pandigitals]({"stubs": ["Defis/Euler_38.py"], "command": "python3 Defis/Euler_38_Test.py"})

---


# Triangles rectangles de longueurs entières
`Difficulté : Facile`
`Origine : Projet Euler n°39`

Si p est le périmètre du'un triangle rectangle dont les côtés {a,b,c} sont de longueurs entières, il y a exactement trois solutions pour p=120 qui sont {20,48,52}, {24,45,51}, {30,40,50}.

Pour quelle valeur de p ≤ 1000, ce nombre de solution est-il maximal ?

On affichera le résultat avec `print`.

@[Triangles rectangles de longueurs entières]({"stubs": ["Defis/Euler_39.py"], "command": "python3 Defis/Euler_39_Test.py"})

---

# Constante de Champernowne
`Difficulté : Facile`
`Origine : Projet Euler n°40`

On peut créer nombre décimal irrationel en concaténant les entiers positifs comme suit :

0.1234567891***0***1112131415161718192021... (C'est la constante de Champernowne)

On peut voir que le 11e chiffre de la partie décimale est 0.

Si $`d_n`$ représente le n ième chiffre de la partie décimale, trouvez la valeur de l'expression suivante : 
If dn represents the nth digit of the fractional part, find the value of the following expression.

$`d_1 \times d_{10} \times d_{100}\times d_{1000}\times d_{10000}\times d_{100000}\times d_{1000000}`$

On affichera le résultat avec `print`.

@[Constante de Champernowne]({"stubs": ["Defis/Euler_40.py"], "command": "python3 Defis/Euler_40_Test.py"})
