# Exercices ne demandant aucune connaissance du lycée en mathématique.

Voici des exercices sur le chapitre Variables et fonctions mathématiques qui peuvent se résoudre avec des connaissances de collège au plus.

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
`Difficulté : Facile`

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
`Difficulté : Facile à moyenne`  
`Notion : Division euclidienne`  
`Origine :` [`Hackerrank`](https://www.hackerrank.com/challenges/game-with-cells/problem)

Luke est dans ses pensées pendant un cours de maths. Sur un papier quadrillé de ***n*** lignes et ***m*** colonnes, il imagine que chaque case est une base armée. Il veut envoyer des fournitures à ses bases à des points stratégiques, en marquant chaque point en rouge. Si une base contient au moins un colis de fourniture dedans ou sur un de ses bords, on qu'onsidère qu'il y a accès. Par exemple : 
![Fournitures](https://s3.amazonaws.com/hr-challenge-images/0/1479944215-79f12638a7-example-army-game.png)

Etant donnés ***n*** et ***m***, quel est le nombre minimum de colis que Luke doit envoyer pour fournir toutes ses bases ?

@[Bases armées]({"stubs": ["Variables_et_fonctions/Bases_armees.py"], "command": "python3 Variables_et_fonctions/Bases_armees_Test.py"})
