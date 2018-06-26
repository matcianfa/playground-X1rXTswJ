# Méthode bourrin : On teste toutes les façons de remplir le graphe et on elimine celles qui ne vérifie pas les conditions.

from itertools import permutations


# Fonction qui verifie si le graphe est bon. Pour les numéros, de 1 à 5 c'est dans le pentagone intérieur et dans la continuité, de 6 à 0.
def vérif(liste):
    return liste[0]< liste[6] and liste[0]< liste[7] and liste[0]< liste[8] and liste[0]< liste[9] and liste[1]+liste[2]+liste[7]==liste[2]+liste[3]+liste[8]== liste[3]+liste[4]+liste[9]==liste[4]+liste[5]+liste[0]==liste[5]+liste[1]+liste[6]  # Les premières conditions sont là pour garder celles qui commencent par la plus petite et éviter ainsi les mêmes configurations à rotations près.
    
liste_config_valides=[]

for config in permutations(range(1,11)):
    if vérif(config):
        # On transforme la config en chaine de caractère.
        config=[str(c) for c in config]
        mot=config[0]+config[5]+config[4]+config[9]+config[4]+config[3]+config[8]+config[3]+config[2]+config[7]+config[2]+config[1]+config[6]+config[1]+config[5]
        if len(mot)==16:
            liste_config_valides.append(mot)

print(sorted(liste_config_valides)[-1])        
