# Algorithme d'Euclide

L'algorithme d'Euclide est permet de trouver le PGCD de deux nombres ***a*** et ***b***. Il est basé sur la propriété suivante : 
> Si on note ***q*** et ***r*** le quotient et le reste de la division euclidienne de ***a*** par ***b***, c'est à dire les nombres entiers tels que ***a=b*q+r*** avec 0 <= r < b, alors on a PGCD(a,b)=PGCD(b,r).
En remarquant que pour tout nombre n, on a PGCD(n,0)=n, il suffit de réitérer des divisions successives jusqu'à arriver à 0 pour obtenir le pgcd.

### Première version

Cette première version consiste à réitérer ces divisions euclidiennes tant que le reste est non nul. Plus précisément:
1. On nomme ***a*** et ***b*** les nombres donnés avec ***a*** le plus grand des deux.
2. On calcule le reste ***r*** de la division euclidienne (en utilisant `%`) de ***a*** par ***b***.
3. On réitère l'étape 2. avec ***a***=***b*** et ***b***=***r*** tant que ***r*** est non nul.
4. On renvoye le dernier reste non nul qui sera le PGCD de ***a*** et ***b***.

Créer un programme qui calcule le PGCD de ***a*** et ***b*** donnés en entrée par cette méthode.

> Entrée : ***a*** et ***b*** deux entiers.

> Sortie : Le PGCD de ***a*** et ***b*** renvoyé avec `return`.

@[Algorithme d'Euclide]({"stubs": ["Maths/Euclide.py"], "command": "python3 Maths/Euclide_Test.py"})

---

### Version récursive

Créer une version récursive (on appellera la fonction ***pgcd***) pour calculer le PGCD en utilisant la propriété du début.

> Entrée : ***a*** et ***b*** deux entiers.

> Sortie : Le PGCD de ***a*** et ***b*** renvoyé avec `return`.

@[Algorithme d'Euclide]({"stubs": ["Maths/Euclide_recursif.py"], "command": "python3 Maths/Euclide_recursif_Test.py"})
