import matplotlib.pyplot as plt
import numpy as np

def u(mu,u0,n):
    liste = [u0]
    u = u0
    for _ in range(n):
        u=mu*u*(1-u)
        #u = mu*u*(1-u)
        liste.append(u)
    return liste
    
def dessiner(mu,u0,n):
    # Tracé de f
    X = np.linspace(0,1,100)
    Y = mu*X*(1-X)
    plt.plot(X,Y)
    
    # Tracé de y=x
    plt.plot([0,1],[0,1],"k")
    
    # Tracé de la suite
    U = u(mu,u0,n)
    for i in range(n):
        # Tracé du trait vertical joignant (u_i;u_i) à (u_i, u_(i+1))
        plt.plot([U[i],U[i]],[U[i],U[i+1]],"r",linewidth=1)
        # Tracé du trait horizontal joignant (u_i;u_(i+1)) à (u_(i+1); u_(i+1))
        plt.plot([U[i],U[i+1]],[U[i+1],U[i+1]],"r",linewidth=1)
        
    # Tracé de la suite2
    U = u(mu,u0+10**(-13),n)
    print(U[-1])
    for i in range(n):
        # Tracé du trait vertical joignant (u_i;u_i) à (u_i, u_(i+1))
        plt.plot([U[i],U[i]],[U[i],U[i+1]],"g",linewidth=1)
        # Tracé du trait horizontal joignant (u_i;u_(i+1)) à (u_(i+1); u_(i+1))
        plt.plot([U[i],U[i+1]],[U[i+1],U[i+1]],"g",linewidth=1)
    
    plt.axis("equal")
    plt.show()
    
    
 
