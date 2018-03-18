def mon_programme(x_a,y_a,x_b,y_b,x_c,y_c):
    if (x_b-x_a)*(x_c-x_a)+(y_b-y_a)*(y_c-y_a)==0 or (x_a-x_b)*(x_c-x_b)+(y_a-y_b)*(y_c-y_b)==0 or (x_b-x_c)*(x_a-x_c)+(y_b-y_c)*(y_a-y_c)==0:
        print("RECTANGLE")
    else :
        print("PAS RECTANGLE")
