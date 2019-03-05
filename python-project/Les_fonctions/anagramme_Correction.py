def anagramme(mot):
    if mot=="": return [""]
    else:
        liste_anagrammes=[]
        for lettre in mot:#Je balaye tous les lettres du mot
            sous_mot=mot.replace(lettre,"")#Je retire la lettre prise du mot
            for ana in anagramme(sous_mot):#Pour tous les anagrammes du mot privé de lettre
                liste_anagrammes.append(lettre+ana)#Je forme lettre+ana et je le rajoute à la liste
        return liste_anagrammes
