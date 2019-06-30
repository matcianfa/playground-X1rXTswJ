# Projet : IA de jeux

## Présentation

Le but de cette page est de présenter un squelette de projet réalisable avec les élèves et les outils qui peuvent être utile pour le réaliser.

L'idée est de proposer aux élèves de programmer une IA permettant de jouer à des jeux existants déjà sur ordinateur ou même telephone ou tablette.  
Pour que l'élève ait juste à programmer l'IA du jeu, il va falloir lui fournir toutes les données utiles et pour cela, nous allons voir quelques modules pythons intéressants.

Le plan d'attaque est à peu près celui la :
- récupération des données graphiques et traduction en données utilisables (mots, scores etc.)
- IA (la partie que l'élève aura à gérer)
- sorties clavier et souris

Après, libre à vous pour les élèves les plus avancés de les laisser faire plus que l'IA ou de laisser différents groupes gérer sa partie.

D'un point de vue pratique, il est indispensable de donner aux élèves ce qu'ils auront comme entrées (par exemple une matrice de lettre) et ce qu'ils doivent donner en sortie de manière très précise (par exemple une liste de commandes avec un format précis).
En effet, pour bien structurer le projet, chacune des trois parties étant indépendantes, elles devront être écrites dans des fichiers distincts et le programme sera lancé dans un quatrième qui importera les 3 autres et les mettra en relation.

## Le jeu

Tout d'abord quelques mots sur le jeu. L'idée est d'utiliser un jeu déjà existant et non pas de le reprogrammer. La motivation venant du fait qu'il pourra ensuite comparer son IA à d'autres joueurs. Pour cela, plusieurs possibilités : 
- Si le jeu existe en version ordinateur (jeux facebook par exemple), alors aucun soucis, il suffira de le lancer
- Si le jeu est un jeu mobile, on pourra utiliser un emulateur qui vous permettra d'émuler un mobile sur votre ordinateur. Par exemple pour Android, on pourra par exemple utiliser [Memu Play](https://www.memuplay.com/fr/). 

L'avantage des jeux mobiles ou facebook c'est qu'ils sont en général assez simples à utiliser (la souris suffit) et les utilisateurs s'imaginent peu qu'on puisse faire jouer un programme à notre place.

## Récupération des données graphiques

L'idée est simple : On fait des captures d'écran. Pour cela, on peut utiliser  ImageGrab de la bibliothèque PIL.

PIL est un bibliothèque classique, elle est souvent déjà installée. Si ce n'est pas le cas, il suffit de taper sur la ligne de commande `pip install PIL` (ou bien dans EDUpython d'aller dans le menu Outils> Outils> Installation d'un nouveau module)

Exemple d'utilisation :

``` python
from PIL import  ImageGrab # Pour faire la capture d'ecran

# On capture la zone de l'écran entre le pixel de coordonnées (100,200) et (400,300)
image=ImageGrab.grab(bbox=(100,200,400,300))

#  Prétraitement de l'image
image = image.convert('L')    # convertit en echelle de gris
image = image.point(lambda x: 0 if x < 140 else 255) # Noir et blanc

# Sauvegarde de  l'image 
image.save("capture.png")
```

J'ai mis quelques exemples de prétraitement de l'image avant son utilisation car c'est souvent utile d'en faire pour éviter d'avoir trop de données à gérer. Il existe énormément de traitements de l'image possibles, il faut choisir les plus pertinents. On pourra se référer à la doc PIL.

Nous aurons besoin faire des captures d'écran pour tous les jeux mais certains peuvent demander de se plonger beaucoup plus dans le module PIL ce qui peut faire un bon entrainement. Par exemple : Memory (où il faut retrouver les paires de cartes identiques) ou bien le jeu des 7 différences.

### Comment voir ce qu'on a capturé ?

Petite sous partie pas indispensable mais utile tout de même car il est toujours important de vérifier qu'on envoit bien les bonnes données à notre IA avant de se lancer dedans.

Pour les jeux relativement statiques comme par exemple les 7 différences, un sudoku, un labyrinthe, ou même le memory... , on prend seulement une image au début ou peut-être quelques autres ensuite mais le nombre est faible. Dans ce cas, le plus simple est d'enregistrer les images (comme dans l'exemple précédent) et visualiser à la main (en les ouvrant) que l'image est bien celle qu'on veut (après traitement).

Pour les jeux plus dynamiques, on va prendre énormément de captures et très souvent donc impossible de vérifier à la main. Dans ce cas, le plus simple est de créer une fenêtre dans laquelle on affiche l'image au fur et à mesure. Attention tout de même, cela peut nuir à la performance de votre IA donc il vaudra mieux désactiver cet affichage une fois que tout semble opérationnel.

Pour cela, on peut utiliser Open-CV. Pour l'installer, il faut taper dans la ligne de commande `pip install opencv-python`. Il faut le module `numpy` pour utiliser Open-cv donc à installer (avant) si ce n'est déjà fait.

Exemple d'utilisation
``` python
from PIL import  ImageGrab
import cv2 # Module d'Open-CV

while True:
    # On capture la zone de l'écran entre le pixel de coordonnées (100,200) et (400,300)
    image=ImageGrab.grab(bbox=(100,200,400,300))
    #  Prétraitement de l'image
    image = image.convert('L')    # convertit en echelle de gris
    
    # On traduit notre image en format PIL en une matrice numpy pour pouvoir utiliser Open CV
    capture =  np.array(image)
    # On affiche le résultat. 
    cv2.imshow('window',cv2.cvtColor(capture, cv2.COLOR_BGR2RGB))
    
    # On attend 100 ms avant de continuer pour voir si on appuye sur une touche. Si on appuye sur 'q', on arrete la boucle infinie
    if cv2.waitKey(100) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break
```





