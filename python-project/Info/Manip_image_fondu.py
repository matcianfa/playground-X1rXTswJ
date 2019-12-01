from PIL import Image, ImageDraw
import numpy as np

# On charge l'image et on la transforme en tableau contenant les couleurs
image = np.asarray(Image.open("Info/Lenna.png"))
image2 = np.asarray(Image.open("Info/subliminale.png"))
nb_lignes,nb_colonnes,_ = image.shape

# Partie à compléter
image_sortie = np.copy(image)
for ligne in range(nb_lignes):
    for col in range(nb_colonnes):
        for i in range(3):
            image_sortie[ligne,col,i] = ...

# On sauvegarde les images pour pouvoir les afficher
Image.fromarray(image).save("image_entree.png")
Image.fromarray(image_sortie).save("image_sortie.png")
