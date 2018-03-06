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
