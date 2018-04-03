# Mémoïzation : Système proies-prédateurs

On a déjà vu ce système dans un exercice précédent que vous pouvez relire [ici](https://tech.io/playgrounds/17176/recueil-dexercices-pour-apprendre-python-au-lycee/systeme-proie-predateur).

Reprenons ici la partie mathématique seulement. On a un système de deux suites définies par $`u_0=53000`$, $`v_0=9000`$ et :
```math
\left\{\begin{array}{l}u_{n+1}=(1+a-bv_n).u_n \\ v_{n+1}=(1-c+du_n).v_n\end{array}\right.
```
Nous allons prendre pour valeur a=0.09, b=0.00001, c=0.25 et d=0.000005.

Créez deux fonctions ***u*** et ***v*** qui prennent en entrée ***n*** et renvoie respectivement les valeurs de $`u_n`$ et $`v_n`$. Les valeurs qui seront vérifiées seront élevées. Il faudra donc utiliser une méthode de mémoïzation.

> Entrée : Un entier ***n*** .

> Sortie : Deux fonctions ***u*** et ***v*** qui renvoie (avec `return`) respectivement les valeurs de $`u_n`$ et $`v_n`$.

@[Système de Lotka-Volterra]({"stubs": ["Optimisation/Volterra.py"], "command": "python3 Optimisation/Volterra_Test.py"})
