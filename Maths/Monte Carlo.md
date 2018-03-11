# Méthode de Monte Carlo pour le calcul d'aire.
`Difficulté : Moyenne`

Le but de cette fiche est de présenter la méthode de Monte Carlo pour calculer l'aire sous une courbe représentative d'une fonction. Pour simplifier, on supposera ici que nos fonctions sont toutes positives sur l'intervalle sur lequel on les considère.

Définissons d'abord ce qu'est l'aire sous la courbe représentative d'une fonction sur un intervalle [a,b] : C'est tout simplement l'aire comprise entre la courbe représentative, l'axe des abscisses et les droites x=a et x=b.

![Illustration](https://upload.wikimedia.org/wikipedia/commons/thumb/c/c9/Aire_sous_la_courbe.svg/220px-Aire_sous_la_courbe.svg.png)

Décrivons à présent la méthode de Monte Carlo pour calculer l'aire sous la courbe d'une fonction f sur un intervalle [a,b] :
1. On choisit un rectangle qui contient l'aire qui nous intéresse. Le plus simple est de prendre le rectangle dont un coté est le segment [AB] où A(a,0) et B(b,0) et dont l'autre coté vaut le maximum de f sur [a,b].
<div>
<img src="Courbe%20et%20rectangle.png" width="250"/>
</div>
