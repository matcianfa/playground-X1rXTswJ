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
+ $`\left(\begin{array}{c} n\\k\end{array}\right)=\frac{n!}{k!(n-k)!}`$ si $`0\leq k\leq n`$
+ $`\left(\begin{array}{c} n\\k\end{array}\right)=0`$ si $`n< k`$

Tout d'abord, copiez-collez votre programme factorielle précédent dans la fenêtre ci-dessous. Créez ensuite un programme ***binom*** qui calcule le coefficient binomial $`\left(\begin{array}{c} n\\k\end{array}\right)`$.

> Entrée : Deux entiers naturels n et k dans cet ordre.

> Sortie : Une fonction ***binom*** qui renvoie (avec `return`) la valeur de $`\left(\begin{array}{c} n\\k\end{array}\right)`$ en utilisant les formules données.

@[Créer une fonction binom]({"stubs": ["Les_fonctions/fonction_binom.py"], "command": "python3 Les_fonctions/fonction_binom_Test.py"})

---

### Application : Approximation de ***e***

En terminale, on étudie la fonction exponentielle. Elle est très liée à un nombre particulier appelée constante de Néper et notée ***e***. On pourra trouver plus d'information sur [Wikipédia](https://fr.wikipedia.org/wiki/E_(nombre)).

Une des façons de calculer ***e*** consiste à utiliser la formule pour ***n*** assez grand :
```math
e\approx 1 +\frac 1{1!} +\frac 1{2!}+ \frac 1{3!} +\dots+\frac 1{n!}
```

Créez un programme ***approx_e*** qui prend en entrée un entier ***n*** et affiche l'approximation de ***e*** calculée avec la formule précédente. Pour vous entrainer, essayez de faire une version recursive de ***approx_e*** (c'est facile puisque c'est un calcul de somme).

N'oubliez pas de copier-coller votre fonction factorielle.

> Entrée : Un entier ***n***.

> Sortie : Une fonction ***approx_e*** qui renvoie (avec `return`) l'approximation de ***e*** calculée avec la formule précédente.

@[Créer une fonction approx_e]({"stubs": ["Les_fonctions/fonction_approx_e.py"], "command": "python3 Les_fonctions/fonction_approx_e_Test.py"})

---

### Application : Approximation de $`\pi`$

Tant qu'on y est, approximons $`\pi`$ ! On peut trouver énormément de formules pour approximer $`\pi`$. On a déjà vu une façon de faire dans les premiers exercices en calculant le périmètre d'un polygone régulier. On peut aller voir [Wikipédia](https://fr.wikipedia.org/wiki/Approximation_de_%CF%80) pour une belle liste de formules permettant d'approximer $`\pi`$ .

Vue la précision de python, nous n'avons pas besoin de formule réellement efficace (on ne vise pas le milliard de décimales), nous allons donc utiliser un formule pas trop compliquée :
```math
\pi\approx \left( 2 +\frac {2^2\times (1!)^2}{3!} +\frac {2^3\times (2!)^2}{5!}+ \frac {2^4\times (3!)^2}{7!} +\dots+\frac {2^{n+1}\times (n!)^2}{(2n+1)!}\right)
```

Créez un programme ***approx_pi*** qui prend en entrée un entier ***n*** et affiche l'approximation de $`\pi`$ calculée avec la formule précédente. Pour vous entrainer, essayez de faire une version recursive de ***approx_pi*** (c'est facile puisque c'est un calcul de somme).

N'oubliez pas de copier-coller votre fonction factorielle.

> Entrée : Un entier ***n***.

> Sortie : Une fonction ***approx_pi*** qui renvoie (avec `return`) l'approximation de $`\pi`$ calculée avec la formule précédente.

@[Créer une fonction approx_pi]({"stubs": ["Les_fonctions/fonction_approx_pi.py"], "command": "python3 Les_fonctions/fonction_approx_pi_Test.py"})

