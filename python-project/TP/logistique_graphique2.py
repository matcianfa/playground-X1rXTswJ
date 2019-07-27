import matplotlib.pyplot as plt
import numpy as np

# Copier coller votre fonction u(mu,u0,n) ci-dessous





# La fonction à compléter :
def dessiner(mu,u0,n):
    # Tracé de f(x) = mu * x * (1-x)
    X = np.linspace(0,1,100)
    Y = ...
    plt.plot(X,Y)
    
    # Tracé de y=x
    ...
    
    # Tracé de la suite
    U = u(mu,u0,n)
    for i in range(n):
        # Tracé du trait vertical joignant (u_i;u_i) à (u_i, u_(i+1))
        plt.plot([U[i],U[i]],[U[i],U[i+1]],"r",linewidth=1)
        # Tracé du trait horizontal joignant (u_i;u_(i+1)) à (u_(i+1); u_(i+1))
        plt.plot( ... ,"r",linewidth=1)
    
    plt.axis("equal") # Pour avoir un repère orthonormé
    plt.show()
