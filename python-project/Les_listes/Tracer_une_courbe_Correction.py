import matplotlib.pyplot as plt

def ma_fonction(f,a,b,n):
    #On crée notre liste des abscisses uniformément répartis
    liste_abscisses=[a]
    x=a
    pas=(b-a)/n
    for _ in range(n-1):
        x+=pas
        liste_abscisses.append(x)
    liste_abscisses.append(b)
    #On crée la liste des images de la liste précédente
    liste_ordonnées=[f(x) for x in liste_abscisses]
    plt.plot(liste_abscisses,liste_ordonnées)
    return liste_abscisses,liste_ordonnées 
