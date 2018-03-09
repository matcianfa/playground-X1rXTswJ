# Statistiques

Le but de cette série d'exercices est de créer des programmes pour calculer la moyenne, l'étendue, le mode, l'écart-type et la médiane d'une série statistique. Pour les définitions, vous pouvez les trouver dans votre cours ou sur internet. 

### Calculs de moyenne

#### Cas d'une série de nombres

Dans cette partie, on vous donne en entrée une ***liste*** de nombres. Vous devez afficher (avec `print`) la moyenne des nombres de cette série.

> Entrée : Une ***liste*** de nombres.

> Sortie : La moyenne de la ***liste*** affichée avec `print`.

@[Calcul de moyenne]({"stubs": ["Maths/stat_moyenne1.py"], "command": "python3 Maths/stat_moyenne1_Test.py"})

---

#### Cas d'une série pondérée de nombres

Dans cette partie, on vous donne en entrée deux listes de nombres : 
+ ***liste_valeurs*** qui est la série statistique.
+ ***liste_pondérations*** qui donne la pondération des éléments de la série statistique c'est à dire le nombre de fois ou les valeurs apparaissent.

Exemple : si ***liste_valeurs***=[4,7,1] et ***liste_pondérations***=[3,5,2] cela signifie que le nombre 4 apparait 3 fois, le nombre 7 apparait 5 fois et le nombre 1 apparait 2 fois.

> Entrée : Deux listes de nombres ***liste_valeurs*** et ***liste_pondérations***.

> Sortie : La moyenne pondérée qui correspond à la série statistique donnée en entrée et affichée avec `print`.


@[Calcul de moyenne]({"stubs": ["Maths/stat_moyenne2.py"], "command": "python3 Maths/stat_moyenne2_Test.py"})

---

### L'étendue

On donne en entrée une série statistique sous forme de ***liste*** de nombre. Vous devez créer un programme qui affiche l'étendue de cette liste.

> Entrée : Une ***liste*** de nombres.

> Sortie : L'étendue de cette ***liste*** affichée avec `print`.


@[Calcul de l'étendue]({"stubs": ["Maths/stat_etendue.py"], "command": "python3 Maths/stat_etendue_Test.py"})

---

### Le mode

