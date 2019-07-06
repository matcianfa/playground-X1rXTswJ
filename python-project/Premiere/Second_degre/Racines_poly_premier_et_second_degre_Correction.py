def ma_fonction(liste):
  if len(liste)==3:
      a,b,c=liste
      delta=b*b-4*a*c
      if delta<0 : 
        return "Pas de solution"
      elif delta==0:
        return -b/(2*a)
      else :
        x1=(-b-delta**0.5)/(2*a)
        x2=(-b+delta**0.5)/(2*a)
        return min(x1,x2),max(x1,x2)  
  elif len(liste)==2:
      a,b=liste
      return -b/a
  else : 
      return "Je ne sais pas faire"
