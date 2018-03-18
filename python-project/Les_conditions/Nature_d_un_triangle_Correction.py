def mon_programme(a,b,c):
    if a==b==c:
        print("EQUILATERAL")
    elif a==b or a==c or b==c:
        if round(a**2,5)==round(b**2+c**2,5) or round(b**2,5)==round(a**2+c**2,5) or round(c**2,5)==round(a**2+b**2,5) :
            print("RECTANGLE ISOCELE")
        elif a/b==(1+sqrt(5))/2 or b/a==(1+sqrt(5))/2 or a/c==(1+sqrt(5))/2 or c/a==(1+sqrt(5))/2:
            print("TRIANGLE D'OR")
        else:
            print("ISOCELE")
    elif round(a**2,5)==round(b**2+c**2,5) or round(b**2,5)==round(a**2+c**2,5) or round(c**2,5)==round(a**2+b**2,5) :
        print("RECTANGLE")
    else:
        print("QUELCONQUE")
