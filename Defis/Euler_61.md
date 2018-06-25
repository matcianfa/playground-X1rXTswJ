# Nombres polygonaux cycliques
`Difficulté : Moyen (20%)`
`Origine : Projet Euler n°61`

Les nombres triangulaires, carrés, pentagonaux, hexagonaux, heptagonaux et octogonaux sont des nombres polygonaux donnés par les formules suivantes :

- Triangulaires : $`P_{3,n}=\dfrac{n(n+1)}{2}`$     
1, 3, 6, 10, 15, ...
- Carrés : $`P_{4,n}=n^2`$                          
1, 4, 9, 16, 25, ...
- Pentagonaux : $`P_{5,n}=\dfrac{n(3n-1)}{2}`$      
1, 5, 12, 22, 35, ...
- Hexagonaux : $`P_{6,n}=n(2n-1)`$                  
1, 6, 15, 28, 45, ...
- Heptagonaux : $`P_{7,n}=\dfrac{n(5n-3)}{2}`$      
1, 7, 18, 34, 55, ...
- Octogonaux : $`P_{8,n}=n(3n-2)`$                  
1, 8, 21, 40, 65, ...

Les 3 nombres de quatre chiffres 8128, 2882 et 8281 possède trois propriétés intéressantes :
1. Ils sont cycliques au sens suivant : les deux derniers chiffres de chaque nombre sont les deux premiers du nombre suivant ( y compris le dernier avec le premier)
2. Chaque nombre polygonal est représenté par un nombre différent : Triangulaire ($`P_{3,127}=8128`$), Carré ($`P_{4,91}=8281`$) et Pentagonal ($`P_{5,44}=2882`$).
3. C'est le seul ensemble de nombre à quatre chiffres qui a cette propriété.

Trouver la somme de l'unique ensemble de six nombres de quatre chiffres qui forment un ensemble cyclique (comme présenté dans l'exemple) et tel que chaque type de polygone soit représenté une et une seule fois (Triangulaire, carré,..., Octogonal)

On affichera le résultat avec `print`.

@[Nombres polygonaux cycliques]({"stubs": ["Defis/Euler_61.py"], "command": "python3 Defis/Euler_61_Test.py"})

---

# Permutations cubiques
`Difficulté : Moyen (15%)`
`Origine : Projet Euler n°62`

Le cube 41063625 ($`3453^3`$) peut être permuté pour produire deux autres cubes 56623104 ($`384^3`$) and 66430125 ($`405^3`$). En fait, 41063625 est le plus petit cube ayant exactement trois permutations de ses chiffres qui sont des cubes.

Trouver le plus petit cube qui a exactement cinq permutations de ses chiffres qui sont des cubes.

On affichera le résultat avec `print`.

@[Permutations cubiques]({"stubs": ["Defis/Euler_62.py"], "command": "python3 Defis/Euler_62_Test.py"})

---
