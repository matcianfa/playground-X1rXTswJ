# Equation Diophantienne
`Difficulté : Moyenne (25%)`
`Origine : Projet Euler n°66`

COnsidérons l'équation Diophantienne quadratique de la forme :
$`x^2-Dy^2=1`$.

Par exemple, quand $`D=13`$, la solution minimale en $`x`$ est $ 6492 – 13×1802 = 1`$.

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
