def mon_programme(mot):
    mot=mot.replace('COMPT','')
    mot=mot.replace('MPH','')
    mot=mot.replace('PH','')
    mot=mot[:-3]+mot[-3:].replace('MP','')
    if 'P' in mot[:-1] or 'M' in mot or 'B' in mot :
        print('TOUCHE')
    else:
        print('TOUCHE PAS')
