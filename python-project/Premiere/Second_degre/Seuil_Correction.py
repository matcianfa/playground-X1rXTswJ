def ma_fonction(n):
    if n<150:
        return "Impossible"
    else :
        t=0
        while 3*t*t+69*t+150 < n :
            t+=1
        return t
