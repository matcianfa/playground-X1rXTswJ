# Suite de Syracuse
`Difficulté : Moyenne`

### Calcul des termes de la suite 

La suite de Syracuse est une suite de nombre définie de la façon suivante : On part d'un nombre entier $`u_0`$ non nul, S'il est pair, on le divise par 2 et s'il est impair, on le multiplie par 3 et on ajoute 1. Et on recommence l'opération avec le résultat. On obtient ainsi une suite de nombres. Ce qui est remarquable avec cette suite, c'est que chaque fois qu'on a essayé avec un nombre, on est tombé sur 1 au bout d'un certain nombre d'essais mais personne n'a pour l'instant réussi à démontrer que c'était vrai pour tous les entiers. On peut aller voir [Wikipédia](https://fr.wikipedia.org/wiki/Conjecture_de_Syracuse) pour plus d'information.

Définissons un peu plus proprement notre suite. On débute avec un entier $`u_0=N`$ puis la relation de récurrence est :
```math
\left\{\begin{array}{ll} \frac {u_n}2& \textrm{si $u_n$ est pair} \\ 3u_n+1 & \textrm{sinon}\end{array}\right.
```

Créez une fonction ***syracuse(N)*** qui prend en entrée un entier ***N*** et qui renvoie (avec `return`) la liste des termes de la suite de Syracuse commençant par le terme $`u_0=N`$ jusqu'au premier 1 obtenu.

::: Aide
On pourra utiliser une boucle while. Attention de bien s'arrêter au premier 1 obtenu.
:::

@[Suite de Syracuse]({"stubs": ["Maths/Syracuse.py"], "command": "python3 Maths/Syracuse_Test.py"})

---

### Représentation graphique

Pour voir un peu mieux l'évolution des termes de la suite, on peut les représenter graphiquement.

Copiez collez votre fonction ***syracuse*** précédente dans la fenêtre ci-dessous et modifiez les valeurs de ***N*** pour voir la représentation de la suite de Syracuse qui commence par ***N***.

@[Suite de Syracuse]({"stubs": ["Maths/Syracuse_plot.py"], "command": "python3 Maths/Syracuse_plot_Test.py"})

---

### Temps de vol et altitude maximale

Si vous testez avec les valeurs N=126 ou N=128 le programme précédent, vous verrez que des nombres très proches donnent des courbes très différentes. Deux questions viennent naturellement à l'esprit quand on regarde ces courbes : Quels nombres donnent montent le plus haut ? Et quels nombres mettent le plus de temps à tomber à 1 ?

C'est pour répondre à ces questions que nous allons nous intéresser  
+ à l'altitude d'un nombre N qui est la valeur la plus haute qu'atteint la suite de syracuse lorsqu'on commence à N 
+ au temps de vol d'un nombre N qui est la plus petite valeur de ***n*** pour laquelle la suite qui commence par N prend la valeur 1.

Créez une fonction ***données(N)*** qui affiche (avec `print(altitude,temps_de_vol)`) l'altitude et le temps de vol (séparés d'un espace) pour la suite dont le premier terme est ***N***

@[Calcul de l'altitude et du temps de vol]({"stubs": ["Maths/Syracuse_données.py"], "command": "python3 Maths/Syracuse_données_Test.py"})

---

### A vous de jouer

Dans la fenêtre ci-dessous, il n'y a rien à valider, vous êtes libre d'afficher ce que vous voulez. Vous pouvez par exemple modifier votre programme précédent pour chercher les nombres N qui donnent le temps de vol le plus grand parmi les nombres plus petits qu'un million. Ou bien le nombre donnant l'altitude la plus haute. Ou même chercher les nombres qui volent en rase-motte c'est à dire qui volent loin sans pour autant aller haut. Et ensuite regarder le résultat dans la représentation graphique plus haut.

@[A vous de jouer]({"stubs": ["Maths/Syracuse_bac_a_sable.py"], "command": "python3 Maths/Syracuse_bac_a_sable.py"})
