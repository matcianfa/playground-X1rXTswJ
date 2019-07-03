# Classe de Première - Second degré

## Exercice n° : Factorisation d'un polynôme du troisième degré admettant une racine connue.
`Programme officiel`  
`Difficulté : Difficile`

On considère un polynôme du troisième degré $`P(x)=ax^3+bx^2+cx+d`$ dont on connait une racine $`r`$. 
1. Montrer qu'on peut alors le factoriser sous la forme $`P(x)=a(x-r)(x^2+px+q)`$. En déduire les valeurs de $`p`$ et $`q`$ en fonction de $`a`$, $`b`$, $`c`$ et $`d`$.
2. Programmer ci-dessous une fonction qui prend en entrée les réels $`a`$, $`b`$, $`c`$ et $`d`$ ainsi que la valeur $`r`$  de la racine réelle connue et donne en sortie les autres solutions de $`P(x)=0`$.  
On renverra avec `return` "Pas de solution" s'il n'y en a pas, et dans le cas où il y en a deux, on donnera le couple avec la plus petite en premier séparé d'une virgule.

@[Factorisation d'un polynôme du troisième degré]({"stubs": ["Premiere/Second_degre/resoudre_troisieme_degre.py"], "command": "python3 Premiere/Second_degre/resoudre_troisieme_degre_Test.py"})
