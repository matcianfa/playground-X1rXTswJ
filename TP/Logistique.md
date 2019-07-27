# La suite logistique
`Difficulté : de Facile à Difficile`  
`Prérequis : Les listes`

La suite est très intéressante à étudier car c'est un des exemples les plus simples qui permettent d'observer ce que l'on appelle le chaos. C'est l'équivalent en physique du double pendule : un phénomène simple et pourtant imprévisible. On pourra lire [Wikipédia](https://fr.wikipedia.org/wiki/Th%C3%A9orie_du_chaos) pour plus d'information sur la théorie du Chaos.

Le but de cette page est donc de présenter la suite logistique et toucher du doigt son coté chaotique.

## Définition de la suite
`Difficulté : Facile`

On appelle suite logistique la suite définie pour un réel $`\mu>0`$ par $`u_{n+1}=\mu u_n(1-u_n)`$.

Créer une fonction `u(mu,u0,n)` qui prend en entrée le paramètre $`\mu`$ (mu), le premier terme $`u_0`$ et un entier ***n*** et renvoie en sortie la ***liste*** des termes de la suite de $`u_0`$ jusqu'à $`u_n`$.

@[Définition des suites]({"stubs": ["TP/logistique.py"], "command": "python3 TP/logistique_Test.py"})

---

## Représentation graphique I
`Difficulté : Facile`

Une première façon de représenter notre suite est de manière classique c'est à dire n selon les abscisses et $`u_n`$ selon les ordonnées.

Créer une fonction `dessiner(mu,u0,n)` qui affiche avec matplotlib les points associés à la suite allant de $`u_0`$ jusqu'à $`u_n`$. On pourra utiliser la fonction `plt.plot(X,Y,".-",linewidth=1)` pour afficher les points et les relier. Le résultat devra ressembler à ![image](logistique1.png)

> Remarques : Il n'y a pas de vérificateur car c'est une fonction graphique.  
Ne pas oublier de copier coller votre fonction `u(mu,u0,n)`.  
Pour la dernière courbe affichée, on peut voir que plus la valeur de $`\mu`$ augmente, plus la suite devient chaotique dans le sens où il devient difficile de prédire la valeur de $`u_n`$ alors que pour  $`\mu=1,6`$, c'est très facile vu qu'elle se "stabilise" autour d'une seule valeur.

@[Représentation graphique 1]({"stubs": ["TP/logistique_graphique1.py"], "command": "python3 TP/logistique_graphique1_Test.py"})

## Représentation graphique II
`Difficulté : Difficile`


---

## Sensibilité aux conditions initiales
`Difficulté : Moyenne`


---

## Diagramme de bifurcation
`Difficulté : Difficile`

---

## Prolongements possibles

On pourra observer les comportements d'autres suites comme par exemple $`u_{n+1}=\mu sin(u_n)`$ ou $`u_{n+1}=\mu- u_n^2`$.

Un prolongement possible est aussi l'étude de la fonction logistique $`f(x)=\mu x(1-x)`$ mais sur l'ensemble des nombres complexes. On obtient alors l'ensemble de Mandelbrot.
