from PIL import Image, ImageDraw
import numpy as np

# On charge l'image et on la transforme en tableau contenant les couleurs
image_entrée = Image.open("Lenna.png")
image = np.asarray(image_entrée)

# On crée notre image de sortie (ici on fait juste une copie de l'image originale)
image_sortie =Image.fromarray(image)

# On sauvegarde les images pour pouvoir les afficher
Image.fromarray(image).save("image_entrée.png")
image_sortie.save("image_sortie.png")

