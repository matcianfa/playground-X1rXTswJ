'''
# Première méthode assez naturelle mais beaucoup trop lente
# On va tout simplement utiliser les propriétés de ces triangles trouvées sur wikipédia : https://en.wikipedia.org/wiki/Integer_triangle#Isosceles_Heronian_triangles
# Parmi tous les triangles isocèles à périmètre et aire  entièrs, on ne compte que ceux qui sont presque equilatéraux

N_max=10**9
    
def chercher():
    somme=0
    # perimetre = 4u² ou 2(u+v)² ce qui donne une borne pour u
    for u in range(1, int(N_max**0.5)+1):
        for v in range(1,u):
            if (u+v)%2==1:
                u2=u*u
                v2=v*v
                a=2*(u2-v2)
                b=u2+v2
                a_=4*u*v
                if abs(a-b)==1 and 4*u2<N_max :
                    somme+=4*u2
                if abs(a_-b)==1 and 2*(u+v)**2 < N_max :
                    somme+=2*(u+v)**2
    return somme
    
print(chercher())
'''                    
                    
# Deuxième méthode basée sur la même idée au fond mais utilisant une génération des triplets pythagoriciens un peu plus efficace. Les triangles de Héron isocèle proviennent de la juxtaposition de deux triangles rectangles identiques d'où la recherche des triplets pythagoriciens
# Un lien vers la méthode : https://en.wikipedia.org/wiki/Tree_of_primitive_Pythagorean_triples

# transformations A, B et C de wikipédia:
def A(x,y,z): return (x-2*y+2*z, 2*x-y+2*z, 2*x-2*y+3*z)
def B(x,y,z): return (x+2*y+2*z, 2*x+y+2*z, 2*x+2*y+3*z)
def C(x,y,z): return (-x+2*y+2*z, -2*x+y+2*z, -2*x+2*y+3*z)

# On cherche les triplets tels que 2*x=z+-1 ou 2y=z+-1 pour former un triangle isocèle presque equilatéral
N_max=10**9

somme=0
def chercher(liste=[[3,4,5]]):
    global somme
    for x,y,z in liste:
        if x+y+z<N_max :
            if abs(2*x-z)==1 :
                somme += 2*(z +x)
                chercher([A(x,y,z),B(x,y,z),C(x,y,z)])
            elif abs(2*y-z)==1:
                somme+= 2*(z+y)
                chercher([A(x,y,z),B(x,y,z),C(x,y,z)])
            
            
chercher()
print(somme)

# Remarque : On peut constater que les triplets qui marchent sont ceux engendrés par (3,4,5) en enchainant les transformations C puis A puis C puis A ... (Ce qui doit pouvoir se prouver) On peut donc en déduire une méthode encore plus rapide (car la on calcule à chaque fois les 3 triplets)
