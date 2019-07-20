# La méthode d'Euler pour représenter la fonction exponentielle.

La fonction exponentielle est définie comme la fonction vérifiant $`f(0)=1`$ et $`f'(x)=f(x)`$ pour tout réel ***x***. On souhaite tracer la courbe représentative de ***f*** à partir de ces informations. Pour cela nous allons utiliser la méthode d'Euler.

La méthode d'Euler consiste à construire une suite de points $`A_n`$ dont les coordonnées seront notées $`(x_n,y_n)`$ de la manière suivante : 
1. $`A_0`$ est le point de la courbe qu'on connait c'est à dire le point de coordonnées $`(0,1)`$.
2. Les abscisses $`x_n`$ augmente de toujours la même valeur qu'on notera ***pas***. Autrement dit $`x_{n+1}=x_n+pas`$.
3. Pour construire $`A_1`$, on va utiliser le fait que la tangente en $`A_0`$ est une bonne approximation de la courbe. Or on connait mieux ici la tangente que la courbe puisque son coefficient directeur est $`f'(0)=f(0)=y_0=1`$. Donc en écrivant le taux d'accroissement, on a $`f'(0)\approx \frac {y_1-y_0}{x_1-x_0}=\frac{y_1-y_0}{pas}`$. On en déduit $`y_1=f'(0).pas+y_0=pas+1`$ puisque $`f'(0)=f(0)=y_0=1`$.
4. Pour construire $`A_2`$, on réitère le même procédé mais en partant de $`A_1`$. On a $`f'(1)\approx \frac {y_2-y_1}{x_1-x_0}=\frac{y_2-y_1}{pas}`$. On en déduit $`y_2=f'(1).pas+y_1=y_1(pas+1)=(pas+1)^2`$ puisque $`f'(1)=f(1)\approx y_1`$.
5. On continue ainsi la construction des points $`A_n`$ dont les coordonnées sont finalement $`x_n=n.pas`$ et $`y_n=(pas+1)^n`$. Voici une représentation de la situation :
![méthode d'Euler](https://www.ilemaths.net/img/forum_img/0450/forum_450471_1.PNG)
6. Une fois cette liste de points établie, on les relie par des segments.

Créer un programme qui prend en entrée un ***pas*** et le nombre ***n*** de segments à construire et qui trace la courbe approximative de la fonction exponentielle. Pour pouvoir vérifier la validité du programme, on demande en plus de renvoyer (avec `return`) la liste des ordonnées des points $`A_n`$.

Pour tracer la courbe, on utilisera la fonction `plt.plot(liste_x, liste_y)` qui demande la liste ***liste_x*** de toutes les abscisses des points à tracer et la liste ***liste_y*** des ordonnées des points à tracer. On pourra trouver sur internet plein d'options de modification (couleur, façon de tracer, de marquer les points etc.) de la fonction `plt.plot`.

> Entrée : un réel ***pas*** et un entier ***n***.

> Sortie : Un programme qui trace ***n*** segments de l'approximation de la courbe représentative de l'exponentielle par la méthode d'Euler de pas valant ***pas***. Pour pouvoir vérifier la validité du programme, il faudra de plus renvoyer (avec `return`) la liste ***liste_y*** des ordonnées des points tracés.

En rouge est tracé la courbe exacte de la fonction exponentielle.

@[Tracé de l'exponentielle par la méthode d'Euler]({"stubs": ["Maths/Euler_plot.py"], "command": "python3 Maths/Euler_plot_Test.py"})

# Approximation du nombre e

La méthode d'Euler nous permet d'obtenir les valeurs de la fonction exponentielle de proche en proche. On va l'utiliser ici pour obtenir plus particulièrement la valeur de $`e = exp(1)`$. Pour cela, nous allons reprendre les formules obtenues dans l'étape 5 :  $`x_n=n.pas`$ et $`y_n=(pas+1)^n`$.

Si on veut que $`y_n`$ nous donne la valeur approximative de $`e`$, il faut que $`x_n=n.pas`$ soit égal à 1. Autrement dit $`pas= \dfrac 1 n`$ ce qui donne en remplaçant $`y_n = \left( 1+\dfrac1 n\right)^n`$.

En utilisant cette formule, créer une fonction qui prend en entrée $`n`$ et donne en sortie une approximation de $`e`$.

@[Approximation de e]({"stubs": ["Maths/approx_e.py"], "command": "python3 Maths/approx_e_Test.py"})
