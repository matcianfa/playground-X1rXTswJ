# Classe de Première - Second degré


## Exercice n° : Calcul du discriminant
`Difficulté : Très facile`  

Le but de cet exercice est de créer un programme qui donne le discriminant $`\Delta`$ d'un polynôme du second degré ***ax²+bx+c***.

>Entrée : Les coefficients ***a***, ***b*** et ***c*** du polynôme du second degré

>Sortie : Le discriminant $`\Delta`$

@[Calcul du discriminant]({"stubs": ["Variables_et_fonctions/Calcul_du_discriminant.py"], "command": "python3 Variables_et_fonctions/Calcul_du_discriminant_Test.py"})

---

## Exercice n° : Nombre de racines d'un polynôme du second degré
`Difficulté : Très Facile`

Écrire un programme qui prend en entrée les coefficients ***a***, ***b*** et ***c*** d'un polynôme du second degré et donne en sortie le nombre de racines réelles du polynôme.

> Entrée : les coefficients ***a***, ***b*** et ***c*** d'un polynôme du second degré.

> Sortie : Le nombre de solutions réelles (juste le nombre, en chiffre).

@[Nombre de racines]({"stubs": ["Les_conditions/Nb_racines_poly_second_degre.py"], "command": "python3 Les_conditions/Nb_racines_poly_second_degre_Test.py"})

---

## Exercice n° : Racines d'un polynôme du second degré
`Difficulté : Très Facile`

Écrire un programme qui prend en entrée les coefficients ***a***, ***b*** et ***c*** d'un polynôme du second degré et donne en sortie les racines réelles du polynôme.

> Entrée : les coefficients ***a***, ***b*** et ***c*** d'un polynôme du second degré.

> Sortie : Les solutions réelles de $`ax^2 + bx + c = 0`$: On renverra "Pas de solution", la solution ou les solutions (séparées par une virgule, la plus petite en premier) selon les cas.

> Exemple : `ma_fonction(1,0,2)` doit renvoyer `"Pas de solution"` car $`x^2+2=0`$ n'a pas de solution.  
`ma_fonction(1,0,-4)` doit renvoyer `(-2,2)` dans cet ordre car les solutions de $`x^2-4=0`$ sont -2 et 2.

@[Racines d'un polynôme du second degré]({"stubs": ["Premiere/Second_degre/Racines_poly_second_degre.py"], "command": "python3 Premiere/Second_degre/Racines_poly_second_degre_Test.py"})

---

## Exercice n° : Racines d'un polynôme du premier ou second degré
`Difficulté : Facile`
`Notion utilisée : Liste`

Écrire un programme qui prend en entrée une ***liste*** de coefficients d'un polynôme $`P`$  et qui renvoie les solutions de l'éqution $`P(x)=0`$

> Entrée : Une ***liste*** de coefficients d'un polynôme $`P`$ (le premier coefficient correspond au degré le plus haut et le dernier au coefficient constant c'est à dire $`P(0)`$).

> Sortie : Les solutions réelles de $`P(x)=0`$ : On renverra "Pas de solution", la solution ou les solutions (séparées par une virgule, la plus petite en premier) selon les cas. On ne traitera QUE les cas où le degré est 1 ou 2. Pour des degrés autres que  1 ou 2, on renverra "Je ne sais pas faire"

> Exemple : `ma_fonction([1,0,2])` doit renvoyer `"Pas de solution"` car $`x^2+2=0`$ n'a pas de solution.  
`ma_fonction([1,0,-4])` doit renvoyer `(-2,2)` dans cet ordre car les solutions de $`x^2-4=0`$ sont -2 et 2.  
`ma_fonction([2,1])` doit renvoyer `-0.5` car la solution de $`2x+1=0`$ est $`-\frac 1 2`$.  
`ma_fonction([1,2,3,4])` doit renvoyer `"Je ne sais pas faire"` car le degré de $`P(x)=x^3+2x^2+3x+4`$ est 3.

> Remarque : il n'y aura pas de pièges du style [0,2,1] qui n'est pas un polynôme de degré 2 mais 1. Cependant, pour les plus rapides, vous pouvez essayer de prévoir ce genre de pièges avec votre fonction.


@[Racines d'un polynôme du premier ou second degré]({"stubs": ["Premiere/Second_degre/Racines_poly_premier_et_second_degre.py"], "command": "python3 Premiere/Second_degre/Racines_poly_premier_et_second_degre_Test.py"})

---

## Exercice n° : Déterminer deux nombres connaissant leur somme $`s`$ et leur produit $`p`$.
`Programme officiel`  
`Difficulté : Facile`

Ecrire une fonction qui prend en entrée deux nombres $`s`$ et $`p`$ et qui renvoie en sortie les deux nombres (séparés par une virgule, le plus petit en premier) dont la somme vaut $`s`$ et leur produit $`p`$. On renverra "Pas de solution" dans le cas où c'est impossible et deux fois le même si c'est le cas.

@[Déterminer deux nombres connaissant leur somme et leur produit]({"stubs": ["Premiere/Second_degre/s_et_p.py"], "command": "python3 Premiere/Second_degre/s_et_p_Test.py"})

---

## Exercice n° : Racines d'un polynôme bicarré.
`Difficulté : Moyen`  
`Notion probablement utile : Liste`

Écrire un programme qui prend en entrée les coefficients ***a***, ***b*** et ***c*** du polynôme $`P(x)=ax^4 + bx^2 + c`$  et donne en sortie les racines réelles du polynôme.

> Entrée : les coefficients ***a***, ***b*** et ***c*** de $`P`$.

> Sortie : Les solutions réelles de $`ax^4 + bx^2 + c = 0`$ : On renverra "Pas de solution", la solution ou les solutions (dans une liste, rangée dans l'ordre croissant, sans doublon) selon les cas.

> Exemple : `ma_fonction(1,0,2)` doit renvoyer `"Pas de solution"` car $`x^4+2=0`$ n'a pas de solution.  
`ma_fonction(1,0,-1)` doit renvoyer `(-1,1)` dans cet ordre car les solutions de $`x^4-1=0`$ sont -1 et 1.  
`ma_fonction(1,-5,4)` doit renvoyer `(-2,-1,1,2)` dans cet ordre car les solutions de $`x^4 - 5x^2+4 =0`$ sont -2, -1,1 et 2 (car on peut remarquer que $`x^4 - 5x^2+4 = (x^2-4)(x^2-1)`$.

@[Racines d'un polynôme bicarré]({"stubs": ["Premiere/Second_degre/Racines_poly_bicarré.py"], "command": "python3 Premiere/Second_degre/Racines_poly_bicarré_Test.py"})

---

## Exercice n° : Recherche de seuil
`Difficulté : Facile`  

On étudie l'évolution d'une certaine bactérie. Son nombre évolue selon la fonction $`f(t)=3t^2+69t+150`$ où $`t`$ représente le temps en heure.  
Ecrire une fonction qui prend en entrée un nombre $`n`$ de bactérie et donne en sortie l'heure à partir de laquelle le nombre  de bactérie dépasse $`n`$. On affichera "Impossible" lorsque ce nombre ne sera jamais atteint après le moment initial (t=0).

@[Recherche de seuil]({"stubs": ["Premiere/Second_degre/Seuil.py"], "command": "python3 Premiere/Second_degre/Seuil_Test.py"})

---
## Exercice n° : Factorisation d'un polynôme du troisième degré admettant une racine connue.
`Programme officiel`  
`Difficulté : Difficile`

On considère un polynôme du troisième degré $`P(x)=ax^3+bx^2+cx+d`$ dont on connait une racine $`r`$. 
1. Montrer qu'on peut alors le factoriser sous la forme $`P(x)=a(x-r)(x^2+px+q)`$. En déduire les valeurs de $`p`$ et $`q`$ en fonction de $`a`$, $`b`$, $`c`$ et $`d`$.
2. Programmer ci-dessous une fonction qui prend en entrée les réels $`a`$, $`b`$, $`c`$ et $`d`$ ainsi que la valeur $`r`$  de la racine réelle connue et donne en sortie les autres solutions de $`P(x)=0`$.  
On renverra avec `return` "Pas de solution" s'il n'y en a pas, et dans le cas où il y en a deux, on donnera le couple avec la plus petite en premier séparé d'une virgule.

@[Factorisation d'un polynôme du troisième degré]({"stubs": ["Premiere/Second_degre/resoudre_troisieme_degre.py"], "command": "python3 Premiere/Second_degre/resoudre_troisieme_degre_Test.py"})

---

## Exercice n° : Factorisation de $`x^n-1`$ par $`x-1`$, de $`x^n-a^n`$ par $`x-a`$.
`Programme officiel`  
`Difficulté : Moyenne`

Le but de cet exercice est de montrer que $`x^n-a`$  peut s'ecrire $`(x-a)P_n(x)`$ où $`P_n(x) `$ est un polynôme en $`x`$ que l'on va déterminer. 

1. On va d'abord s'intéresser au cas où $`a=1`$.  
Déterminer les valeurs de $`P_1(x)`$, $`P_2(x)`$ et vérifier que  $`P_3(x)=x^2+x+1`$.
2. Déterminer la formule de $`P_n(x)`$ en fonction de $`x`$ et $`n`$.
3. On s'intéresse à présent au cas où $`a`$ est un réel quelconque.  
Déterminer les valeurs de $`P_1(x)`$, $`P_2(x)`$ et vérifier que  $`P_3(x)=x^2+ax+a^2`$.
4. Vérifier que pour $`n\geq 1`$, on a $`P_n(x)=x^{n-1}+ax^{n-2}+a^2x^{n-3}+...+a^{n-2}x+a^{n-1}`$.
5. Ecrire une fonction qui prend en entrée les valeurs de $`n`$ et $`a`$ et donne en sortie la liste des coefficients de $`P_n`$ en commençant par ceux de plus haut degré.  
Par exemple si $`n=3`$ et $`a=3`$, alors $`P_n(x)=x^2+3x+9`$, la fonction devra donc renvoyer la liste `[1,3,9]`.

@[Factorisation de x^n-a^n par x-a]({"stubs": ["Premiere/Second_degre/facto_xn_an.py"], "command": "python3 Premiere/Second_degre/facto_xn_an_Test.py"})

