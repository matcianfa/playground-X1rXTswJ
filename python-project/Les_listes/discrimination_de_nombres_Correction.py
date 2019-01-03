def ma_fonction(n,max):
    reponse=[]
    for k in range(max+1):
        if str(n) not in str(k):
            reponse.append(k)
    return reponse
