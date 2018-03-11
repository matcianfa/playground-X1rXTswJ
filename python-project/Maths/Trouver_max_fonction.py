pas=0.01

#Fonction qui donne le maximum d'une fonction f sur l'intervalle [a,b]
def maximum(f,a,b):
  #Au cas où on se trompe dans l'ordre de a et b, on les remet dans le bon sens :
  if b<a: a,b=b,a
  #On commence à chercher le maximum pour x=a
  x=a
  maximum= f(a)
  #On essaye pour toutes les valeurs de x si f(x) est plus grand que le maximum qu'on a deja trouvé, en augmentant x du pas à chaque fois
  while x<b:
    y=f(x)
    if y>maximum:
      maximum=y
    x+= pas
  return maximum
