# Calculs des termes d'une suite récurrente (Version récursive)

### Suite définie par une formule de récurrence simple

Considérons la suite définie par $`u_{n+1}=2 u_n +3`$ et $`u_0=2`$.

Créez une fonction ***u*** qui donne la valeur de $`u_n`$ pour un ***n*** donné. On programmera de manière récursive cette fonction.

> Entrée : Un entier ***n***

> Sortie : Une fonction récursive ***u*** qui renvoie (avec `return`) la valeur de $`u_n`$.

@[Calcul des termes de la suite u]({"stubs": ["Les_fonctions/Suite_recurrente_simple.py"], "command": "python3 Les_fonctions/Suite_recurrente_simple_Test.py"})

---

### Suite définie par une récurrence double

Intéressons nous à présent à la suite définie par $`u_{n+1}=2 u_n +3 u_{n-1}`$ avec  $`u_0=2`$ et $`u_1=1`$.

Créez une fonction ***u*** qui donne la valeur de $`u_n`$ pour un ***n*** donné. On programmera de manière récursive cette fonction.

> Entrée : Un entier ***n***

> Sortie : Une fonction récursive ***u*** qui renvoie (avec `return`) la valeur de $`u_n`$.

@[Calcul des termes de la suite u]({"stubs": ["Les_fonctions/Suite_recurrente_double.py"], "command": "python3 Les_fonctions/Suite_recurrente_double_Test.py"})

---

### Calcul de la racine carrée par la formule de Héron

Pour calculer une approximation de la racine carrée d'un nombre ***x***, une façon de faire est de calculer les termes de la suite définie par $`u_{n+1}=\frac 1 2 \left(u_n+\frac x{u_n}\right)`$ et $`u_0=1`$. On appelle cette technique la méthode de Héron d'Alexandrie.

Cette suite se rapproche très rapidement de la valeur de $`\sqrt{x}`$ c'est pourquoi on va se contenter de calculer $`u_5`$ pour la comparer à la vraie valeur de $`\sqrt{x}`$.

Le but de cet exercice est de créer une fonction ***racine*** qui prend en entrée ***x*** et affiche la valeur de $`u_5`$ qui correspond à une valeur approchée de $`\sqrt{x}`$ par la méthode de Héron. 

::: Aide
On peut créer une fonction dans une autre fonction. Par exemple ici, une façon de faire est de créer un fonction ***racine(x)*** et à l'intérieur de cette fonction, une fonction ***u(n)*** qui calcule de manière récursive les valeurs de ***u***.
:::

> Entrée : Un nombre ***x***.

> Sortie : Une fonction ***racine*** qui donne une approximation de $`\sqrt{x}`$ en renvoyant (avec `return`) la valeur de $`u_5`$ par la méthode de Héron.

@[Calcul approché de racine(x)]({"stubs": ["Les_fonctions/Formule_de_Heron.py"], "command": "python3 Les_fonctions/Suite_recurrente_simple_Test.py"})
