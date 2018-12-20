# Exercices ne demandant aucune connaissance du lycée en mathématique.

Voici des exercices sur le chapitre Variables et fonctions mathématiques qui peuvent se résoudre avec des connaissances de collège au plus.

# Prix total
`Difficulté : Très facile`

Léa va régulièrement acheter toujours les mêmes bonbons : des fraises à 0.04 euros l'unité et des réglisses à 0.07 euros l'unité.  
Créer un programme qui donne le prix total payé par Léa en fonction du nombre ***a*** de fraises et ***b*** de réglisses achetés.

> Entrée : Le nombre ***a*** de fraises et ***b*** de réglisses achetés.

> Sorties : le prix payé par Léa.

@[Ticket de caisse]({"stubs": ["Variables_et_fonctions/Bonbons.py"], "command": "python3 Variables_et_fonctions/Bonbons_Test.py"})

---

# Paires de chaussettes
`Difficulté : Très Facile`  
`Origine :` [`Hackerrank`](https://www.hackerrank.com/challenges/maximum-draws/problem)

Baptiste cherche des chaussettes pour aller à une soirée. Son tiroir est plein de chaussettes, chaque paire est de couleur différente. Pour choisir une chaussette, il met sa main dans le tiroir et ne voit la couleur de la chaussette qu'une fois qu'il l'a sortie du tiroir.

Dans le pire des cas, combien doit-il prendre de chaussettes dans son tiroir pour être sûr d'avoir une paire de la même couleur ?

> Entrée : Le nombre ***n*** de chaussettes dans le tiroir.

> Sortir : Le nombre de chaussettes que Baptiste doit sortir dans le pire des cas du tiroir être sûr d'avoir une paire de la même couleur.

@[Chacun cherche ses chaussettes sèches]({"stubs": ["Variables_et_fonctions/Chaussettes.py"], "command": "python3 Variables_et_fonctions/Chaussettes_Test.py"})

---

# Nombre de bises au nouvel an
`Difficulté informatique : Très facile`  
`Difficulté mathématique : Facile`

Des amis passent le soir du reveillon du nouvel an ensemble. A minuit, chacun embrasse (en faisant deux bises) tous les autres invités.

Combien y a-t-il eu de bises échangées pas les invités pour ce nouvel an ?

> Entrée : Le nombre ***n*** d'invités.

> Sortie : Le nombre de bises échangées pour ce nouvel an.

::: Indications :
On pourra considérer le nombre de bises que doit faire chaque personne puis remarquer qu'en comptant ainsi, on a compté plusieurs fois les mêmes bises.
:::

@[Nombre de bises]({"stubs": ["Variables_et_fonctions/Bises.py"], "command": "python3 Variables_et_fonctions/Bises_Test.py"})

---

# Bases armées
`Difficulté informatique : Très facile`  
`Difficulté mathématique : Moyenne`  
`Notion : Division euclidienne`  
`Origine :` [`Hackerrank`](https://www.hackerrank.com/challenges/game-with-cells/problem)

Luke est dans ses pensées pendant un cours de maths. Sur un papier quadrillé de ***n*** lignes et ***m*** colonnes, il imagine que chaque case est une base armée. Il veut envoyer des fournitures à ses bases à des points stratégiques, en marquant chaque point en rouge. Si une base contient au moins un colis de fourniture dedans ou sur un de ses bords, on qu'onsidère qu'il y a accès. Par exemple : 
![Fournitures](https://s3.amazonaws.com/hr-challenge-images/0/1479944215-79f12638a7-example-army-game.png)

Etant donnés ***n*** et ***m***, érire une fonction qui renvoit le nombre minimum de colis que Luke doit envoyer pour fournir toutes ses bases.

@[Bases armées]({"stubs": ["Variables_et_fonctions/Bases_armees.py"], "command": "python3 Variables_et_fonctions/Bases_armees_Test.py"})

---

# Découpe de morceaux de papier
`Difficulté informatique: Très facile`  
`Difficulté mathématique : Moyenne`  
`Origine : ` [`Hackerrank`](https://www.hackerrank.com/challenges/p1-paper-cutting/problem)

Marie veut découper un morceau de papier de dimmension $`n\times m`$ en morceau de papier de dimension $`1\times 1`$ selon les règles suivantes :

+ Elle ne peut couper qu'un morceau de papier à la fois, c'est à dire qu'elle ne peut pas placer des papiers déjà découpés les uns sur les autres ou d'affilée. Elle ne peut pas non plus les plier avant de les découper.

+ Elle découpe en ligne droite horizonthalement ou bien verticalement uniquement.

Voici un exemple montrant les trois seules découpes possibles dans ce cas :
![Découpes](https://s3.amazonaws.com/hr-challenge-images/26273/1476740077-bd1ab26d74-example-cutting-squares.png)

Etant donnés n et m, trouver et renvoyer (avec `return`) le nombre minimum de découpe que Marie peut faire pour découper le papier en carré unité.

> Entrée : Les dimensions entières ***n*** et ***m*** du morceau de papier au départ.

> Sortie : Le nombre minimum de découpe nécessaire pour n'obtenir plus que des petits carrés de dimensions $`1\times 1`$

:::  Indication :
On pourra remarquer que chaque coup de ciseau rajoute un au nombre de morceaux de papier qu'on a ...
:::

@[Découpe de morceaux de papier]({"stubs": ["Variables_et_fonctions/Decoupe_papier.py"], "command": "python3 Variables_et_fonctions/Decoupe_papier_Test.py"})

---

