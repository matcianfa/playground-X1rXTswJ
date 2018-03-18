def mon_programme(n):
    if n<2:
        print("PAS PREMIER")
    else:
        for d in range(2,n):
            if n%d==0:
                print("PAS PREMIER")
                break
        else:
            print("PREMIER")
