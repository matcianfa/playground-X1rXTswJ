# Compléments sur le module matplotlib

Nous allons présenter ici comment parametrer l'affichage des graphiques avec matplolib comme par exemple le choix de la couleur et de la façon de tracer les courbes, des axes, du titre etc.

## Paramétrisation rapide des courbes

Dans la partie précédente du cours sur matplotlib, nous avons vu la fonction `plt.plot(X,Y)` qui permet de tracer lessegments dont les extrémités sont les points de coordonnées (x,y) avec x dans X et y dans Y. Cette fonction peut prendre beaucoup de paramètre qui permette de configurer l'affichage de notre courbe comme on le souhaite. Une remarque au passage : je prendrais l'exemple de la fonction `plt.plot` mais ce qui suit peut fonctionner dans beaucoup d'autres fonctions du module matplotlib.

Une première façon de configurer les courbes est d'utiliser le formatage rapide sous forme de chaine de 1 à 4 caractères qui résume les propriétés principales de la courbe : un caractère pour la couleur, un pour le style de point et un (ou deux) pour le style de la ligne. Ce paramètre se place après les X et Y dans la fonction `plot`.

Par exemple si je veux tracer une courbe en rouge (caractère "r") avec de gros points (caractère "o") et en ligne pointillée (caractères "--"), il faudra que j'écrive `plt.plot(X,Y,"ro--")` Ce qui donnera :

@[Tracé de fonctions]({"stubs": ["Maths/cplt_plot1.py"], "command": "python3 Maths/cplt_plot1_Test.py"})

On voit donc que c'est très facile de modifier rapidement une courbe mais forcément le choix des modifications est restreint. Si un paramètre n'est pas précisé alors c'est le choix par défaut qui est pris. On peut donc décider de ne configurer que le style de trait ( en n'écrivant que `plt.plot(X,Y,"--")` par exemple ) ou bien que la couleur... Un cas très utile est celui du choix du style de point uniquement car il permet de retirer les segments et donc n'afficher que les points. Ainsi `plt.plot(X,Y,"o")` n'affichera que les points et non la courbe.

Voici un résumé des caractères les plus couramment utilisés.
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





