# Méthode en utilisant les fonctions Python adaptées
import itertools

for i,n in enumerate(itertools.permutations("0123456789")):
    if i==999999 : print(int("".join(n)))

--------------------------------------------------------------------------------
#Méthode en enlevant autant de factorielle qu'il faut au fur et à mesure
# Exemple: Il y a 9!=362880 nombres commençant par 0 et autant par 1 donc le millionième commence forcément par 2
# Si je retire les nombres commençant par 0 et 1, il reste 274240 nombres. 8! =40320. 274240//8! =6 Donc c'est le sixième chiffre mais comme on a retiré 2, c'est le chiffre 7 etc...
# Comme j'ai besoin de la fonction factorielle, je la crée rapidement
def factorielle(n):
    return 1 if n<2 else n*factorielle(n-1)
    
liste=[0,1,2,3,4,5,6,7,8,9]
N=1000000
réponse=""
while liste!=[] :
    fact=factorielle(len(liste)-1)
    q,N = N//fact,N%fact
    if N==0 : #Si on tombe sur un multiple de fact, ca correpond au q précédent (Ca veut simplement dire qu'on prend la dernière permutation possible pour un nombre
        q-=1
        N+=fact
    réponse+=str(liste[q])
    liste.remove(liste[q])

print(réponse)
