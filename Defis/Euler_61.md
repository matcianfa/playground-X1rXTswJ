# Nombres polygonaux cycliques
`Difficulté : Moyen (20%)`
`Origine : Projet Euler n°61`

Les nombres triangulaires, carrés, pentagonaux, hexagonaux, heptagonaux et octogonaux sont des nombres polygonaux donnés par les formules suivantes :

- Triangulaires : $`P_{3,n}=\dfrac{n(n+1)}{2}`$     1, 3, 6, 10, 15, ...
- Carrés : $`P_{4,n}=n^2`$                          1, 4, 9, 16, 25, ...
- Pentagonaux : $`P_{5,n}=\dfrac{n(3n-1)}{2}`$      1, 5, 12, 22, 35, ...
- Hexagonaux : $`P_{6,n}=n(2n-1)`$                  1, 6, 15, 28, 45, ...
- Heptagonaux : $`P_{7,n}=\dfrac{n(5n-3)}{2}`$      1, 7, 18, 34, 55, ...
- Octogonaux : $`P_{8,n}=n(3n-2)`$                  1, 8, 21, 40, 65, ...

Les 3 nombres de quatre chiffres 8128, 2882 et 8281 possède trois propriétés intéressantes :
1. Ils sont cycliques au sens suivant : les deux derniers chiffres de chaque nombre sont les deux premiers du nombre suivant ( y compris le dernier avec le premier)
2. Chaque nombre polygonal est représenté par un nombre différent : Triangulaire ($`P_{3,127}=8128`$), Carré ($`P_{4,91}=8281`$) et Pentagonal ($`P_{5,44}=2882`$).
3. C'est le seul ensemble de nombre à quatre chiffres qui a cette propriété.

Trouver la somme de l'unique ensemble de six nombres de quatre chiffres qui forment un ensemble cyclique (comme présenté dans l'exemple) et tel que chaque type de polygone soit représenté une et une seule fois (Triangulaire, carré,..., Octogonal)

On affichera le résultat avec `print`.

@[Nombres cycliques associés à une figure]({"stubs": ["Defis/Euler_61.py"], "command": "python3 Defis/Euler_61_Test.py"})

---
