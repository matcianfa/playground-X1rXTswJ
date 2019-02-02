# Compléments sur le module matplotlib

Nous allons présenter ici comment parametrer l'affichage des graphiques avec matplolib comme par exemple le choix de la couleur et de la façon de tracer les courbes, des axes, du titre etc.

## Paramétrisation rapide des courbes

Dans la partie précédente du cours sur matplotlib, nous avons vu la fonction `plt.plot(X,Y)` qui permet de tracer les segments dont les extrémités sont les points de coordonnées (x,y) avec x dans X et y dans Y. Cette fonction peut prendre beaucoup de paramètre qui permette de configurer l'affichage de notre courbe comme on le souhaite. Une remarque au passage : je prendrais l'exemple de la fonction `plt.plot` mais ce qui suit peut fonctionner dans beaucoup d'autres fonctions du module matplotlib.

Une première façon de configurer les courbes est d'utiliser le formatage rapide sous forme de chaine de 1 à 4 caractères qui résume les propriétés principales de la courbe : un caractère pour la couleur, un pour le style de point et un (ou deux) pour le style de la ligne. Ce paramètre se place après les X et Y dans la fonction `plot`.

Par exemple si je veux tracer une courbe en rouge (caractère "r") avec de gros points (caractère "o") et en ligne pointillée (caractères "--"), il faudra que j'écrive `plt.plot(X,Y,"ro--")` Ce qui donnera :

@[Tracé de fonctions]({"stubs": ["Maths/cplt_plot1.py"], "command": "python3 Maths/cplt_plot1_Test.py"})

On voit donc que c'est très facile de modifier rapidement une courbe mais forcément le choix des modifications est restreint. Si un paramètre n'est pas précisé alors c'est le choix par défaut qui est pris. On peut donc décider de ne configurer que le style de trait ( en n'écrivant que `plt.plot(X,Y,"--")` par exemple ) ou bien que la couleur... Un cas très utile est celui du choix du style de point uniquement car il permet de retirer les segments et donc n'afficher que les points. Ainsi `plt.plot(X,Y,"o")` n'affichera que les points et non la courbe.

Voici un résumé des caractères les plus couramment utilisés. On pourra trouver une liste complète dans la [documentation](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.plot.html) de matplotlib
+ Pour les couleurs  
::: Cliquer pour voir la liste

| Caractère | Couleur correspondante |
|:---------:|:----------------------:|
| 'b' | bleu |
| 'g' | vert |
| 'r' | rouge |
| 'c' | cyan |
| 'm' | magenta |
| 'y' | jaune |
| 'k' | noir |
| 'w' | blanc |

:::

+ Pour le style de point

::: Cliquer pour voir la liste

| Caractère | Style de point correspondant |
|:---------:|:----------------------:|
| '.' | Un petit point |
| 'O' | Un gros point |
| ',' | Un pixel |
| '+' | Un + |
| 'x' | Un x |
| '\*' | Une étoile |

:::


+ Pour le style de de ligne

::: Cliquer pour voir la liste

| Caractère(s) | Style de ligne correspondant |
|:---------:|:----------------------:|
| '-' | Ligne continue |
| '--' | Ligne discontinue |
| '-.' | Alternance de points et tirets |
| ':' | Ligne pointillée |

:::

## Paramétrisation plus précise des courbes

Nous allons voir comment modifier davantage encore notre courbe. La liste des propriétés modifiables est très grande donc nous n'allons voir que les plus courantes. Pour modifier une propriétés, il suffit de rajouter dans la fonction `plot` le nom de la propriété = la valeur que l'on désire. Par exemple si je veux modifier l'épaisseur du trait à 3, j'écrirai `plt.plot(X,Y,linewidth=3)`.

::: Voici quelques propriétés modifiables :

+ `color` : Pour modifier la couleur. Il y a beaucoup de façon de définir une couleur pour matplotlib. La plus simple est d'utiliser un triplet RGB (rouge, vert, bleu) de nombres entre 0 et 1. Autrement dit, `color=(1,0,0)` correspondrait à du rouge, `color=(0,0,1)` à du bleu et `color=(1,0,1)` à du magenta.  
Un exemple de modification serait donc : `plt.plot(X,Y,color=(0.1,0.4,0.6))`  
On peut aussi modifier la couleur de chaque point du graphique. Pour cela, il suffit de donner une liste de même longueur que la liste des X et Y contenant la couleur que l'on veut pour chaque point.

+ `label` : Permet d'associer un label à ce qu'on dessine. C'est le nom qui apparaitra dans la légende de la figure par exemple. 
Un exemple de modification serait donc : `plt.plot(X,Y,label="Courbe n°1")` 

+ `linestyle` : Permet de modifier le style de ligne. Ce sont les mêmes arguments que pour la modification rapide du style de ligne autrement dit "-", "--", "-.", ":" ou "" pour ne pas afficher de ligne.  
Un exemple de modification serait donc : `plt.plot(X,Y,linestyle="--")` 

+ `linewidth` : Permet de modifier l'épaisseur de la ligne.  
Un exemple de modification serait donc : `plt.plot(X,Y,linewidth=3)` 

+ `markeredgecolor` et `markerfacecolor` : Permet de modifier la couleur des marqueurs (c'est à dire les points que l'on a placé). `markeredgecolor` modifie le contour et `markerfacecolor` modifie l'intérieur du marqueur.  
Un exemple de modification serait donc : `plt.plot(X,Y,"o",markeredgecolor=(1,0,0),markerfacecolor=(0,1,0))`

+ `markersize` : Permet de modifier la taille des marqueurs (c'est à dire des points que l'on a placé).  
Un exemple de modification serait donc : `plt.plot(X,Y,"o",markersize=3)` 

:::

Voici un exemple combinant toutes les modifications de propriétés précédentes :
@[Modifications plus précises]({"stubs": ["Maths/cplt_plot2.py"], "command": "python3 Maths/cplt_plot2_Test.py"})

