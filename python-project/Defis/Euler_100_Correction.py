# Le force brute est beaucoup trop longue ici.
# Attention la méthode qui suit demande pas mal de maths. On s'appuie sur la résolutions des équations de Pell Fermat qu'on peut trouver par exemple ici : https://fr.wikipedia.org/wiki/%C3%89quation_de_Pell-Fermat#Cas_m_=_%E2%80%931 
'''
On remarque que l'équation b(b-1)/(t(t-1))=1/2 où b est le nombre de bleu et t le nombre total revient à l'equation diophantienne 2b²-2b-t²+t=0.
On peut transformer cette équation en 8b²-8b-4t²+4t=0 ce qui donne 2(2b-1)²-(2t-1)²=1. Pour ce ramener exactement à une équation de Pell Fermat, on mulitplie par -1 ce qui donne en posant B=2b-1 et T=2t-1 :
T²-2B²=-1
D'après Wikipédia, les solutions sont alors générée par la suite T_0=1, B_0=1 (qui est solution évidente) et T_(k+1)= T_k + 2 B_k et B_(k+1) = B_k + T_k avec k pair. 
Comme ce qui nous intéresse ce n'est que les k pair, on calcule le rang (k+2) en fonction du rang k on obtient une suite de solutions donnée par :
T_(k+2)=3 T_k + 4 B_k et B_(k+2)=2 T_k + 3 B_k pour k pair
Si on revient aux suites de départ b_k et t_k qui nous intéressent, en utilisant B_k= 2b_k-1 et de même pour t_k, on en déduit que ces suites vérifient :
t_(k+2) = 3 t_k + 4 b_k - 3 et b_(k+2) = 2 t_k + 3 b_k -2 pour k pair et t_0 = 1 et b_0 = 1
On voit facilement que cela revient à étudier la suite :
t_(k+1) = 3 t_k + 4 b_k - 3 et b_(k+1) = 2 t_k + 3 b_k -2 pour k entier et t_0 = 1 et b_0 = 1
Les couples donnent des solutions au problème initial, il ne reste qu'à trouvé la valeur de t qui dépassera 10^12

'''
from functools import lru_cache

# On définit nos suites et on mémoize
@lru_cache(maxsize=None)
def t(k):
    if k==0 : return 1
    return 3*t(k-1)+4*b(k-1)-3
 
@lru_cache(maxsize=None)
def b(k):
    if k==0: return 1
    return 2*t(k-1)+3*b(k-1)-2
    
k=0
while t(k)<10**12:
    k+=1
    
print(b(k))
