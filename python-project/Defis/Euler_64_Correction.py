# L'idée est simplement d'utiliser les résultats sur les fractions continues de racines carrées d'entiers
# On peut par exemple les trouver ici : https://en.wikipedia.org/wiki/Methods_of_computing_square_roots#Algorithm

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
    
# Fonction qui cherche la réponse (on met dans une fonction pour gagner en rapidité
def chercher():
    compteur=0
    for N in range(10001):
        deux_a_0=2*a(0,N)
        n=0
        try: # Pour exclure les carrés parfait qui vont donner des erreurs de division par 0, je capture l'exception
            while a(n,N)!=deux_a_0: #On utilise la propriété qui dit que la dernière valeur d'un cycle est le double de a_0
                n+=1
        except ZeroDivisionError:
            n=0
        if n%2==1 :
            compteur+=1
    return compteur
    
print(chercher())
