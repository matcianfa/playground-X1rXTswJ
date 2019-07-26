from math import *
import matplotlib.pyplot as plt

def u(n) :
    if n== 0 : return 0
    return (n+0.15)*n**0.5
    
    
def x(n):
    liste = [0]
    for i in range(1,n+1):
        liste.append(liste[i-1]+ cos(2*pi*u(i)))
    return liste
    

def y(n):
    liste = [0]
    for i in range(1,n+1):
        liste.append(liste[i-1]+ sin(2*pi*u(i)))
    return liste
    
N=100000
plt.axis('equal')
plt.plot(x(N),y(N),linewidth=1)
plt.show()
