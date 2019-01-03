def ma_fonction(liste):
    for i in range(1,len(liste)):
        element_a_inserer=liste[i]
        #je décale tous les éléments plus grands que mon élément à insérer vers la droite pour pouvoir l'insérer
        j=i
        while j>0 and liste[j-1]>element_a_inserer:
            liste[j]=liste[j-1]
            j-=1
        #je l'insére
        liste[j]=element_a_inserer
    return liste
