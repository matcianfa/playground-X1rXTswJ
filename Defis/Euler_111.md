# Nombres premiers avec répétitions de chiffres
`Difficulté : Moyen (45%)`
`Origine : Projet Euler n°111`

En considérant les nombres premiers de quatre chiffres qui se répètent, il est clair qu'ils ne peuvent pas être tous identiques : 1111 est divisible par 11, 2222 par 22 ... Cependant, il y a neuf nombres de quatre chiffres qui contiennent trois 1 :

1117, 1151, 1171, 1181, 1511, 1811, 2111, 4111, 8111

On notera M(n,d) le nombre maximum de chiffres d répétés dans un nombre premier de n chiffres, N(n,d) le nombre de tels nombres premiers et S(n,d) la somme de tous ces nombres premiers.

Par exemple, M(4,1)=3 est le nombre maximum de répétition de 3 dans un nombre premier de quatre chiffres, il y a N(4,1)=9 nombres premiers ainsi et la somme de ces nombres est S(4,1)=22274. Pour d=0, on a seulement M(4,0)=2 répétitions possible mais N(4,0)=13 dans ce cas.

De la même façon, on peut obtenir les résultats suivants pour les nombres premiers de 4 chiffres : 

| Chiffre : d | M(4,d) | N(4,d) | S(4,d) |
|:-----------:|:------:|:------:|:------:|
| 0 | 2 | 13 | 67061 |
| 1 | 3 | 9 | 22275 |
| 2 | 3 | 1 | 2221 |
| 3 | 3 | 12 | 46214 |
| 4 | 3 | 2 | 8888 |
| 5 | 3 | 1 | 5557 |
| 6 | 3 | 1 | 6661 |
| 7 | 3 | 9 | 57863 |
| 8 | 3 | 1 | 8887 |
| 9 | 3 | 7 | 48073 |

Pour d = 0 à 9, la somme de tous les S(4,d) est 273700.

Trouver la somme de tous les S(10,d).

On affichera le résultat avec `print`.

@[Nombres premiers avec répétitions de chiffres]({"stubs": ["Defis/Euler_111.py"], "command": "python3 Defis/Euler_111_Test.py"})

---

# Nombres oscillants
`Difficulté : Moyen (15%)`
`Origine : Projet Euler n°112`

En travaillant de gauche à droite, si aucun chiffre d'un nombre n'est excédé par le chiffre sur sa gauche, on dira que le nombre est croissant. Par exemple 134468.

De même, si aucun chiffre n'est excédé par le chiffre sur sa droite, on dira le nombre décroissant comme par exemple 66420.

On dira qu'un entier est "oscillant" s'il n'est ni croissant ni décroissant comme par exemple 155349.

Il n'y a clairement pas de nombres oscillants en dessous de 100 mais juste un peu plus de la moitié (525) des nombres inférieurs à 1000 sont oscillants. En fait, le plus petit nombre pour lequel la proportion de nombres oscillants dépasse 50% est 538.

De façon assez surprenante, les nombres oscillants deviennent de plus en plus fréquents et à partir de 21780, la proportion de nombres oscillants est de 90%.

Trouver le plus petit nombre pour lequel la proportion de nombres oscillants est exactement 99%.

On affichera le résultat avec `print`.

@[Nombres oscillants]({"stubs": ["Defis/Euler_112.py"], "command": "python3 Defis/Euler_112_Test.py"})

---

# Nombres non oscillants
`Difficulté : Moyen (30%)`
`Origine : Projet Euler n°113`

En travaillant de gauche à droite, si aucun chiffre d'un nombre n'est excédé par le chiffre sur sa gauche, on dira que le nombre est croissant. Par exemple 134468.

De même, si aucun chiffre n'est excédé par le chiffre sur sa droite, on dira le nombre décroissant comme par exemple 66420.

On dira qu'un entier est "oscillant" s'il n'est ni croissant ni décroissant comme par exemple 155349.

Quand n augmente, la proportion de nombres oscillants inférieurs à n croit tellement qu'il n'y a que 12951 nombres inférieurs à un million qui ne sont pas oscillants et seulement 277032 nombres non oscillants inférieurs à $`10^{10}`$.

Combien de nombres inférieurs à un googol ($`10^{100}`$) sont non oscillants ?

On affichera le résultat avec `print`.

@[Nombres non oscillants]({"stubs": ["Defis/Euler_113.py"], "command": "python3 Defis/Euler_113_Test.py"})

---

# Compter les combinaisons de blocs I
`Difficulté : Moyen (35%)`
`Origine : Projet Euler n°114`

On considère une ligne mesurant 7 unités de long sur laquelle on place des bandes rouges de longueur minimale 3 telles que ces bandes sont séparées par au moins un bloc noir. Il y a exactement 17 façons de le faire : 

![bandes colorées](Euler114.png)

De combien de façons peut-on recouvrir une bande de 50 unités de long ?

Note : Bien que sur l'exemple donné cette possibilité est impossible, en général, les blocs rouges peuvent être de longueurs différentes : Par exemple si la longueur est 8, on peut avoir un recouvrement de la forme rouge(3) noir(1) et rouge(4).

On affichera le résultat avec `print`.

@[Compter les combinaisons de blocs I]({"stubs": ["Defis/Euler_114.py"], "command": "python3 Defis/Euler_114_Test.py"})

---

# Compter les combinaisons de blocs II
`Difficulté : Moyen (35%)`
`Origine : Projet Euler n°115`

Note : Ce problème est une version un peu plus difficile du problème précédent.

Une bande mesurant n unité de longueur est recouverte par des bandes rouges de longueur minimale m telles que deux blocs rouges sont séparées par au moins une case noire.

On pose F(m,n) le nombre de façon de recouvrir une bande de longueur n par des bandes rouges de longueur au moins m.

On a par exemple F(3, 29) = 673135 et F(3, 30) = 1089155.

On peut voir que pour m=3, n=30 est la plus petite valeur telle que F(3,.) dépasse un million.

De la même façon, pour m=10, on peut vérifier que F(10, 56) = 880711 et F(10, 57) = 1148904, donc n=57 est la plus petite valeur telle que la fonction F(10,.) dépasse un million.

Pour m = 50, quelle est la plus petite valeur de n pour laquelle F(50,.) dépasse un million ?

On affichera le résultat avec `print`.

@[Compter les combinaisons de blocs II]({"stubs": ["Defis/Euler_115.py"], "command": "python3 Defis/Euler_115_Test.py"})

---
