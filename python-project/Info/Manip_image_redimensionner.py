from PIL import Image, ImageDraw
import numpy as np

# On charge l'image et on la transforme en tableau contenant les couleurs
image = np.asarray(Image.open("Info/Lenna.png"))
a0,b0,_ = image.shape
# Dimensions finales (modifiables)
a1,b1 = 300,300

ratio_lignes = a0/a1
ratio_colonnes = b0/b1

# Partie à compléter
image_sortie = np.zeros((a1,b1,3),dtype = np.uint8)
for ligne in range(a1):
    for col in range(b1):
        for i in range(3):
            image_sortie[ligne,col,i] = ...

# On sauvegarde les images pour pouvoir les afficher
Image.fromarray(image).save("image_entree.png")
Image.fromarray(image_sortie).save("image_sortie.png")
