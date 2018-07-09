''' On reprend exactement le programme de problème 108
Pour résoudre ce probleme, on peut déja remarquer que, comme x et y sont positifs, x>n et y>n. Donc on peut écrire x=n+a et y=n+b.
A partir de la notre equation est équivalente à  n²=a*b
Donc le nombre de solutions est égal au nombre sigma(n²) de diviseurs de n². Pour avoir le nombre de solutions distinctes, une fois retirée la solution symétrique n*n, il faut diviser par 2. Cela revient à chercher sigma(n²)> 8000000.
Si n est de la forme p1^a1*p2^a2*pk^ak alors sigma(n²)=(2*a1+1)(2*a2+1)*...*(2*ak+1)
Comme 3^15> 8000000, on voit qu'il suffit de chercher pour k<=14. 
De plus comme on cherche le minimum des n possibles, on peut supposer p1=2,p2=3,...,p14=43.
Comme p1<p2<...<p14, et qu'on cherche n minimal on peut supposer aussi 2a1+1 >= 2a2+1 >= ... >= 2a14+1. 
Et comme on veut le plus petit n tel que sigma(n²)> 8000000, il est donc inutile de chercher pour des valeurs de a6 telles que (2a14+1)^14 > 8000000 donc a14<=(8000000^1/14 -1)/2. On peut faire le même raisonnement pour les 13 autres ak.

On va donc tester toutes les valeurs des ak pour trouver celles qui donnent le plus petit n
'''

from math import log

#Majorants pour les boucles des ak
exposants_max=[int((8000000**(1/k)-1)/2)+1 for k in range(1,15)]

#liste des log des nb premiers (on décalle le premier par convenance)
logs=[log(p) for p in [1,2,3,5,7,11,13,17,19,23,29,31,37,41,43]]

#fonction qui cherche
def chercher():
    n_min=2*3*5*7*11*13*17*19*23*29*31*37*41*43*47 # le carré de ce nombre a 3^15 diviseurs donc plus de 8000000
    log_min = log(n_min) # On va travailler avec le log pour éviter les puissances trop grosses
    for a14 in range(exposants_max[13]):
        for a13 in range(a14,exposants_max[12]):
            for a12 in range(a13,exposants_max[11]):
                for a11 in range(a12,exposants_max[10]):
                    for a10 in range(a11,exposants_max[9]):
                        for a9 in range(a10,exposants_max[8]):
                            for a8 in range(a9,exposants_max[7]):
                                for a7 in range(a8,exposants_max[6]):
                                    for a6 in range(a7,exposants_max[5]):
                                        for a5 in range(a6,exposants_max[4]):
                                            for a4 in range(a5,exposants_max[3]):
                                                for a3 in range(a4,exposants_max[2]):
                                                    for a2 in range(a3,exposants_max[1]):
                                                        temp =a2*logs[2]+a3*logs[3]+a4*logs[4]+a5*logs[5]+a6*logs[6]+a7*logs[7]+a8*logs[8]+a9*logs[9]+a10*logs[10]+a11*logs[11]+a12*logs[12]+a13*logs[13]+a14*logs[14] 
                                                        if temp>log_min : # Si on dépasse déjà, on passe au suivant
                                                            break
                                                        a1=int(7999999/(2*(2*a2+1)*(2*a3+1)*(2*a4+1)*(2*a5+1)*(2*a6+1)*(2*a7+1)*(2*a8+1)*(2*a9+1)*(2*a10+1)*(2*a11+1)*(2*a12+1)*(2*a13+1)*(2*a14+1))-0.5)+1
                                                        temp =a1*logs[1]+temp
                                                        if temp<log_min:
                                                            
                                                            n_min = 2**a1*3**a2*5**a3*7**a4*11**a5*13**a6*17**a7*19**a8*23**a9*29**a10*31**a11*37**a12*41**a13*43**a14
                                                            
                                                            log_min=temp
    return n_min
    
                                    
print(chercher())

