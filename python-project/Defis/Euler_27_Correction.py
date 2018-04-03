# renvoie true si le nombre est premier
def est_premier(n):
    if n<2 : return False
    if n==2 : return True
    if n%2==0 : return False
    for d in range(3,int(n**0.5)+1,2):
        if n%d==0: return False
    return True

# fonction qui prend les valeurs de a et b et renvoie le nombre de nombres premiers d'affilée
def tester(a,b):
    n=0
    while est_premier(n*n+a*n+b):
        n+=1
    return n

# On teste tous les a,b entre -1000 et 1000
n_max=0
a_max=b_max=-1000
for a in range(-999,1000,1):
    for b in range(-999,1000,1):
        n=tester(a,b)
        if n>n_max:
            n_max=n
            a_max=a
            b_max=b

print(a_max*b_max)
