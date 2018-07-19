# L'idée est la suivante : Déjà on ne regarque que les exposants, le problème revient à trouver une suite d'exposants tels que chaque terme est la somme de deux précédents. Le but étant d etrouver la plus courte.
# Pour connaitre la suite la plus courte qui arrive à n On va donc partir de 1 et à chaque étape, on calcule la somme des derniers exposants qu'on a obtenus avec tous ceux les précédents jusqu'à arriver à n.

# Fonction qui donne la longueur de la suite la plus courte qui se termine en n
def longueur_mini(n):
    liste_suites=[[1]] # Liste dans laquelle on met toutes les suites qu'on construit au fur et à mesure. On commence par les suites de longueur 1 puis il y aura celles de longueur 2 etc.
    while True :
        nv_liste_suites=[] 
        for liste_prec in reversed(liste_suites): # On inverse pour gagner un peu en vitesse car a priori, plus le dernier terme est grand plus on arrivera vite à n...
            dernier=liste_prec[-1]
            for el in liste_prec:
                nouveau = el + dernier
                if nouveau<n : # Si on a trouvé la suite qui termine en n, on la renvoie. Ca sera forcément la plus courte
                    nv_liste_suites.append(liste_prec+[nouveau])
                elif nouveau ==n :
                    return len(liste_prec)+1
                else : 
                    break # Si nouveau > n, tous ses suivants le seront aussi donc inutile de continuer à chercher
        liste_suites=nv_liste_suites.copy()
        

print(sum([longueur_mini(n)-1 for n in range(2,201)])) # Ne pas oublier d'enlever 1 pour avoir le nombre de multiplications
            
