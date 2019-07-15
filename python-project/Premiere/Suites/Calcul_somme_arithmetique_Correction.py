# Première méthode : en utilisant une formule
def ma_fonction(u0,r,i,j):
    return u0*(j-i+1) + r*(j*(j+1)-i*(i-1))/2
    
"""
# Seconde méthode : on calcule la somme 
def  ma_fonction(u0,r,i,j):
    u = u0+i*r # Le terme ui
    S = u
    for k in range(i,j):
      u += r
      S += u
    return S
    
# Troisieme méthode : en utilisant une autre formule 
def ma_fonction(u0,r,i,j):
    ui = u0 + i*r
    uj = u0 + j*r
    return (j-i+1)*(ui+uj)/2
"""
