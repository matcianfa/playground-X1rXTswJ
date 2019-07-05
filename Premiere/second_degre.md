# Classe de Première - Second degré

## Exercice n° : Factorisation d'un polynôme du troisième degré admettant une racine connue.
`Programme officiel`  
`Difficulté : Difficile`

On considère un polynôme du troisième degré $`P(x)=ax^3+bx^2+cx+d`$ dont on connait une racine $`r`$. 
1. Montrer qu'on peut alors le factoriser sous la forme $`P(x)=a(x-r)(x^2+px+q)`$. En déduire les valeurs de $`p`$ et $`q`$ en fonction de $`a`$, $`b`$, $`c`$ et $`d`$.
2. Programmer ci-dessous une fonction qui prend en entrée les réels $`a`$, $`b`$, $`c`$ et $`d`$ ainsi que la valeur $`r`$  de la racine réelle connue et donne en sortie les autres solutions de $`P(x)=0`$.  
On renverra avec `return` "Pas de solution" s'il n'y en a pas, et dans le cas où il y en a deux, on donnera le couple avec la plus petite en premier séparé d'une virgule.

@[Factorisation d'un polynôme du troisième degré]({"stubs": ["Premiere/Second_degre/resoudre_troisieme_degre.py"], "command": "python3 Premiere/Second_degre/resoudre_troisieme_degre_Test.py"})

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

@[Factorisation de $`x^n-a^n`$ par $`x-a`$]({"stubs": ["Premiere/Second_degre/facto_xn-an.py"], "command": "python3 Premiere/Second_degre/facto_xn-an_Test.py"})

