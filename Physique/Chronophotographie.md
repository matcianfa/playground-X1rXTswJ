# Chronophotographie

Cette page est dédiée à quelques idées pour exploiter une chronophotographie avec python.  
Tous les scripts qui suivent ne pourront pas être lancés directement sur cette page car le site ne prend pas en charge les interactions. Il faudra donc faire des copier coller dans un interpreteur python (comme Edupython par exemple).

## Programme pour ouvrir une chronophotographie

Voici une fonction à copier coller dans votre éditeur python préféré pour pouvoir ouvrir une chronophotographie (sous forme d'image .jpg par exemple), selectionner des points en cliquant dessus et obtenir en sortie la liste des coordonnées sous la forme liste_des_abscisses, liste_des_ordonnées pour pouvoir l'exploiter directement avec matplotlib.  
Remarque : Les coordonnées obtenues sont celles dans le repère dont l'origine est située en bas à gauche de l'image et les axes orientés classiquement en mathématique (vertical vers le haut pour les ordonnées).

Pour l'utiliser c'est alors très simple, il suffit de taper :

``` python
X,Y = image_to_coord()
```
On peut ensuite exploiter la liste des X et la liste des Y comme on le souhaite. On donne quelques exemples ci-dessous.

::: Dérouler pour voir le code
```python
import tkinter as tk
from tkinter import filedialog
import pygame
from pygame.locals import *

def ouvrir_fichier():
    """
    Pour ouvrir l'explorateur pour selectionner le fichier image à ouvrir
    Entrée : None
    Sortie : Chemin absolu du fichier ouvert
    """
    popup=tk.Tk()
    chemin_fichier =  filedialog.askopenfilename(initialdir = "./",title = "Select file",filetypes = (("images","*.jpg *.jpeg *.png *.bmp *.gif"),("all files","*.*")))
    popup.destroy()
    return chemin_fichier

def image_to_coord(chemin_fichier=""):
    """
    Propose de charger une image, l'affiche et permet de placer des points
    pour ensuite récupérer les coordonnées sous forme de liste de couples.
    L'origine du repère est placé en bas à gauche de l'image et la direction est verticale ascendante (comme en math et non comme python)
    Entrée : le chemin d'acces au fichier image (ou pas)
    Sortie : liste des x , la liste des y (pour pouvoir l'utiliser directement avec matplotlib)
    """
    #Les constantes/variables :
    liste_points=[]
    dimension_fenetre=(800,600)

    #------------------Mes fonctions intermédiaires
    # Trace le point
    def trace_point(centre,color=(255,0,0),epaisseur=2):
        """
        Trace le point de coordonnées centre
        """
        x,y=centre
        pygame.draw.circle(fenetre,color , (int(x),int(y)),epaisseur)

    #----------------------------
    if not chemin_fichier :
        chemin_fichier=ouvrir_fichier()
    # Ouvre la fenetre pygame et initialise un peu tout
    pygame.init()
    fenetre = pygame.display.set_mode(dimension_fenetre)
    # Afficher un fond blanc
    fond = pygame.Surface(fenetre.get_size())
    fond = fond.convert()
    fond.fill((255,255,255))
    fenetre.blit(fond,(0,0))
    # La police de caractère
    font=pygame.font.SysFont("Arial",12,bold=False,italic=False)

    # On charge l'image
    try:
        if chemin_fichier :
            image=pygame.image.load(chemin_fichier).convert()
        else :
            image=None
        pygame.mouse.set_cursor(*pygame.cursors.broken_x)
    except :
        print("Erreur lors du chargement de l'image\n Vérifier que le chemin entré est le bon")
        #On recommence à demander un fichier
        chemin_fichier=ouvrir_fichier()

    # Gestion des touches
    continuer=1
    while continuer:
        pygame.time.Clock().tick(20) # Pour éviter de trop rafraichir
        for event in pygame.event.get():   #On parcours la liste de tous les événements reçus
            if event.type == QUIT :     #Si un de ces événements est de type QUIT
                continuer = 0      #On arrête la boucle
            # Si on clique, on rajoute le point
            if event.type == MOUSEBUTTONDOWN and event.button == 1 :
                    x,y=event.pos
                    liste_points.append((x+1,y+1)) # On décale car le viseur est décalé...
            if event.type == KEYDOWN:
                # Espace réinitialise la liste des points
                if event.key==K_SPACE:
                        liste_points=[]
                # Touche suppr ou backspace pour supprimer le dernier point ajouté
                elif event.key==K_DELETE or event.key==K_BACKSPACE :
                    liste_points=liste_points[:-1]
                # Entrée pour valider les points
                elif event.key==K_RETURN:
                    x0,y0,h=rect.x,rect.y,rect.height
                    pygame.quit()
                    return zip(*[(x-x0,h-y+y0) for x,y in liste_points]) # On décale pour que l'origine soit en bas à gauche de l'image
        #On affiche l'image si elle existe
        if image is not None:
            rect = image.get_rect()
            rect.center=(dimension_fenetre[0]//2,dimension_fenetre[1]//2)
            fenetre.blit(image,(rect.x,rect.y))
        # On affiche les points enregistrés
        for point in liste_points :
            trace_point(point)
        # On affiche les textes
        text=font.render("Cliquer pour créer un point",1,(0,0,220))
        fenetre.blit(text,(15,15))
        text=font.render("Entrée : Valider les points",1,(0,0,220))
        fenetre.blit(text,(15,30))
        text=font.render("Retour arrière : Supprimer le dernier point",1,(0,0,220))
        fenetre.blit(text,(15,45))
        text=font.render("Espace : Réinitialiser la liste des points",1,(0,0,220))
        fenetre.blit(text,(15,60))

        pygame.display.flip() # Pour rafraichir l'affichage
    pygame.quit()
```
:::

--- 

## Quelques exemples d'utilisation

### Afficher une trajectoire d'ajustement d'ordre 2 à partir de coordonnées de points

L'intérêt d'utiliser un ajustement polynomial d'ordre 2 est de gommer un peu les erreurs de mesures en tout genre.
Voici un exemple de code utilisant la fonction précédente. On n'oubliera donc pas de mettre le code de la fonction image_to_coord ci-dessus aussi.

::: Dérouler pour voir le code
```python
import matplotlib.pyplot as plt
import numpy as np

# On récupère les coordonnées sur une chronophotographie :
X,Y= image_to_coord()
# On transforme nos listes en 'numpy.array' (Pour pouvoir calculer le polynome d'ajustement et l'afficher facilement)
X=np.array(X)
Y=np.array(Y)
# On dessine les points correspondant avec matplotlib :
plt.scatter(X,Y)
# polyfit donne les coefficients du polynome de regression (d'ordre 2 ici)
a,b,c=np.polyfit(X,Y,2)
# On affiche le polynome :
plt.plot(X,a*X**2+b*X+c)
# On montre le résultat :
plt.show()
```
:::

Voici le même code dans lequel on affiche en plus l'image utilisée dans matplotlib ainsi que la courbe polynomiale sur toute la longueur et largeur de l'image.

::: Dérouler pour voir le code
``` python
import matplotlib.pyplot as plt
import numpy as np
import PIL # Pour gerer les images

# On ouvre et affiche l'image
chemin_image=ouvrir_fichier()
image=np.asarray(PIL.Image.open(chemin_image))
plt.imshow(image[::-1],origin='lower') #[::-1] pour inverser l'image car matplotlib inverse les axes pour les images (!?)
longueur_image=len(image[0])
hauteur_image=len(image)

# On récupère les coordonnées sur une chronophotographie :
X,Y= image_to_coord(chemin_image)
# On dessine les points correspondant avec matplotlib :
plt.scatter(X,Y)
# polyfit donne les coefficients du polynome de regression (d'ordre 2 ici)
a,b,c=np.polyfit(X,Y,2)
# On prolonge les X tant que la courbe d'ajustement reste dans l'image
X=np.array([x for x in np.linspace(0,longueur_image,201) if 0 <= a*x**2+b*x+c <= hauteur_image])
# On affiche le polynome :
plt.plot(X,a*X**2+b*X+c)
# On montre le résultat :
plt.show()
```
:::

---

### Afficher les vecteurs vitesses et accélérations

Une fois obtenues les coordonnées des points, on peut afficher les vecteurs vitesses et accélérations.  
Pratiquement, on utilisera pour le vecteur vitesse $`\overrightarrow{v_i}`$ le calcul suivant : $`\overrightarrow{v_i}=\dfrac{\overrightarrow{OM_{i+1}}-\overrightarrow{OM_{i-1}}}{2\Delta t}`$ pour lisser un peu les erreurs d'approximations lorsqu'on clique pour selectionner la position. On fait de même pour les accélérations. C'est pour cela qu'il manquera les vecteurs en début et fin de mouvement.

Ne pas oublier d'ajouter le code de la fonction image_to_coord qui se trouve en haut de cette page pour que le script qui suit fonctionne.

::: Dérouler pour voir le code
```python
import matplotlib.pyplot as plt
import numpy as np

# Dt est le temps entre 2 photos de la chronophotographie.
# Cette valeur est donc à modifier en fonction de la photo.
Dt=0.25

# On récupère les coordonnées sur une chronophotographie :
X,Y= image_to_coord()
# On trace les points
plt.plot(X,Y,"rx")
# On trace les vecteurs vitesses moyennes entre le précédent et le suivant
for i in range(1,len(X)-1):
    plt.arrow(X[i],Y[i],(X[i+1]-X[i-1])/(2*Dt),(Y[i+1]-Y[i-1])/(2*Dt),width=1)
# On peut même rajouter les accelerations
for i in range(2,len(X)-2):
    plt.arrow(X[i],Y[i],(X[i+2]-2*X[i]+X[i-2])/(4*Dt**2),(Y[i+2]-2*Y[i]+Y[i-2])/(4*Dt**2),width=1,color='b')
plt.show()
```
:::

Remarque : Même avec la meilleure volonté du monde, on obtient assez rarement des vecteurs accélérations parfaitement verticaux pour un mouvement de chute. Une partie de cette "erreur" est due à l'imprécision lorsqu'on clique. Un façon de minimiser cette imprécision est d'utiliser la loupe (fournie de base dans Windows) qui grossit la zone autour du pointeur de la souris augmentant largement la précision.

On peut utiliser les observations qu'on obtient pour vérifier ou mettre en place la deuxième loi de Newton, pour mettre en évidence des forces de frottements...

---

### Prolongements possibles

Une fois qu'on a les coordonnées des points d'une chronophotographie, on peut en déduire des vitesses comme dans la partie précédente et calculer les différentes energies pour montrer la conservation de l'énergie mécanique (ou pas) par exemple.
