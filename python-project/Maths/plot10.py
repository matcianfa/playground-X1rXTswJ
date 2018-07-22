import matplotlib.pyplot as plt
import numpy as np
from random import *

# Fonction qui crée la liste de couleurs en fonction de la condition
def donner_couleur(x,y):
    couleurs=[]
    for i in range(len(x)):
        if y[i]<x[i]**2 : couleurs.append("r")
        else : couleurs.append("b")
    return couleurs
    
x = [random() for _ in range(5000)]
y = [random() for _ in range(5000)]
plt.scatter(x,y,s=1,c=donner_couleur(x,y))

plt.show()
