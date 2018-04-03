# Mémoïzation : Approximation de ***e***

On appelle ***e*** la constante de Neper. Elle est incontournable en mathématiques comme on peut le voir en Terminale avec la fonction exponentielle ou les nombres complexes. On pourra en trouver une présentation sur [Wikipédia](https://fr.wikipedia.org/wiki/E_(nombre)).

Le but est ici de programmer l'approximation $`e\approx \dfrac 1{0!} + \dfrac 1{1!} +\dfrac 1{2!} +\dfrac 1{3!} +\cdots+\dfrac 1{n!} `$ pour n assez grand. Je rappelle que $`n!=1\times 2\times 3\times\cdots\times n`$ est la factorielle de n. Nous avons déjà programmé cette fonction [ici](https://tech.io/playgrounds/17176/recueil-dexercices-pour-apprendre-python-au-lycee/factorielle-dun-nombre).

Comme on peut le voir, on va devoir calculer souvent la factorielle d'un nombre. Pour ne pas avoir à calculer plusieurs fois la même, il faudra donc programmer une fonction ***factorielle*** avec une méthode de mémoïzation avec un cache en variable globale.

> Entrée : Un entier ***n***

> Sortie : L'approximation de ***e*** par la formule ci-dessus. Pour cela, on devra créer deux fonctions : une ***factorielle(n)*** qui calcule la factorielle de ***n*** et une ***mon_programme(n)*** qui calcule l'approximation de ***e*** et affiche le résultat avec `return`.

@[Approximation de e]({"stubs": ["Optimisation/Approx_e.py"], "command": "python3 Optimisation/Approx_e_Test.py"})
