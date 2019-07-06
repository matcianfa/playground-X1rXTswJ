def ma_fonction(a,b,c):
  delta = b*b-4*a*c
  solutions=[]  # Pour ranger nos solutions au fur et à mesure
  if delta<0 : return "Pas de solution"
  elif delta==0 :
    X0=-b/(2*a)
    # La cas ou X0==0 est particulier car il n'y aura qu'une seule solution
    if X0==0 : return [0]
    # Si X0>0, deux solutions qui sont la racine de X0 et son opposé
    elif X0>0 : return [-X0**0.5,X0**0.5]
    # Si X0<0, pas de solution
    else : return "Pas de solution"
  else: # Delta >0
    X1=(-b-delta**0.5)/(2*a)
    X2=(-b+delta**0.5)/(2*a)
    # Pour chaque racine, on regarde si on peut prendre sa racine carrée qui seront alors (avec son opposé) les solutions de l'équation bicarrée)
    for X in [X1,X2]:
      if X>0 : 
        solutions.append(-X**0.5)
        solutions.append(X**0.5)
      elif X==0 : 
        solutions.append(0)
    # Si la liste des solutions est vide : pas de solution
    if solutions==[]: return "Pas de solution"
    # Sinon on renvoie la liste triée dans l'ordre croissant
    else : return sorted(solutions)
        
