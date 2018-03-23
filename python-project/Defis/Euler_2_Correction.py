u1=1
u2=2
somme=0
while u2<4000000:
    if u2%2==0 : somme+=u2
    u1,u2=u2,u1+u2

print(somme)
