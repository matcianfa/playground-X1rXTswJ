from PIL import Image, ImageDraw
import numpy as np

# On charge l'image et on la transforme en tableau contenant les couleurs
image_lenna = np.asarray(Image.open("Info/Lenna.png"))
image_fond_vert = np.asarray(Image.open("Info/fond_vert.png"))
nb_lignes,nb_colonnes,_ = image_fond_vert.shape

# Partie à compléter
image_sortie = np.copy(image_fond_vert)
for ligne in range(nb_lignes):
    for col in range(nb_colonnes):
        image_sortie[ligne,col] = ...

# On sauvegarde les images pour pouvoir les afficher
Image.fromarray(image_sortie).save("image_sortie.png")
