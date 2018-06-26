# Equation Diophantienne
`Difficulté : Moyenne (25%)`
`Origine : Projet Euler n°66`

COnsidérons l'équation Diophantienne quadratique de la forme :
$`x^2-Dy^2=1`$.

Par exemple, quand $`D=13`$, la solution minimale en $`x`$ est $`649^2 – 13×180^2 = 1`$.

On admettra qu'il n'y a pas de solutions pour les entiers strictement positifs quand D est un carré.

En trouvant les solutions minimales en x pour D dans l'ensemble {2, 3, 5, 6, 7}, on obtient :

$`3^2 – 2×2^2 = 1`$  
$`2^2 – 3×1^2 = 1`$  
$`9^2 – 5×4^2 = 1`$  
$`5^2 – 6×2^2 = 1`$  
$`8^2 – 7×3^2 = 1`$  

Donc, en considérant les solutions minimales en x pour D ≤ 7, le plus grand x est obtenu pour D=5.

Trouver la valeur de D ≤ 1000 pour laquelle la valeur de x est maximale parmi les solutions minimale en x de l'équation considérée.

On affichera le résultat avec `print`.

@[Equation Diophantienne]({"stubs": ["Defis/Euler_66.py"], "command": "python3 Defis/Euler_66_Test.py"})

---

# Chemin de somme maximum II
`Difficulté : Facile`
`Origine : Projet Euler n°67`

A partir d'un nombre dans les triangles ci-dessous, on peut se déplacer uniquement vers le bas soit vers le nombre juste en dessous, soit vers le nombre à droite de celui qui est en dessous. Par exemple, à partir du 6, on peut descendre uniquement vers le 9 ou le 3 mais pas vers le 5.

En partant du sommet du triangle ci-dessous, le chemin dont le total en additionnant les nombres du chemin est le plus grand est 23.

***3***  
***7*** 4  
2 ***4*** 6  
8 5 ***9*** 3  

En effet, 3 + 7 + 4 + 9 = 23.

Trouver le chemin de somme maximum dans le triangle donné. (Le triangle est donné sous forme de chaine de caractère).

Note : L'énoncé est le même que le problème 18 à la différence près que cette fois ci le triangle a 100 lignes ce qui fait un total de 2^99 chemins. Même avec un ordinateur qui calcule 1000 milliard de chemins par seconde, il faudrait 20 milliard d'années pour tous les tester. Il vaut donc mieux refléchir à des stratégies plus efficaces.

On affichera le résultat avec `print`.

@[Chemin de somme maximum II]({"stubs": ["Defis/Euler_67.py"], "command": "python3 Defis/Euler_67_Test.py"})

---

# Pentagone magique
`Difficulté : Moyen(25%)`
`Origine : Projet Euler n°68`

Considérons le triangle magique suivant, rempli avec les nombres de 1 à 6 tel que chaque ligne a une somme qui vaut neuf.

![Triangle magique](https://projecteuler.net/project/images/p068_1.gif)

En tournant dans le sens des aiguilles d'une montre et en commençant par le groupe de trois qui a le noeud externe dont la valeur est la plus petite (4,3,2 dans cet exemple), chaque solution peut être décrite de manière unique. Par exemple, la solution ci-dessus peut être décrite par l'ensemble : 4,3,2; 6,2,1; 5,1,3 .

Il est possible de completer ce triangle avec quatre sommes différentes : 9, 10, 11 et 12. Il y a en tout huit solutions : 

Total	 Ensemble solution   
9	  4,2,3; 5,3,1; 6,1,2  
9	  4,3,2; 6,2,1; 5,1,3  
10	2,3,5; 4,5,1; 6,1,3  
10	2,5,3; 6,3,1; 4,1,5  
11	1,4,6; 3,6,2; 5,2,4  
11	1,6,4; 5,4,2; 3,2,6  
12	1,5,6; 2,6,4; 3,4,5  
12	1,6,5; 3,5,4; 2,4,6  

En concaténant chaque groupe, il est possible de former une chaine de caractère de 9 chiffres. La chaine maximum pour ce triangle magique est 432621513.

En utilisant des nombres de 1 à 10, selon l'arrangement, il est possible de former ainsi des chaines de 16 ou 17 chiffres. Quelle est la chaine de caractère maximum formée de 16 chiffres pour un pentagone magique ?

![Pentagone magique](https://projecteuler.net/project/images/p068_2.gif)

On affichera le résultat avec `print`.

@[Pentagone magique]({"stubs": ["Defis/Euler_68.py"], "command": "python3 Defis/Euler_68_Test.py"})

---

# Fonction phi d'Euler et maximum
`Difficulté : Moyen(10%)`
`Origine : Projet Euler n°69`

La fonction phi d'Euler, φ(n) est utilisée pour déterminer le nombre d'entiers inférieurs à n qui sont premiers avec  n. Par exemple, comme les entiers 1, 2, 4, 5, 7, et 8 sont tous inférieurs à 9 et premiers avec 9, on a φ(9)=6.

| n | premiers avec n | φ(n)| n/φ(n) |
| ------ | ----------- | ---- | ---- |
| 2 | 1 | 1 | 2 |
| 3 | 1,2 | 2 | 1.5 |
| 4 | 1,3 | 2 | 2 |
| 5 |	1,2,3,4 |	4 |	1.25 |
| 6 |	1,5 |	2 |	3 |
| 7 |	1,2,3,4,5,6 |	6 |	1.1666... |
| 8 |	1,3,5,7 |	4 |	2 |
| 9 |	1,2,4,5,7,8 |	6 |	1.5 |
| 10 | 1,3,7,9 | 4 |	2.5 |

On peut voir que pour n=6, la valeur de n/φ(n) est maximum pour n ≤ 10.

Trouver la valeur de n ≤ 1,000,000 pour laquelle n/φ(n) est maximum.


On affichera le résultat avec `print`.

@[Fonction phi d'Euler et maximum]({"stubs": ["Defis/Euler_69.py"], "command": "python3 Defis/Euler_69_Test.py"})

---
