# Incontournable factorielle (version recursive)

La factorielle d'un nombre ***n*** (noté $`n!`$) est définie par $`n!=1\times 2\times 3\times\dots\times n`$ et par convention $`0!=1`$. On a déjà crée un programme avec un boucle `for`pour calculer la factorielle d'un nombre. Cette fois-ci, nous allons créer la version recursive.

En remarquant que $`factorielle(n)=n \times factorielle(n-1)`$, créer une version recursive de la fonction factorielle.

> Entrée : Un entier naturel ***n***.

> Sortie : La fonction ***factorielle*** programmée de manière récursive qui revoie (avec `return`) $`n!`$.

@[Créer une fonction factorielle]({"stubs": ["Les_fonctions/factorielle.py"], "command": "python3 Les_fonctions/factorielle_Test.py"})

---

### Application : Calcul des coefficients binomiaux

En probabilité, lorsqu'on étudie la loi binomiale, apparaissent naturellement ce que l'on appelle les coefficients binomiaux. Ils apparaissent aussi dans d'autres parties des mathématiques. On pourra trouver plus d'information sur [Wikipédia](https://fr.wikipedia.org/wiki/Coefficient_binomial).

Nous allons nous intéresser ici à leur calcul en utilisant la formule faisant intervenir les factorielles : On a pour des entiers naturels ***n*** et ***k*** :
+ $`\left(\begin{array}{c} n\\k\end{array}\right)=\frac{n!}{k!}{(n-k)!}`$ si $`0\leq k\leq n`$
+ $`\left(\begin{array}{c} n\\k\end{array}\right)=0`$ si $`n< k`$

Tout d'abord, copiez-collez votre programme factorielle précédent dans la fenêtre ci-dessous. Créez ensuite un programme ***binom*** qui calcule le coefficient binomial $`\left(\begin{array}{c} n\\k\end{array}\right)`$.

> Entrée : Deux entiers naturels n et k dans cet ordre.

> Sortie : Une fonction ***binom*** qui renvoie (avec `return`) la valeur de $`\left(\begin{array}{c} n\\k\end{array}\right)`$ en utilisant les formules données.

@[Créer une fonction binom]({"stubs": ["Les_fonctions/fonction_binom.py"], "command": "python3 Les_fonctions/fonction_binom_Test.py"})
