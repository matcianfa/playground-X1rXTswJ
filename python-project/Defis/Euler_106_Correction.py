# Bien qu'on parle de la même chose que dans les problèmes 103 et 105, ici on n'a pas besoin de ce qu'on a fait avant. Par contre, ce qui suit est une résolution grandement mathématiques, la part de programmation est ridicule par rapport aux autres problemes ce qui m'étonne un peu mais je n'ai pas trouvé plus simple comme méthode.
''' L'idée est de regarder dans un premier temps le nombre de façons de choisir deux ensembles de même cardinal. Appelons le k. 
Il suffit de regarder le coefficient multinomial (qui généralise le coefficient binomial :
Le nombre de façon de choisir une partition d'un ensemble à n éléments en ensembles de cardinaux respectifs k1,...k_p est :  n!/(k1!*k2!*...*kp!)
Attention car parmi ces partitions, l'ordre compte c'est à dire que si k1=k2, des partitions sont comptées en double. Il fuadrait donc diviser par 2 pour enlever ce problème d'ordre.
Ici, si on veut uniquement 2 ensembles de cardinal k, cela donne : n!/(2*k!*k!*(n-2k)!)

Dans un second temps, intéressons nous aux ensembles parmi ceux trouvés ci-dessus qui n'ont pas besoin d'être vérifié car il est évident par construction qu'ils vérifient S(B)!=S(C).
Par exemple, (1,2,5) et (3,4,6) ne donnent pas la même somme car 1<3, 2<4 et 5<6. Ainsi, si tous les éléments du premier ensemble sont inférieurs un à un à ceux du second, pas besoin de faire le moindre calcul pour conclure. On se demande donc combien il y a de tels ensembles. Un vision astucieuse et de partir de l'ensemble ordonné 1,2,3,4,5,6 et leur associer des parenthèses comme suit : ((())). La première parenthèse ouvrante représente 1, la deuxième 2 etc.
Ainsi on peut se convaincre assez facilement qu'une expression bien parenthésée correspond à un cas où on peut comparer directement les ensembles par comparaison des éléments un à un
Par exemple (()()) correspond à la partition 1,2,4 et 3,5,6. Et réciproquement chaque ensemble comparable directement peut être associé à un bon parenthésage.
Or on sait que le nombre de bon parenthésage avec k parenthèses ouvrantes est donné par les nombres de Catalan C_k=(2k!)/((k+1)!k!).
Ce nombre est donc le nombre de choix parmi les façons de prendre 2 partitions d'une partition de longueur 2k donnée dont il est inutile de regarder par le calcul s'il fonctionnent. Or il y a n!/(2k!*(n-2k)!) façons de prendre une partition de longueur 2k

En résumé le nombre qu'on cherche est : 
n!/(2*k!*k!*(n-2k)!)-n!/(k!*(k+1)!*(n-2k)!) = (n!/(k!²*(n-2k)!))*(k-1)/(2(k+1))
'''

from functools import lru_cache

# La fonction factorielle
@lru_cache(maxsize=None)
def factorielle(n):
    if n==0 or n==1 : return 1
    return n*factorielle(n-1)
    
# fonction qui cherche
def chercher(n=12):
    somme=0
    for k in range(1, n//2+1):
        somme+= ((k-1)*factorielle(n))//(2*(k+1)*factorielle(n-2*k)*factorielle(k)**2)
    return somme
    
print(chercher())
        
