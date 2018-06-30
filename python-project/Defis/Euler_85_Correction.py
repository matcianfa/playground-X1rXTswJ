# Pour connaitre le nombre de rectangles dans un rectangle de dimension Lxl il suffit de créer un quadrillage et de choisir 2 points qui représenteront les sommets opposés du rectangle. Or il y a L(L+1)/2 façons de choisir l'abscisse de ces 2 points et l(l+1)/2 pour les ordonnées.
# En résumé dans un rectangle de dimension Lxl, il y a L(L+1)l(l+1)/4 rectangles.
# Tant qu'à faire, on fixe L et on résout notre équation du second degré en l.
# On obtient que L=(1+sqrt(1+32000000/l(l+1)))/2
# Reste à trouver la valeur la plus proche de 2 Million


distance_min=2000000
l_min=0
L_min=0
for l in range(1,int(((2000000)**0.25))+1): # Pour des raisons de symétrie, on peut considérer l<L et donc (l(l+1))²<2000000 ce qui donne une idée de borne sup pour l
    for delta in range(2):
        L=int((-1+(1+32000000/(l*(l+1)))**0.5)/2) + delta
        distance = abs(((l*(l+1)*L*(L+1))//4)- 2000000)
        if distance < distance_min:
            distance_min= distance
            l_min=l
            L_min=L

print(l_min*L_min)    
    
