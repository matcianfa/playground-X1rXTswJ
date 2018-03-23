def mon_programme(phrase):
    dic={'a':['à','â','ä'],'e':['é','è','ë','ê'],'c':['ç'],'i':['ï','î'],'o':['ö','ô'],'u':['ù','û']}
    phrase= phrase.lower()
    endroit=""
    envers=""
    #On se débarasse des accents
    for lettre in dic:
        for lettre_accentuée in dic[lettre]:
            phrase=phrase.replace(lettre_accentuée,lettre)
    #On ne garde que les lettres
    for car in phrase:
        if car in "azertyuiopmlkjhgfdsqwxcvbn":
            endroit=endroit+car
            envers=car+envers
    if envers==endroit:
        print('PALINDROME')
    else:
        print('PAS PALINDROME')
