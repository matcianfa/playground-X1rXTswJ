# Art algorithmique

Le but de cette page est de présenter un exemple d'"oeuvre algorithmique". Certains artistes comme Vera Molnar utilisent des algorithmes pour créer leurs oeuvres. 

## Créations des suites 

Créer trois fonctions `u(n)`, `x(n)` et `y(n)` permettant de calculer respectivement les suites définies par :  
$`\left\lbrace\begin{array}{l} u_0=x_0=y_0=0 \\ u_n = (n+0.15)*\sqrt{n} \\ x_{n+1}=x_n + cos(2\pi u_n) \\ y_{n+1} = y_n + sin(2\pi u_n)\end{array}\right.`$

La fonction `u(n)` devra renvoyer directement la valeur de $`u_n`$ mais les fonctions `x(n)` et `y(n)` devront renvoyer la ***liste*** des valeurs des suites $`(x_n)`$ et $`(y_n)`$ de 0 jusqu'à n.

@[Définition des suites]({"stubs": ["TP/art_algo.py"], "command": "python3 TP/art_algo_Test.py"})

---

## Représentation

Admirons maintenant notre oeuvre : Compléter le script suivant pour qu'il affiche les lignes reliant les points de coordonnées $`(x_n,y_n)`$. 

On pourra s'amuser à modifier le nombre 0.15 qui apparait dans la fonction `u(n)` (en 0.25 par exemple) ou bien la puissance de n (mettre n**0.45 au lieu de $`\sqrt n`$) pour voir differentes figures se dessiner.

@[Représentation]({"stubs": ["TP/art_algo_graphique.py"], "command": "python3 TP/art_algo_graphique_Test.py"})
