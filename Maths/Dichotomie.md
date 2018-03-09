# Méthode de recherche par dichotomie
`Difficulté : Moyenne à difficile`

Lorsque l'on cherche une donnée que l'on ne connait pas, il y a toujours plusieurs stratégies pour s'en approcher. La méthode de recherche par dichotomie consiste à couper notre intervalle de recherche en 2 et regarder dans quel sous intervalle se trouve ce que l'on cherche. Ensuite, on recommence avec le sous intervalle, on le coupe en deux pour ne garder que l'intervalle ou se trouve ce que l'on cherche etc.

Nous allons illustrer cette méthode par deux exemples.

### Le juste prix

Le juste prix est un jeu où la personne doit trouver le plus rapidement possible le bon prix. A chaque proposition de prix qu'il fait, le présentateur lui dit si le bon prix est plus grand ou plus petit que la valeur qu'il a proposé.

Le but est de créer une fonction qui donnera un prix à chaque étape en fonction de ce qu'on lui donne en entrée.
Les entrées sont soit :
+ "Go" si c'est le premier tour.
+ "Plus grand" si le nombre à trouver est plus grand que celui que vous avez proposé avant.
+ "Plus petit" si le nombre à trouver est plus petit que celui que vous avez proposé avant.

Pour compliquer l'affaire, vous jouez contre un adversaire (qui joue après vous) et qui lui utilisera une recherche par dichotomie pour trouver le prix. Pour gagner il faut donc trouver le juste prix avant l'adversaire ! 

Pour simplifier, tous les prix seront choisis au hasard entre 1 et 2000 et sont entiers.

:::  Aide
Il va surement falloir utiliser des variables globales...
:::

Entrée : Les ***paroles*** du commentateurs : "Go" pour lancer la partie. Ensuite des enchainements de "Plus grand" ou "Plus petit" jusqu'à ce qu'il y ait un gagnant.

Sortie : Le prix que vous proposez. Ce doit être un entier et il doit être renvoyé avec `return`.

@[Le juste prix !]({"stubs": ["Maths/Juste_prix.py"], "command": "python3 Maths/Juste_prix_Test.py"})
