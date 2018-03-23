def mon_programme(n):
    n=n-1
    mot='G'
    while n>0:
        nouveau_mot=''
        mot+='G'
        while mot!='':
            début=mot[:2]
            if début=='GG':
                nouveau_mot+='GGDG'
            elif début=='DG':
                nouveau_mot+='GDDG'
            elif début=='GD':
                nouveau_mot+='GGDD'
            else:
                nouveau_mot+='GDDD'
            mot=mot[2:]
        mot=nouveau_mot[:-1]
        n-=1
    print(mot)
