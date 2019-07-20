# La méthode de Newton
`Difficulté : Moyenne à difficile`   
`Prérequis : Notion de dérivée`

Le but de cette page est de présenter la méthode de Newton pour rechercher les solutions d'une équation de la forme $`f(x)=0`$. Cette méthode ne fonctionne pas toujours parfaitement (selon la situation qu'on pourrait souvent contourner mais nous n'en parlerons pas ici) mais quand elle fonctionne, elle donne rapidement la solution. Pour donner un ordre d'idée grossier, une recherche par dichotomie (qui est déjà efficace) divise l'erreur par 2 alors que dans les cas favorables, la méthode de Newton va quasiment doubler le nombre de décimales justes. Autrement dit, il faut beaucoup moins de calcul pour obtenir le résultat ce qui est indispensable en programmation.

## Calcul du nombre dérivé (version améliorer)

Pour utiliser la méthode de Newton, nous aurons besoin d'avoir le nombre dérivé d'une fonction. Une première façon de faire est d'utiliser une conséquence de la définition du nombre dérivé : $`f'(a)\approx \dfrac{f(a+h)-f(a)}{h}`$. 

Or une petite astuce toute simple donne de bien meilleurs résultats dans les cas favorables (mais dans certains cas ne marchera pas du tout mais nous n'allons pas en croiser ici). On va utiliser le résultat : $`f'(a)\approx \dfrac{f(a+\frac 1 2 h)-f(a-\frac 1 2 h)}{h}`$.  Cette simple astuce permet de doubler la précision. C'est ce qu'on appelle la méthode des [différences finies](https://fr.wikipedia.org/wiki/Diff%C3%A9rence_finie). Elle est souvent utilisée dans les logiciels de calcul formel pour calculer les nombres dérivées.

Créer une fonction `deriver(f,a,h)` qui donne le nombre dérivé de f en a en utilisant la méthode des différences finies.

@[Calcul du nombre dérivé]({"stubs": ["TP/diff_finie.py"], "command": "python3 TP/diff_finie_Test.py"})

---


