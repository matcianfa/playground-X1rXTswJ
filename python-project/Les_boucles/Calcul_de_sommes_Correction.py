def ma_fonction(n,p):
    somme=0
    for i in range(1,n+1):
      somme+=i**p
    return somme

#Version en une ligne :
def ma_fonction(n,p):
    return sum([(i+1)**p for i in range(n)])
