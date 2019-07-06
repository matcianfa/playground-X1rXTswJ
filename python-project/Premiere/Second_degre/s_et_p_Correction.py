def ma_fonction(s,p):
  delta = s*s-4*p
  if delta>=0 : 
    x1=(s-delta**0.5)/2
    x2=(s+delta**0.5)/2
    return min(x1,x2),max(x1,x2)
  else :
    return "Pas de Solution"
