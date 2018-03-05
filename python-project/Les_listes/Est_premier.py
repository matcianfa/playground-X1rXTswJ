from math import sqrt

def est_premier(n):
  if n<2 or (n%2==0 and n!=2):
      return False
  else:
      for d in range(3,int(sqrt(n))+1,2):
          if n%d==0:
              return False
      else:
          return True
