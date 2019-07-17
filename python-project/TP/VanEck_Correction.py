def VanEck(n):
    liste = [0]
    for i in range(n):
        v_n = liste[-1] # Je prends le dernier terme calculé
        # Je cherche de combien je dois reculer pour retomber sur la même valeur v_n
        for recul in range(1,len(liste)):
            if liste[-recul-1] == v_n : # Si on l'a trouvé, le terme suivant est recul donc on l'ajoute à la liste et on arrete la boucle
                liste.append(recul)
                break
        else : # Si on ne l'a jamais trouvé (donc pas de break d'où l'utilisation de else), on rajoute 0
            liste.append(0)
    return liste
