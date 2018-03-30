# Nombres amicaux
`Difficulté : Facile`
`Origine : Projet Euler n°21`

On note d(n) la somme des diviseurs propres de n (c'est à dire les diviseurs de n différents de n).  
Si pour deux nombres a ≠ b, on a d(a)=d(b), on dit que les nombres a et b sont amicaux.

Par exemple, les diviseurs propres de 220 sont 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 et 110; on a donc d(220) = 284. Les diviseurs propres de 284 son 1, 2, 4, 71 and 142; d'où d(284) = 220.  
220 et 284 sont donc des nombres amicaux.

Trouver la somme de tous les nombres amicaux inférieurs à 10000.

On affichera le résultat avec `print`.

@[Nombres amicaux]({"stubs": ["Defis/Euler_21.py"], "command": "python3 Defis/Euler_21_Test.py"})

---

# Score de noms
`Difficulté : Facile`
`Origine : Projet Euler n°22`

Dans la ***liste*** donnée ci-dessous, il y a 500 prénoms. Il faut d'abord la trier par ordre alphabetique. Il faut ensuite pour chaque prénom calculer son score qui est la somme des valeurs de chaque lettre (avec A=1, B=2...) multipliée par sa position dans la ***liste*** (en commençant par 1 pour le premier nom).

Par exemple, quand la liste est triée par ordre alphabétique, COLIN dont la somme des valeurs des lettres est 3 + 15 + 12 + 9 + 14 = 53 est à la 938e position dans la liste. Donc, COLIN a un score de 938 × 53 = 49714.

Quelle est la somme totale des scores de tous les prénoms de la ***liste*** ?

On affichera le résultat avec `print`.

@[Score de noms]({"stubs": ["Defis/Euler_22.py"], "command": "python3 Defis/Euler_22_Test.py"})

---

# Sommes non abondantes
`Difficulté : Facile`
`Origine : Projet Euler n°23`
 
Un nombre n est dit abondant si la somme de ses diviseurs propres (c'est à dire les diviseurs positif différents de n) est plus grande strictement que n.

Par exemple 12 est un nombre abondant car 1+2+3+4+6=16. C'est même le plus petit.

On va s'intéresser aux nombres qui sont la somme de deux nombres abondants. Comme 12 est le plus petit nombre abondant, 24 est le plus petit nombre qui peut s'écrire comme une somme de deux nombres abondants. On peut démontrer par une analyse mathématique que tous les nombres plus grands que 28123 peuvent s'écrire comme la somme de deux nombres abondants.

Trouver la somme de tous les entiers positifs qui ne peuvent pas s'écrire comme la somme de deux nombres abondants.

On affichera le résultat avec `print`.

Remarque : Il va peut-être falloir optimiser votre code pour qu'il finisse dans les temps.

@[Sommes non abondantes]({"stubs": ["Defis/Euler_23.py"], "command": "python3 Defis/Euler_23_Test.py"})

---

# Permutations lexicographiques
`Difficulté : Facile`
`Origine : Projet Euler n°24`

Une permutation est un arrangement ordonné d'objets. Par exemple, 3124 est une permutation possible des chiffres 1, 2 , 3 et 4. Si on énumère toutes les permutations de la plus petite à la plus grande, on appelle cela l'ordre lexicographique. Les permutations lexicographiques de 0, 1, et 2 sont : 

012   021   102   120   201   210

Quelle est la millionième permutation lexicographique de 0, 1, 2, 3, 4, 5, 6, 7, 8 et 9?

On affichera le résultat avec `print`.


@[Permutations lexicographiques]({"stubs": ["Defis/Euler_24.py"], "command": "python3 Defis/Euler_24_Test.py"})

---

# Nombre de Fibonacci ayant 1000 chiffres
`Difficulté : Facile`
`Origine : Projet Euler n°25`

La suite de Fibonacci est définie par la relation de récurrence :

    $`F_n = F_{n−1} + F_{n−2}`$, où  $`F_1 = 1`$ and $`F_2 = 1`$

Ainse les 12 premiers termes seront :

    F1 = 1
    F2 = 1
    F3 = 2
    F4 = 3
    F5 = 5
    F6 = 8
    F7 = 13
    F8 = 21
    F9 = 34
    F10 = 55
    F11 = 89
    F12 = 144

Le douzième terme est le premier terme de la suite ayant 3 chiffres.

Quel est l'indice du premier terme dans la suite de Fibonacci à contenir 1000 chiffres ?

On affichera le résultat avec `print`.

@[Nombre de Fibonacci ayant 1000 chiffres]({"stubs": ["Defis/Euler_25.py"], "command": "python3 Defis/Euler_25_Test.py"})

