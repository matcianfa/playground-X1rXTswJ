# On travaille modulo 10^10

m=28433
p=7830457


# Pour avoir moins de multiplications à faire, on transforme p en binaire
# vu le problème on va travailler modulo 10^10
def puissance(n,p) :
    reponse=1
    while p:
        if p%2==1 : 
            reponse= (reponse*n)%10000000000
        n=(n**2)%10000000000
        p//=2
    return reponse
    
print((m*puissance(2,p)+1)%10000000000)
