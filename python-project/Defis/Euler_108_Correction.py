''' Pour résoudre ce probleme, on peut déja remarquer que, comme x et y sont positifs, x>n et y>n. Donc on peut écrire x=n+a et y=n+b.
A partir de la notre equation est équivalente à  n²=a*b
Donc le nombre de solutions est égal au nombre sigma(n²) de diviseurs de n². Pour avoir le nombre de solutions distinctes, une fois retirée la solution symétrique n*n, il faut diviser par 2. Cela revient à chercher sigma(n²)> 2000.
Si n est de la forme p1^a1*p2^a2*pk^ak alors sigma(n²)=(2*a1+1)(2*a2+1)*...*(2*ak+1)
Comme 3^7> 2000, on voit qu'il suffit de chercher pour k<=6. 
De plus comme on cherche le minimum des n possibles, on peut supposer p1=2,p2=3,...,p6=13.
Comme p1<p2<...<p6, et qu'on cherche n minimal on peut supposer aussi 2a1+1 >= 2a2+1 >= ... >= 2a6+1. 
Et comme on veut le plus petit n tel que sigma(n²)> 2000, il est donc inutile de chercher pour des valeurs de a6 telles que (2a6+1)^6 > 2000 donc a6<=(2000^1/6 -1)/2. On peut faire le même raisonnement pour les 5 autres ak.

On va donc tester toutes les valeurs des ak pour trouver celles qui donnent le plus petit n
'''

#Majorants pour les boucles des ak
exposants_max=[int((2000**(1/k)-1)/2)+1 for k in range(1,7)]

#fonction qui cherche
def chercher():
    n_min=2*3*5*7*11*13*17 # le carré de ce nombre a 3^7 diviseurs donc plus de 1000
    for a6 in range(exposants_max[5]):
        for a5 in range(a6,exposants_max[4]):
            for a4 in range(a5,exposants_max[3]):
                for a3 in range(a4,exposants_max[2]):
                    for a2 in range(a3,exposants_max[1]):
                        for a1 in range(a2,exposants_max[0]):
                            if (2*a1+1)*(2*a2+1)*(2*a3+1)*(2*a4+1)*(2*a5+1)*(2*a6+1)>2000 :
                                temp = 2**a1*3**a2*5**a3*7**a4*11**a5*13**a6
                                if temp<n_min:
                                    n_min = temp
    return n_min
    
                                    
print(chercher())

