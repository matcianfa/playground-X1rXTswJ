import matplotlib.pyplot as plt

def u(mu,n):
    liste = [0.5]
    u=0.5
    for i in range(n):
        u=mu*u*(1-u)
        liste.append(u)
    return liste
    
def dessiner(mu,n):
    liste = u(mu,n)
    X = [z.real for z in liste]
    Y = [z.imag for z in liste]
    plt.plot(X,Y, ".-",linewidth=1)
    plt.show()
