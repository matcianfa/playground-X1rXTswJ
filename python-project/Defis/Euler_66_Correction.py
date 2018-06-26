# On va utiliser les méthodes de résolutions des équations de Pell Fermat avec les fractions continues qu'on peut trouver par exemple ici : https://fr.wikipedia.org/wiki/%C3%89quation_de_Pell-Fermat#%C3%89quation_de_Pell_et_entier_alg%C3%A9brique
# L'idée est donc de calculer les valeurs du numérateur de la fraction continue partielle donnée par le critère qui est sur la page Wikipédia qui est en fait la solution minimal cherchée.


# On va mémoizer les suites pour gagner en temps
from functools import lru_cache

@lru_cache(maxsize=None)
def m(n,S):
    if n==0: return 0
    return d(n-1,S)*a(n-1,S)-m(n-1,S)
    
@lru_cache(maxsize=None)
def d(n,S):
    if n==0: return 1
    return (S-m(n,S)**2)//d(n-1,S)
    
@lru_cache(maxsize=None)
def a(n,S):
    if n==0: return int(S**0.5)
    return int((a(0,S)+m(n,S))/d(n,S))
    
@lru_cache(maxsize=None)
def h(n,D):
    if n==-2 : return 0
    if n==-1 : return 1
    return a(n,D)*h(n-1,D)+ h(n-2,D)
    
@lru_cache(maxsize=None)
def k(n,D):
    if n==-2 : return 1
    if n==-1 : return 0
    return a(n,D)*k(n-1,D)+ k(n-2,D)
    
x_max=0
D_max=0
for D in range(1001):
    deux_a_0=2*a(0,D)
    p=0
    try: # Pour exclure les carrés parfait qui vont donner des erreurs de division par 0, je capture l'exception
        while a(p,D)!=deux_a_0: #On utilise la propriété qui dit que la dernière valeur d'un cycle est le double de a_0
            p+=1
    except ZeroDivisionError:
        p=0
    # maintenant qu'on a p, on utilise le critère :
    if p%2==0 :
        x= h(p-1,D)
    else :
        x= h(2*p-1,D)
    if x>x_max:
        x_max=x
        D_max=D
        
print(D_max)
