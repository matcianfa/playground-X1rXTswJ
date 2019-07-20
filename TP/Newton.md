# La méthode de Newton
`Difficulté : Moyenne à difficile`   
`Prérequis : Notion de dérivée`

Le but de cette page est de présenter la méthode de Newton pour rechercher les solutions d'une équation de la forme $`f(x)=0`$. Cette méthode ne fonctionne pas toujours parfaitement (selon la situation qu'on pourrait souvent contourner mais nous n'en parlerons pas ici) mais quand elle fonctionne, elle donne rapidement la solution. Pour donner un ordre d'idée grossier, une recherche par dichotomie (qui est déjà efficace) divise l'erreur par 2 alors que dans les cas favorables, la méthode de Newton va quasiment doubler le nombre de décimales justes. Autrement dit, il faut beaucoup moins de calcul pour obtenir le résultat ce qui est indispensable en programmation.

## Calcul du nombre dérivé (version améliorée)

Pour utiliser la méthode de Newton, nous aurons besoin d'avoir le nombre dérivé d'une fonction. Une première façon de faire est d'utiliser une conséquence de la définition du nombre dérivé : $`f'(a)\approx \dfrac{f(a+h)-f(a)}{h}`$. 

Or une petite astuce toute simple donne de bien meilleurs résultats dans les cas favorables (mais dans certains cas ne marchera pas du tout mais nous n'allons pas en croiser ici). On va utiliser le résultat : $`f'(a)\approx \dfrac{f(a+\frac h 2 )-f(a-\frac h 2 )}{h}`$.  Cette simple astuce permet de doubler la précision. C'est ce qu'on appelle la méthode des [différences finies](https://fr.wikipedia.org/wiki/Diff%C3%A9rence_finie). Elle est souvent utilisée dans les logiciels de calcul formel pour calculer les nombres dérivées.

Créer une fonction `deriver(f,a,h)` qui donne le nombre dérivé de f en a en utilisant la méthode des différences finies.

@[Calcul du nombre dérivé]({"stubs": ["TP/diff_finie.py"], "command": "python3 TP/diff_finie_Test.py"})

---

## La méthode de Newton

Passons à présent aux choses sérieuses : On cherche à trouver une approximation d'une solution de l'équation $`f(x)=0`$ pour une fonction $`f`$ donnée. L'idée est, comme sur la figure ci-dessous, de :
![Méthode de Newton](https://upload.wikimedia.org/wikipedia/commons/e/e0/NewtonIteration_Ani.gif)
- prendre un point d'abscisse $`x_0`$ (pas trop loin de là où on imagine que la solution se trouve), 
- tracer la tangente à la courbe représentative de $`f`$ et regarder pour quelle valeur $`x_1`$ la tangente coupe l'axe des abscisses
- On considère alors le point de la courbe représentative de $`f`$ ayant pour abscisse cette valeur trouvée $`x_1`$ dans l'étape précédente et on recommence...

> Question mathématique : Prouver que la méthode revient à considérer la suite des abscisses $`(x_n)`$ définie par la relation de récurrence $`x_{n+1}=x_n-\dfrac{f(x_k)}{f'(x_k)}`$.

Créer une fonction `Newton(f,x0,n)` qui calcule la valeur de $`x_n`$ definie juste avant en prenant comme valeur initiale x0.
Pour cela vous devrez faire un copier coller de votre fonction `deriver` précédente. On fixera la valeur de `h` pour le calcul du nombre dérivé à 0.000001.

> Remarque : Les tests sont faits avec n=5 seulement. On pourra remarquer la précision de l'approximation obtenue en calculant seulement $`x_5`$. C'est cette rapidité de convergence qui fait la force de cette méthode.

@[Méthode de Newton]({"stubs": ["TP/Newton.py"], "command": "python3 TP/Newton_Test.py"})

---

## Pour aller plus loin
`Difficulté : Difficile`

Créer ci-dessous un script qui permet d'afficher graphiquement la fonction ainsi que les 5 tangentes successives de la méthode de Newton.

Pour cela, on utilisera le module [matplotlib](https://tech.io/playgrounds/17176/recueil-dexercices-pour-apprendre-python-au-lycee/cours---representation-graphique-avec-matplotlib) et les fonctions précédentes (en les modifiant si besoin)

> Remarques : La fonction f et la valeur de départ sont données pour l'exemple mais vous pouvez les modifier pour observer d'autres cas.  
Cette fenêtre n'a pas d'auto correction, le résultat étant visuel, vous devriez voir si cela fonctionne ou pas.

@[Méthode de Newton - Graphique]({"stubs": ["TP/Newton_graphique.py"], "command": "python3 TP/Newton_graphique_Test.py"})
