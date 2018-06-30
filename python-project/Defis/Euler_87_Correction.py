# Methode bourrin : On essaye tout et on compte

N=50000000

#  Ressortons de notre boite à outils la fonction qui permet de savoir si un nombre est premier
def est_premier(n):
    if n==2 : return True
    if n < 2 or n%2==0: return False
    for x in range(3, int(n**0.5) + 1,2):
        if n % x == 0:
            return False
    return True
    
# liste des nombres premiers inférieurs à racine carré de N
# On crée 3 listes distinctes pour gagner du temps et minimiser les comparaisons et calculs
temp = int(N**0.5)+1
premiers2 = [ p for p in range(2,temp) if est_premier(p)]
temp = int(N**(1/3))+1
premiers3 = [ p for p in premiers2 if p<=temp ]
temp = int(N**0.25)+1
premiers4 = [ p for p in premiers3 if p<=temp ]

# Pour gagner du temps on met dans une fonction
def chercher():
    # Ensemble dans lequel on met les nombres qui marchent
    solutions=set([])
    for i in premiers2:
        i_carré=i*i
        for j in premiers3:
            j_cube=j**3
            for k in premiers4:
                temp=i_carré+j_cube+k**4
                if temp<=N:
                    solutions.add(temp)
    return len(solutions)
            
print(chercher())
