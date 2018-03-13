# Calcul approché d'aires par la méthode des trapèzes.
`Difficulté : Moyenne`

### Présentation

Le but de cette fiche est de présenter la méthode des trapèzes pour calculer l'aire sous une courbe représentative d'une fonction. Cette méthode est très proche de la méthode des rectangles mais donne de meilleurs approximations. Pour simplifier la présentation, on supposera ici que nos fonctions sont toutes positives sur l'intervalle sur lequel on les considère.

Définissons d'abord ce qu'est l'aire sous la courbe représentative d'une fonction sur un intervalle [a,b] : C'est tout simplement l'aire comprise entre la courbe représentative, l'axe des abscisses et les droites x=a et x=b.

![Illustration](https://upload.wikimedia.org/wikipedia/commons/thumb/c/c9/Aire_sous_la_courbe.svg/220px-Aire_sous_la_courbe.svg.png)

Présentons à présent la méthode des trapèzes pour calculer l'aire sous la courbe représentative d'une fonction ***f*** sur un intervalle [a,b].  
L'idée est d'approcher l'aire sous la courbe par des trapèzes dont l'aire est facilement calculables comme sur la figure ci-dessous (les bases des trapèzes sont verticales).
![Illustration](https://blogdemaths.files.wordpress.com/2015/07/methode_des_trapezes_redecouvrons_la_formule.png?w=300)
Pour cela, on procède comme suit :
1. On commence par choisir le nombre ***n*** de trapèzes qu'on veut sous la courbe . Plus le nombre sera grand, plus la surface formée par les trapèzes sera proche de l'aire sous la courbe.
1. On répartit sur [a,b] ***n+1*** points de la façon équitable suivante : $`x_0=a`$ et $`x_{n+1}=x_n+\frac{b-a} n`$.
1. On construit le premier trapèze de largeur $`\frac{b-a} n`$ entre $`x_0`$ et $`x_1`$ sur l'axe des abscisses et dont les bases mesurent $`f(x_0)`$ et $`f(x_1)`$. Son aire est donc de $`\dfrac{(base1+base2)\times hauteur}2=\frac{\left(f(x_0)+f(x_1)\right)\times\frac{b-a}n}{2}`$
1. On contruit le deuxième trapèze juste à coté de même largeur $`\frac{b-a} n`$ mais qui  cette fois ci est entre $`x_1`$ et $`x_2`$ sur l'axe des abscisses et dont les bases mesurent $`f(x_1)`$ et $`f(x_2)`$. Son aire est donc de $`\dfrac{(base1+base2)\times hauteur}2=  \frac{\left(f(x_1)+f(x_2)\right)\times\frac{b-a}n}{2}`$. 
1. On continue ainsi jusqu'à arriver au dernier trapèze qui finira en b donc commencera à $`x_{n-1}`$. Son aire sera $`\frac{\left(f(x_{n-1})+f(x_n)\right)\times\frac{b-a}n}{2}`$

Finalement, l'aire de tous ces trapèzes ainsi construits sera : $`\frac{b-a}n \left(a+\frac{f(x_1)+\dots+f(x_{n-1})}2+b\right)`$.

Dans la fenêtre ci-dessous, vous avez juste à appuyer sur Run pour voir une illustration. Vous pouvez modifier les paramètres pour voir les conséquences.

@[Illustration de la méthode des trapèzes]({"stubs": ["Maths/Methode_trapèzes_illustration.py"], "command": "python3 Maths/Methode_trapèzes_illustration_Test.py"})

---

### A vous de jouer

Créez un programme qui prend en entrée ***f***, ***a***, ***b*** et ***n*** et affiche (avec `return`) l'aire calculée par la méthode des rapèzes.

> Entrée : Une fonction ***f***, les bornes de l'intervalle ***a*** et ***b*** et le nombre de subdivisions ***n***.

> Sortie : L'aire calculée avec la méthode des trapèzes et affichée avec `return`.

@[Méthode des trapèzes]({"stubs": ["Maths/Methode_trapèzes.py"], "command": "python3 Maths/Methode_trapèzes_Test.py"})
