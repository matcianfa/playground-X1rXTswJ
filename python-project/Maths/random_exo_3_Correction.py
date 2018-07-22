from random import *

jeu=["Pierre", "Caillou", "Ciseaux"]
liste=[]
for _ in range(100):
    liste.append(choice(jeu))
print(liste)

######################################################################
#Version 1 ligne:

print([choice(["Pierre", "Caillou", "Ciseaux"]) for _ in range(100)])
