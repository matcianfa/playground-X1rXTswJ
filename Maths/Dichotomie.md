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

---

### Recherche des zéros d'une fonction

Considérons une fonction f continue sur un intervalle [a,b] (Si vous n'avez pas vu la continuité en cours, on va simplifier en disant que cela signifie que sa courbe représentative se trace sans lever le stylo). On suppose que f(a) et f(b) sont de signes opposés. Alors forcément, entre a et b, on peut trouver un réel x tel que f(x)=0. Le but de cette partie est de trouver une valeur approchée de ce x à 0,000001 près.

Pour cela, on va utiliser une méthode de recherche par dichotomie. Le principe est simple : 
+ On calcule $`f\left(\frac{a+b}2\right)`$ c'est à dire la valeur de f au milieu de l'intervalle [a,b].
+ Si cette valeur est du même signe que f(a) c'est que x est dans l'intervalle $`\left[\frac{a+b}2, b\right]`$.
+ Sinon c'est que x est dans l'intervalle $`\left[a,\frac{a+b}2\right]`$
+ On recommence notre rechercher par dichotomie sur l'intervalle plus petit où se trouve x tant qu'on est pas sûr que la précision est atteinte c'est à dire tant que l'intervalle qu'on considère est plus grand que 0,000001.

Créez un programme qui prend en entrée une fonction ***f***, et les bornes ***a*** et ***b*** de l'intervalle et affiche une valeur approchée de x à 0,000001 près.

> Entrée : Une fonction ***f*** et deux réels ***a*** et ***b***.

> Sortie : Une valeur à 0,000001 près d'une solution à l'équation ***f(x)=0*** renvoyée avec return.

@[Recherche de zéros]({"stubs": ["Maths/zero_dicho.py"], "command": "python3 Maths/zero_dicho_Test.py"})
