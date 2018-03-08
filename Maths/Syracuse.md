# Suite de Syracuse
`Difficulté : Moyenne`

### Calcul des termes de la suite 

La suite de Syracuse est une suite de nombre définie de la façon suivante : On part d'un nombre entier $`u_0`$ non nul, S'il est pair, on le divise par 2 et s'il est impair, on le multiplie par 3 et on ajoute 1. Et on recommence l'opération avec le résultat. On obtient ainsi une suite de nombres. Ce qui est remarquable avec cette suite, c'est que chaque fois qu'on a essayé avec un nombre, on est tombé sur 1 au bout d'un certain nombre d'essais mais personne n'a pour l'instant réussi à démontrer que c'était vrai pour tous les entiers. On peut aller voir [Wikipédia](https://fr.wikipedia.org/wiki/Conjecture_de_Syracuse) pour plus d'information.

Définissons un peu plus proprement notre suite. On débute avec un entier $`u_0=N`$ puis la relation de récurrence est :
```math
\left\{\begin{array}{ll} \frac {u_n}2& \textrm{si $u_n$ est pair} \\ 3.u_n+1 & \textrm{sinon}\end{array}\right.
```

Créez une fonction ***syracuse(N)*** qui prend en entrée un entier ***N*** et qui renvoie (avec `return`) la liste des termes de la suite de Syracuse commençant par le terme $`u_0=N`$ jusqu'au premier 1 obtenu.

::: Aide
On pourra utiliser une boucle while. Attention de bien s'arrêter au premier 1 obtenu.
:::

@[Suite de Syracuse]({"stubs": ["Maths/Syracuse.py"], "command": "python3 Maths/Syracuse_Test.py"})

