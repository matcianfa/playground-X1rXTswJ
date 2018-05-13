# On va bien sur utiliser l'égalité de Pythagore pour vérifier si le triangle est rectangle.

p_max = 0 # La valeur de p max trouvée
n_max = 0 # Le nombre de solutions trouvée pour p_max

for p in range(3,1001):
    compteur=0 #Compte le nombre de solutions trouvées
    for a in range(1,p-1):
        for b in range(a,p-a):# Vu la façon de compter de l'énoncé, on peut considérer a<=b<=c
            c=p-a-b
            if a*a+b*b>c*c : break  # Pour gagner du temps : si pour un b, le calcul a²+b² dépasse c², ca ne sert à rien de continuer d'augmenter b...
            if a*a+b*b==c*c : 
                compteur+=1
    if compteur>n_max : # Si on a trouvé plus de solutions que le max précédent alors on sauvegarde ces nouvelles valeurs
        n_max=compteur
        p_max=p
    
print(p_max)
