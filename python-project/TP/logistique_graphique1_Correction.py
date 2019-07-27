import matplotlib.pyplot as plt

def u(mu,u0,n):
    liste = [u0]
    u = u0
    for _ in range(n):
        u = mu*u*(1-u)
        liste.append(u)
    return liste
    
def dessiner(mu,u0,n):
    X = list(range(n+1))
    Y = u(mu,u0,n)
    plt.plot(X,Y,".-",linewidth=1)
    plt.show()
