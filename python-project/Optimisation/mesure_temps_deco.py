from time import time 

def chrono(fonction):
    def lancer(*args, **kwargs):
        t_i = time()
        resultat = fonction(*args, **kwargs)
        t_f = time()
        print("temps d'execution (en s):", t_f-t_i)
        return resultat
    return lancer
    
@chrono
def fonction_à_tester(n):
    somme=0
    for i in range(1,n):
        if n%i==0:
            somme+= i
    return somme        

print(fonction_à_tester(10**7))
