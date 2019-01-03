def ma_fonction(n,liste):
    compteur = [0]*(n+1)
    # On comptabilise le nombre d'occurrence de chaque nombre dans la liste
    for nombre in liste: 
        compteur[nombre]+=1
    # On crée la liste ordonnée :
    reponse=[]
    for i in range(n+1):
        reponse+=[i]*compteur[i] #On rajoute à la liste reponse la liste contenant i autant de fois que le nombre d'occurrence dans la liste d'origine
    return reponse
