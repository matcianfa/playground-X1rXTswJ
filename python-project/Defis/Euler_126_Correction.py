# Un peu galère de se représenter la figure pour trouver une formule et encore plus de l'expliquer
# Déjà, on peut remarquer que pour la première couche, il faut rajouter 2(pq+qr+pr)
# Pour la couche d'après, on remet une couche identique sur celle qu'on a rajouté donc il y a encore 2(pq+qr+pr) cubes a ajouter mais en plus, il faut compléter les coins qui sont tous de la forme px1x1, qx1x1 et rx1x1. Il y en a 4 de chaque donc au total pour la deuxième couche, il faut 2(pq+qr+pr) + 4(p+q+r)
# Le coup d'après, On rajoute encore une couche sur la première donc 2(pq+qr+pr). Et ca forme comme un escalier ou cette fois ci il y a 2 fois plus de coins qu'avant à combler donc 8(p+q+r) cubes a mettre. Enfin, Sur les bords de cet escalier, il faut rajouter 1 cubes à chaque marche, ce qui fait 8 en tout. Au final, on a 2(pq+qr+pr) + 8(p+q+r) + 8 cubes necessaires
# Essayons de généraliser. Il faut s'imaginer  que ca forme comme un escalier (vu de coté). La couche d'après, on a toujours 2(pq+qr+pr). On rajoute une marche à notre escalier (dans tous les sens). A l'étape n on a donc n-1 escaliers formé par des blocs px1x1, qx1x1 rx1x1 4 fois (par symétrie) donc 4(n-1)(p+q+r) cubes. Et chacune des n-2 marches de l'escalier de l'étape d'avant, pour la première ligne, un cube suffit, pour la deuxième, il en faut 2 celle d'arpès 3 etc. ce qui donne 1 + 2+ 3+ ... + (n-2)= (n-2)*(n-1)/2 pour chaque coin donc on multiplie ensuite par 8.


#Donne le nombre de cubes necessaires pour recouvrir n fois un parallélépipède de dimension pxqxr.
def n_cubes(p,q,r,n):
    return 2*(p*q+q*r+p*r) + 4*(n-1)*(p+q+r+n-2)
    


# valeur max de n donnée à priori (100000 au début puis une fois trouvé la réponse, on peut baisser un peu pour gagner en vitesse)
n_max = 20000

# but
but=1000

# fonction qui cherche
# Pour des raisons de symétrie, on peut chercher uniquement pour p>=q>=r
def chercher():
    global n_max
    # dictionnaire qui compte
    compteur = {}
    p=1
    while n_cubes(p,1,1,1)<=n_max :
        q=1
        while q<=p and n_cubes(p,q,1,1)<=n_max:
            r=1
            while r<=q and n_cubes(p,q,r,1)<=n_max :
                n=1
                n_temp = n_cubes(p,q,r,n)
                while n_temp <= n_max :
                    compt_temp=compteur.setdefault(n_temp,0)
                    compteur[n_temp]=compt_temp+1
                    n+=1
                    n_temp = n_cubes(p,q,r,n)
                r+=1
            q+=1
        p+=1
    n_min = n_max
    for cle,val in compteur.items():
        if val == but and cle<n_min:
            n_min=cle
    return n_min
    
print(chercher())

    
