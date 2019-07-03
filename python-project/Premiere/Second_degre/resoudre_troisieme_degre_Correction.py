def ma_fonction(a,b,c,d,r):
        p=b/a+r
        q=-d/(a*r)
        delta=p*p-4*q
        if delta<0 : 
                return "Pas de solution"
        elif delta == 0 : 
                return -p/2
        else : 
                x1=(-p-delta**0.5)/2
                x2=(-p+delta**0.5)/2
                return min(x1,x2),max(x1,x2)
