from PIL import Image, ImageDraw
import numpy as np

# On charge l'image et on la transforme en tableau contenant les couleurs
image = np.asarray(Image.open("Info/Lenna.png"))
nb_lignes,nb_colonnes,_ = image.shape

# On commence par chercher la valeur de i_min et i_max
i_min, i_max = 255,0
for ligne in range(nb_lignes):
    for col in range(nb_colonnes):
        r,v,b =[int(x) for x in image[ligne, col]]
        i = (r+v+b)/3
        i_min = min(i_min, i)
        i_max = max(i_max, i)
        
# Partie à compléter
image_sortie = np.copy(image)
for ligne in range(nb_lignes):
    for col in range(nb_colonnes):
        r,v,b =[int(x) for x in image[ligne, col]]
        i = ...
        i_n = ...
        image_sortie[ligne,col] = ...


# On sauvegarde les images pour pouvoir les afficher
Image.fromarray(image).save("image_entree.png")
Image.fromarray(image_sortie).save("image_sortie.png")
