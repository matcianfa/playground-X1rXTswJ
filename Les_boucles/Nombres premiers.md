# Vérifier si un nombre est premier
`Difficulté : Moyenne`

Je rappelle qu'un nombre premier est un nombre qui a exactement 2 diviseurs qui sont 1 et lui même. Ainsi 2, 3 ,5 ,7, 11 sont des nombres premiers mais 4, 6, 9 n'en sont pas.

Le but de cet exercice est de créer un algorithme qui nous dit si un nombre est premier ou pas. Dans un deuxième temps, on tentera de l'améliorer un peu pour qu'il soit plus rapide.

### Première version

Etant donnée la définition, pour savoir si un nombre ***n*** est premier ou pas, on va tout simplement tester s'il est divisible par un des nombres compris entre 2 et ***n-1***. Dès qu'on trouve un diviseur, on affiche "PAS PREMIER" sinon on affiche "PREMIER".

::: Aide
+ Je rapelle que pour savoir si un nombre ***d*** divise ***n***, il suffit de regarder si ***n%d==0***
+ Dès qu'on a trouvé un diviseur, on peut s'arrêter. On pourra utiliser break si on utilise un boucle `for`
+ Il existe un syntaxe très pratique (pour ici par exemple) avec les boucles `for`:
```Python
for ...:
    #commandes à faire en boucle
else:
    #commandes executées uniquement si la boucle for ne s'est pas terminée par un break
```
Ce qui vient après le `else` ne sera exécuté que si la boucle se termine normalement (c'est à dire pas par un `break`)
:::

> Entrée : Un nombre ***n***

> Sortie : "PREMIER" ou "PAS PREMIER"

@[Nombre premier ?]({"stubs": ["Les_boucles/Nombre_premier1.py"], "command": "python3 Les_boucles/Nombre_premier1_Test.py"})

---

### Version un peu améliorée

La version précédente a quelques défauts facilement améliorables. 

Le premier est que le programme vérifie si le nombre est divisible par tous les nombres pairs or s'il n'est pas divisible par 2, ça ne sert à rien de vérifier pour les autres.

De plus, si ***n***=117 par exemple, c'est évident qu'il ne peut pas être divisible par 116, ni même 115 ou 114... car ces nombres sont trop grands. Par un petit raisonnement, on peut montrer qu'il ne sert à rien de chercher des diviseurs plus grands que $`\sqrt n`$

Recopiez votre programme précédent ci-dessous et améliorez le en vous aidant des deux remarques précédentes.
Avant de le modifier, lancer Run pour voir qu'il est trop lent pour passer les tests.

> Entrée : Un nombre ***n***

> Sortie : "PREMIER" ou "PAS PREMIER"

@[Nombre premier ?]({"stubs": ["Les_boucles/Nombre_premier2.py"], "command": "python3 Les_boucles/Nombre_premier2_Test.py"})




