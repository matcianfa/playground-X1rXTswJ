def mon_programme(n,p):
    somme=0
    for i in range(1,n+1):
      somme+=i**p
    print(somme)

#Version en une ligne :
def mon_programme(n,p):
    print(sum([(i+1)**p for i in range(n)]))
