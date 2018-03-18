def mon_programme(a,b,u_0,n):
    u=u_0
    for i in range(n) :
        u=a*u+b
    print(u)
