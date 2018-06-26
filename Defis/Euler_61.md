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

# Puissances et nombre de chiffres
`Difficulté : Facile`
`Origine : Projet Euler n°63`

Le nombre de cinq chiffres $`16807=7^5`$ est aussi une puissance 5-ième. De même, le nombre de 9 chiffres $`134217728=8^9`$ est une puissance 9-ième.

Combien existe-t-il de nombres entiers strictement positifs de n-chiffres qui sont aussi des puissances n-ième ?

On affichera le résultat avec `print`.

@[Puissances et nombres de chiffres]({"stubs": ["Defis/Euler_63.py"], "command": "python3 Defis/Euler_63_Test.py"})

---

# Racines carrées de période impaire
`Difficulté : Moyen(20%)`
`Origine : Projet Euler n°64`

Toutes les racines carrées sont périodiques quand elles sont écrites sous forme de fractions continues c'est à dire sous la forme : 

$`\sqrt N = a_0+\dfrac{1}{a_1+\frac{1}{a_2+\frac{1}{a_3+\dots}}}`$

Par exemple :

$`\sqrt{23}=4+\sqrt{23}-4= 4+\dfrac{1}{\frac{1}{\sqrt{23}-4} }= 4 + \dfrac{1}{1+\frac{\sqrt{23}-3}{7}}`$

Si on continue, on obtiendrait le développement suivant :  
$`\sqrt{23} = 1+\dfrac{1}{1+\frac{1}{3+\frac{1}{1+\frac 1{8+\dots}}}}`$

Le processus peut être résumé comme suit :

$`a_0=4`$, $`\dfrac 1{\sqrt{23}-4}=\dfrac{\sqrt{23}+4} 7= 1+\dfrac{\sqrt{23}-3}7`$  
$`a_1=1`$, $`\dfrac 7{\sqrt{23}-3}=\dfrac{7(\sqrt{23}+3)}{14}=3+\dfrac{\sqrt{23}-3}{2}`$  
$`a_2=3`$, $`\dfrac 72{\sqrt{23}-3}=\dfrac{2(\sqrt{23}+3)}{14}=1+\dfrac{\sqrt{23}-4}{7}`$  
$`a_3=1`$, $`\dfrac 7{\sqrt{23}-4}=\dfrac{7(\sqrt{23}+4)}{7}=8+\sqrt{23}-4`$  
$`a_4=8`$, $`\dfrac 1{\sqrt{23}-4}=\dfrac{\sqrt{23}+4} 7= 1+\dfrac{\sqrt{23}-3}7`$  
$`a_5=1`$, $`\dfrac 7{\sqrt{23}-3}=\dfrac{7(\sqrt{23}+3)}{14}=3+\dfrac{\sqrt{23}-3}{2}`$  
$`a_6=3`$, $`\dfrac 72{\sqrt{23}-3}=\dfrac{2(\sqrt{23}+3)}{14}=1+\dfrac{\sqrt{23}-4}{7}`$  
$`a_7=1`$, $`\dfrac 7{\sqrt{23}-4}=\dfrac{7(\sqrt{23}+4)}{7}=8+\sqrt{23}-4`$  

Les dix premieres représentations en fraction continue des racines carrées (irrationnelles) sont : 

$`\sqrt 2=[1;(2)]`$, periode=1  
$`\sqrt 3=[1;(1,2)]`$, periode=2  
$`\sqrt 5=[2;(4)]`$, periode=1  
$`\sqrt 6=[2;(2,4)]`$, periode=2  
$`\sqrt 7=[2;(1,1,1,4)]`$, periode=4  
$`\sqrt 8=[2;(1,4)]`$, periode=2  
$`\sqrt{10}=[3;(6)]`$, periode=1  
$`\sqrt{11}=[3;(3,6)]`$, periode=2  
$`\sqrt{12}= [3;(2,6)]`$, periode=2  
$`\sqrt {13}=[3;(1,1,1,1,6)]`$, periode=5  

Exactement quatre fractions continues pour N ≤ 13 ont une période impaire.

Combien de fractions continues pour N ≤ 10000 ont une période impaire ?

On affichera le résultat avec `print`.

@[Racines carrées de période impaire]({"stubs": ["Defis/Euler_64.py"], "command": "python3 Defis/Euler_64_Test.py"})

---
