# Projet : Intelligence Artificielle et jeux sur mobiles

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

::: Exemple d'utilisation :

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
:::

J'ai mis quelques exemples de prétraitement de l'image avant son utilisation car c'est souvent utile d'en faire pour éviter d'avoir trop de données à gérer. Il existe énormément de traitements de l'image possibles, il faut choisir les plus pertinents. On pourra se référer à la doc PIL.

Nous aurons besoin faire des captures d'écran pour tous les jeux mais certains peuvent demander de se plonger beaucoup plus dans le module PIL ce qui peut faire un bon entrainement. Par exemple : Memory (où il faut retrouver les paires de cartes identiques) ou bien le jeu des 7 différences.

Une dernière remarque très importante : fixer une bonne fois pour toute l'endroit où votre jeu sera affiché. le plus simple est de mettre en mode fenêtre agrandie ou bien dans un coin. En effet tout ce qui suit dépendra de la capture d'écran mais si à chaque fois qu'on relance le jeu, il faut redéfinir tous les paramètres car la fenêtre de jeu a changé de place (même un pixel de différence peut tout changer), ça devient vite pénible.

### Comment voir ce qu'on a capturé ?

Petite sous partie pas indispensable mais utile tout de même car il est toujours important de vérifier qu'on envoit bien les bonnes données à notre IA avant de se lancer dedans.

Pour les jeux relativement statiques comme par exemple les 7 différences, un sudoku, un labyrinthe, ou même le memory... , on prend seulement une image au début ou peut-être quelques autres ensuite mais le nombre est faible. Dans ce cas, le plus simple est d'enregistrer les images (comme dans l'exemple précédent) et visualiser à la main (en les ouvrant) que l'image est bien celle qu'on veut (après traitement).

Pour les jeux plus dynamiques, on va prendre énormément de captures et très souvent donc impossible de vérifier à la main. Dans ce cas, le plus simple est de créer une fenêtre dans laquelle on affiche l'image au fur et à mesure. Attention tout de même, cela peut nuir à la performance de votre IA donc il vaudra mieux désactiver cet affichage une fois que tout semble opérationnel.

Pour cela, on peut utiliser Open-CV. Pour l'installer, il faut taper dans la ligne de commande `pip install opencv-python`. Il faut le module `numpy` pour utiliser Open-cv donc à installer (avant) si ce n'est déjà fait.

::: Exemple d'utilisation
``` python
from PIL import  ImageGrab
import numpy as np
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
:::

Quelques remarques : Open-cv a besoin qu'on traduise les images en matrice numpy. De plus PIL semble travailler en couleur BGR alors que Open-cv en RGB d'où la commande de conversion entre les deux `cv2.cvtColor(capture, cv2.COLOR_BGR2RGB)`

Normalement le programme précédent prend des captures d'écran toutes les 100ms de la zone, le transforme en nuance de gris et affiche le résultat dans une fenêtre. Si on fait bouger des choses, on peut constater que les modifications sont répércutées en direct. Pour sortir de la boucle infinie, il faut selectionner la fenetre d'open-cv et appuyer sur la touche 'q' du clavier.

## Passer des données graphiques aux données exploitables

Maintenant qu'on sait récupérer ce qu'il se passe à l'écran, il faut réussir à le traduire en données exploitables. 

Tout va dépendre du type de jeu, voici quelques idées en vrac :
- Pour memory, par exemple, on n'a rien besoin de faire puisqu'on va comparer des images.
- Avec un peu de chance et d'astuce, on peut traduire les données juste en regardant les couleurs. Par exemple si chaque personnage ou chaque lettre à une couleur spécifique, pas besoin de faire un traitement d'image compliqué, on regarde juste la couleur des pixel pour savoir ce qu'il se passe et en déduire les données utiles. On peut combiner la couleur avec la postion. Par exemple, on peut deviner la valeur d'une carte juste en regardant à des positions stratégiques la couleur du pixel. donc en une vingtaine de pixel on a notre information. Bien sûr cela demande d'être très précis quand on prend la capture d'ecran mais fait gagner beaucoup de temps.  
Par exemple : le jeu de Go, puissance4, mastermind, 2048, 
- Pour les jeux de lettres ou de chiffres, il va falloir traduire notre image en lettres, mots ou nombres. Soit on peut utiliser une astuce de couleur, position ou autre (cela peut être le nombre de pixels noirs qui caractérise ce qui nous intéresse par exemple ), soit on n'a pas d'autre choix que de faire une reconnaissance graphique de caractère. J'en parle dans la sous-section suivante.
- Certains jeux sont trop complexes pour être traduits simplement (jeux 3D par exemple) donc il vaut mieux rester raisonnable.
- Des fois il est plus simple de rentrer à la main les données : Par exemple si le jeu consiste à donner le mot le plus long formé avec 7 lettres, on a aussi vite fait (avec de l'entrainement) de les retaper que de faire une reconnaissance de caractères.

### Reconnaissance de caractères

Cela consiste à reconnaitre les lettres présentes sur une image. Typiquement, cela peut servir pour des jeux du type Boggle, Scrabble, Sudoku, mots mélés...

Pour cela, on va utiliser le module tesseract. Il est un peu plus complexe à installer. En effet il faut d'abord installer Tesseract OCR que l'on peut trouver ici [Tesseract pour Windows](https://github.com/UB-Mannheim/tesseract/wiki). Ensuite il faut installer le module pytesseract en lançant dans la ligne de commande `pip install pytesseract`. On pourra trouver un tutoriel très bien fait [ici](http://info.blaisepascal.fr/tesseract).

::: Exemple :
``` python
from PIL import  ImageGrab
import numpy as np
import cv2 # Module d'Open-CV
import pytesseract
# Préciser le chemin à  suivre pour le fichier tesseract.exe
pytesseract.pytesseract.tesseract_cmd = 'c:\\Program Files\\Tesseract-OCR-2\\tesseract'


while True:
    # On capture la zone de l'écran entre le pixel de coordonnées (100,200) et (400,300)
    image=ImageGrab.grab(bbox=(100,200,400,300))
    #  Prétraitement de l'image
    image = image.convert('L')    # convertit en echelle de gris

    # On traduit notre image en format PIL en une matrice numpy pour pouvoir utiliser Open CV
    capture =  np.array(image)
    # On affiche le résultat.
    cv2.imshow('window',cv2.cvtColor(capture, cv2.COLOR_BGR2RGB))
    # On récupère le texte sur l'image
    text = pytesseract.image_to_string(image)
    print(text)
    # On attend 1s avant de continuer pour voir si on appuye sur une touche. Si on appuye sur 'q', on arrete la boucle infinie
    if cv2.waitKey(1000) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break
            
```
:::

Si tout va bien, vous devriez voir apparaitre dans votre console tout le texte présent dans la fenêtre capturée.

Très important : il faut préciser le chemin où vous avez installé Tesseract OCR (c'est la ligne qui suit `import pytesseract`) sinon il affiche qu'il n'a pas trouvé tesseract.

C'est assez impressionnant mais :
- c'est relativement lent à executer. Donc quasiment inutilisable pour des jeux où les lettres bougent et changent en permanence et demande de la rapidité.
- c'est une reconnaissance de caractère générique c'est à dire qu'il marche dans énormément de situations et reconnait les mots. Ce qui veut dire qu'il risque de se tromper si on demande une reconnaissance lettre à lettre. J'aurais tendance à dire que c'est un bon outil pour commencer mais si on veut optimiser pour un jeu précis, il va falloir améliorer cette partie là. Cela peut être un bon défi pour les bons groupes de s'attaquer à entrainer un réseau de neurones pour un jeu précis (quitte à prémacher le travail et juste les faire entrainer le réseau) qui reconnaisse les caractères ou bien le score.

## Les sorties clavier et souris

On a vu comment récupérer les données. Les élèves ont fait leur IA qui donne les instructions à suivre. Voyons maintenant comment executer ces instructions c'est à dire réellement jouer au jeu. Pour cela, nous allons utiliser le module pyautogui. Toujours pareil, pour l'installer, on execute `pip install pyautogui` et pour l'importer dans notre script `import pyautogui`.

Je ne vais pas donner d'exemple mais renvoyer plutôt à la [documentation officielle](https://pyautogui.readthedocs.io/en/latest/introduction.html) qui est remarquablement claire. On pourra trouver plus particulièrement comment prendre le controle de la souris et du clavier avec python.

## Exemples

On pourra trouver quelques exemples de projets aboutis dans les pages suivantes.

## Quelques idées 

Voici quelques idées (en vrac) de projets d'IA de jeux qui doivent être réalisables avec les élèves. J'ai mis une * pour les projets qui me semblent plus difficiles à réaliser d'un point de vue IA efficace car il risque de falloir un peu de théorie.

De manière général, la liste des jeux de l'app store et google play dans les rubriques casse tête, jeux de société, jeux de cartes, dés peuvent être une bonne source d'inspiration. D'un point de vu ludique, je pense que les jeux à plusieurs sont plus motivants à programmer pour les élèves que les jeux solos même si certains gardent un défi (obtenir le meilleur score ou temps).

- Memory
- 7 différences
- Mots mélés
- Sudoku
- Labyrinthe
- Mastermind
- Motus
- Puissance 4*
- Jeu de dame, echec, go ******
- Taquin* (version avec les chiffres ou plus dur (pour récupérer les données), version graphique)
- Jeux de dés (Yam's, 421...)
- Jeux de cartes* (Belote, poker, président, Uno, dame de pique,...)
- Scrabble (juste donner la liste des meilleurs mots ou bien carrément jouer seul***)
- Tetris
- Flow free, knots puzzle (trouver comment relier des points sans se croiser)
- Morpion (Tic tac toe en anglais) et Ultimate Tic tac toe*
- Le démineur
- Le pendu
- Dominos, triominos
- Drag n Merge



