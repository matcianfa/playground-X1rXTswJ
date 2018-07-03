from time import time

Max=10**5
liste=[n*n for n in range(Max//10)]
ens= set(liste)
dic={}
for carré in liste:
    dic[carré]=1

t_0= time()

for el in range(Max):
    if el in liste:
        pass
    
t_1= time()

for el in range(Max):
    if el in ens : 
        pass
        
t_2 = time()

for el in range(Max):
    if el in dic : 
        pass
    
t_3 = time()

print("Parcourt d'une liste : {} secondes".format(t_1-t_0))
print("Parcourt d'un ensemble : {} secondes".format(t_2-t_1))
print("Parcourt d'un dictionnaire : {} secondes".format(t_3-t_2))
