# Vérifier si un nombre est premier
`Difficulté : Moyenne`

Je rappelle qu'un nombre premier est un nombre qui a exactement 2 diviseurs qui sont 1 et lui même. Ainsi 2, 3 ,5 ,7, 11 sont des nombres premiers mais 4, 6, 9 n'en sont pas.

Le but de cet exercice est de créer un algorithme qui nous dit si un nombre est premier ou pas. Dans un deuxième temps, on tentera de l'améliorer un peu pour qu'il soit plus rapide.

### Première version

Etant donnée la définition, pour savoir si un nombre ***n*** est premier ou pas, on va tout simplement tester s'il est divisible par un des nombres compris entre 2 et ***n-1***. Dès qu'on trouve un diviseur, on affiche "PAS PREMIER" sinon on affiche "PREMIER".

::: Aide
+ Je rapelle que pour savoir si un nombre ***d*** divise ***n***, il suffit de regarder si ***n%d==0***
+ Dès qu'on a trouvé un diviseur, on peut s'arrêter. On pourra utiliser break si on utilise un boucle `for`
:::

> Entrée : Un nombre ***n***

> Sortie : "PREMIER" ou "PAS PREMIER"

@[Nombre premier ?]({"stubs": ["Les_boucles/Nombre premier1.py"], "command": "python3 Les_boucles/Nombre premier1_Test.py"})



