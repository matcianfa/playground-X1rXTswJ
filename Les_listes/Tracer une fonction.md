# Tracer la courbe représentative d'une fonction
`Difficulté : Moyenne`

Pour tracer une courbe, une calculatrice ou un ordinateur ne calcule pas les coordonnées de tous les points de la courbe (il y en a une infinité). Ils se contentent de calculer régulièrement des valeurs de la fonction puis relie les points par des segments qui ne se voient presque pas à l'oeil nu. C'est ce que nous allons faire.

On considère donc une fonction ***f*** sur un intervalle [a,b]. On note ***n*** le nombre de segments que nous allons tracer pour représenter notre courbe.
Pour ce faire, on va procéder par étape :
1. On crée une liste ***liste_abscisses*** de n+1 abscisses répartis uniformément sur l'intervalle [a,b]. Pour cela, on crée une liste contenant la suite de valeurs : $`a`$, $`a+\frac{b-a}n`$, $`a+2\frac{b-a}n`$, $`a+3\frac{b-a}n`$ , ... ,  $`a+n\frac{b-a}n`$ (On peut remarquer que ce dernier élément vaut $`b`$).
2. On crée une liste ***liste_ordonnées*** de n+1 ordonnées dans laquelle on calcule dans le même ordre les images par ***f*** des éléments de la liste des abscisses précédente ce qui donnera la liste [ $`f(a)`$, $`f\left(a+\frac{b-a}n\right)`$, $`f\left(a+2\frac{b-a}n\right)`$, ... ,  $`f\left(a+n\frac{b-a}n\right)`$]
3. On affiche les segments reliant les points ayant pour abscisses les valeurs dans ***liste_abscisses*** et comme ordonnées les valeurs dans ***liste_ordonnées***. Pour cela nous allons utiliser la fonction `plot`de matplotlib de la façon suivante : `plt.plot(liste_abscisses,liste_ordonnées)`.  
On peut même rajouter des arguments comme par exemple la couleur ou la façon de tracer les courbes :  
`plt.plot(liste_abscisses,liste_ordonnées,color="blue",linestyle=":")` donnera une courbe bleue tracer en pointillés.
::: Détails pour quelques arguments possibles de `plot`
+ Pour les couleurs : Le paramètre `color=` permet de changer la couleur du tracé. Cette couleur peut être donnée sous plusieurs formes.
    - Sous forme de chaîne de caractères représentant les noms (ou abréviations) pour les couleurs primaires, le noir et le blanc : b ou blue, g ou green, r ou red, c ou cyan, m ou magenta, y ou yellow, k ou black, w ou white. C’est quand même assez explicite, il suffit d’écrire les noms en anglais.
    - Sous la forme d’un tuple correspondant aux valeurs RGB de la couleur. Cependant, ce tuple doit contenir des valeurs entre 0 et 1 (il suffit alors de diviser les valeurs RGB par 255). Ainsi, ce sera color = (255 / 255, 0, 0) pour obtenir du rouge. Notons que nous pouvons ajouter une valeur (toujours entre 0 et 1) à ce tuple pour représenter la transparence alpha.
    - Sous la forme de chaîne de caractères représentant la couleur en notation hexadécimale. On aura donc color = '#00FF00' pour obtenir du vert.
    - Et les adeptes des nuances de gris pourront donner en paramètre une chaine de caractère correspondant à l’intensité en gris. Par exemple color = '0.8' permet d’obtenir un gris pâle.
+ Pour les styles de lignes : On utilise le paramètre `linestyle=`.
    - "-" est le style par défaut, il correspond à une ligne pleine ;
    - "--" correspond à une ligne en pointillés ;
    - ":" correspond à une ligne formée de points ;
    - "-." correspond à une ligne formée d’une suite de points et de tirets.
+ Pour les points qu'on demande de tracer : De base, ils ne sont pas mis en valeurs pour avoir une jolie courbe mais si on veut les afficher pour les voir, on peut ajouter le paramètre `marker=` suivit d'un des choix suivant.
    - "x" pour une croix.
    - "o" pour un rond
    - "." pour un point
    - Il y a plein d'autres possibilités comme "*", "+" ... 
:::

Le but de cet exercice est de créer un programme qui prend en entrée ***f***, ***a***, ***b*** et ***n*** et qui affiche la courbe. Pour vérifier les calculs, vous devez aussi renvoyer en fin de programme vos deux listes en utilisant `return liste_abscisses,liste_ordonnées` (le nom des listes étant à modifier selon votre choix de nom pour ces listes).

> Entrée : La fonction ***f***, les bornes ***a*** et ***b*** de l'intervalle sur lequel on trace la fonction et le nombre ***n*** de segments pour tracer la courbe.

> Sortie : Votre programme devra tracer avec `plt.plot` en suivant la méthode décrite au dessus et il devra de plus renvoyer les deux listes ***liste_abscisses*** et ***liste_ordonnées*** qui ont servi à tracer la courbe en utilisant `return liste_abscisses,liste_ordonnées`. Cette dernière étape ne sert qu'à vérifier que votre programme est juste. C'est inutile si on souhaite juste tracer la courbe.

@[Tracer la courbe représentative d'une fonction]({"stubs": ["Les_listes/Tracer_une_courbe.py"], "command": "python3 Les_listes/Tracer_une_courbe_Test.py"})
