def mon_programme(mot_1,mot_2):
    mot_1_inversé=''
    #Je renverse mot_1
    for lettre in mot_1:
        mot_1_inversé=lettre+mot_1_inversé
    if mot_1_inversé==mot_2:
        print('ANACYCLIQUE')
    else:
        print('PAS ANACYCLIQUE')
