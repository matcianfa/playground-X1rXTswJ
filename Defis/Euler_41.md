# Nombre premier pandigital
`Difficulté : Facile`
`Origine : Projet Euler n°41`

On dit qu'un nombre de n chiffres est pandigital si il utilise tous les chiffres de 1 à n une fois exactement. Par exemple, 2143 est un nombre pandigital de 4 chiffres et il est de plus premier.

Quel est le plus grand nombre premier pandigital de n chiffres existant ?

On affichera le résultat avec `print`.

@[Nombre premier pandigital]({"stubs": ["Defis/Euler_41.py"], "command": "python3 Defis/Euler_41_Test.py"})

---

# Nombres triangulaires codés
`Difficulté : Facile`
`Origine : Projet Euler n°42`

Le n ième terme de la suite des nombres triangulaires est donné par $`t_n=\frac{n(n+1)}2`$. Ainsi, les dix premiers nombres triangulaires sont :

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

En convertissant chaque lettre d'un mot en un nombre correspondant à sa position alphabetique et en additionant ces valeurs, on forme la valeur d'un mot. Par exemple la valeur du mot SKY est $`19 + 11 + 25 = 55 = t_{10}`$. Si la valeur du mot est un nombre triangulaire, on peut appeler ce mot un mot triangulaire.

Dans la liste de mots donnée qui contient près de 200 mots communs en anglais, combien sont des mots triangulaires ?

On affichera le résultat avec `print`.

@[Nombres triangulaires codés]({"stubs": ["Defis/Euler_42.py"], "command": "python3 Defis/Euler_42_Test.py"})

---

# Divisibilité de sous-chaines
`Difficulté : Facile`
`Origine : Projet Euler n°43`

Le nombre 1406357289 est un nombre 0 à 9 pandigital car il est composé des chiffres de 0 à 9 une et une seule fois mais il a aussi une propriété de divisibilité de ses sous-chaines intéressante :

Si on $`d_n`$ le n-ième chiffre, on remarque que :

$`d_2d_3d_4=406`$ est divisible par 2
$`d_3d_4d_5=063`$ est divisible par 3
$`d_4d_5d_6=635`$ est divisible par 5
$`d_5d_6d_7=357`$ est divisible par 7
$`d_6d_7d_8=572`$ est divisible par 11
$`d_7d_8d_9=728`$ est divisible par 13
$`d_8d_9d_{10}=289`$ est divisible par 17
    
Trouver la somme de tous les nombres 0 à 9 pandigitals ayant cette propriété

On affichera le résultat avec `print`.

@[Divisibilité de sous-chaines]({"stubs": ["Defis/Euler_43.py"], "command": "python3 Defis/Euler_43_Test.py"})

---

# Nombres pentagonaux
`Difficulté : Facile`
`Origine : Projet Euler n°44`

Un nombre pentagonal est donné par la formule $`P_n=\frac{n(3n-1)}2`$. Les dix premiers nombres pentagonaux sont :

1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...

On peut remarqur que $`P_4+ P_7=22+70 = 92 = P_8`$. Cependant, leur différence, 70 - 22 = 48, n'est pas pentagonale.

Trouver la pair de nombres pentagonaux $`P_j`$ et $`P_k`$ tels que leur somme et leur différence sont pentagonal et $`D = |Pk − Pj|`$ est la plus petite; donner la valeur de D.

::: Indications
On pourra considérer que le premier trouvé est le bon.  
On pourra utiliser les ensembles au lieu des listes pour gagner en vitesse, ce qui ne sera pas un luxe.
:::

On affichera le résultat avec `print`.

@[Nombres pentagonaux]({"stubs": ["Defis/Euler_44.py"], "command": "python3 Defis/Euler_44_Test.py"})

---

# Nombres triangulaires, pentagonaux et hexagonaux
`Difficulté : Facile`
`Origine : Projet Euler n°45`

Les nombres triangulaires, pentagonaux et hexagonaux sont donnés par les formules suivantes :

Triangulaire 	$`T_n=\frac{n(n+1)}2 `$	  	    1, 3, 6, 10, 15, ...  
Pentagonaux 	$`P_n=\frac{n(3n−1)}2`$         1, 5, 12, 22, 35, ...  
Hexagonaux 	  	$`H_n=n(2n−1)`$         	  	1, 6, 15, 28, 45, ...  

On peut vérifier que $`T_{285}=P_{165}=H_{143}=40755`$.

Trouver le nombre triangulaire suivant qui est aussi pentagonal et hexagonal.

On affichera le résultat avec `print`.

@[Nombres triangulaires, pentagonaux et hexagonaux]({"stubs": ["Defis/Euler_45.py"], "command": "python3 Defis/Euler_45_Test.py"})
