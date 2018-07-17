# On développe en utilisant le binome de Newton et on trouve : 
# si n est pair =2[a²]
# si n est impair = 2na[a²]. Donc le maximum est atteint pour 2na<a² c'est à dire n < a/2 d'où : r_max = 2*((a-1)//2)*a

somme=0
for a in range(3,1001):
    somme+= 2*((a-1)//2)*a
print(somme)
