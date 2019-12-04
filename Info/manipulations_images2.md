# Manipulations d'images (Seconde partie)

## Fondu de deux images

On peut, à partir de deux images, créer un mélange des deux. Pour cela, on commence par choisir dans quelle proportion on veut les mélanger (par exemple 60% de la première et donc 40% de la seconde). Ensuite, il suffit de prendre, pour chaque couleur de chaque pixel, 60% de la valeur de la première image et 40% de la valeur de la seconde image.

Ainsi, si par exemple le premier pixel de la première image est de couleur (10,20,30) et le premier pixel de la seconde image est de couleur (100,100,100) alors l'image mélangée sera de couleur `(0.6*10 + 0.4*100, 0.6*20 + 0.4*100, 0.6 * 30 + 0.4*100)` c'est à dire `(46, 52, 58)`.

Modifier le script suivant pour qu'il mélange `image` et `image2` avec une proportion de 60% de la première et 40% de la seconde.

::: Astuce numpy
Ici c'est presque trop facile puisque multiplier un tableau numpy par un nombre multiplie chacun de ses termes. 
Seul détail technique, il faut penser à transformer le résultat final en tableau à valeur entière inférieure à 255 (en appliquant `np.asarray(..., dtype=np.uint8)` au résultat)
::: 

@[Fondu de deux images]({"stubs": ["Info/Manip_image_fondu.py"], "command": "sh -c 'python3 Info/Manip_image_fondu.py && python3 Info/afficher_images.py'"})

## Redimensionner

Supposons que nous voulions redimensionner notre image qui est de dimension *a0* lignes et *b0* colonnes en une nouvelle dimension *a1* lignes et *b1* colonnes. On peut noter alors les ratios des transformations selon les lignes et les colonnes : `ratio_lignes = a0/a1` et `ratio_colonnes = b0/b1`.  
Pour remplir notre nouvelle image, il suffit alors de remplir le pixel situé à la ligne *ligne* et la colonne *col* avec les couleurs du pixel de l'image de départ situé à la ligne `int(ligne*ratio_lignes)` et la colonne `int(col*ratio_colonnes)`.

Remarque : Si on fait ainsi, lors d'un agrandissement, plusieurs pixels de l'image de départ seront recopiés donnant une impréssion de gros pixels. Il existe beaucoup de façon d'empecher ce phénomène en lissant les couleurs par différentes méthodes mais nous ne nous y intéresserons pas ici.

Modifier le script suivant pour qu'il affiche une image en sortie de dimension 300 lignes et 300 colonnes. 

@[Redimensionner une image]({"stubs": ["Info/Manip_image_redimensionner.py"], "command": "sh -c 'python3 Info/Manip_image_redimensionner.py && python3 Info/afficher_images.py'"})

## Faire tourner


## Contraste

## jeu des erreurs

## Filtres...
