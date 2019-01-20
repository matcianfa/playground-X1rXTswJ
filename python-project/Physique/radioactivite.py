# On précise notre constante
a=-0.1
# On crée la liste des temps : 1000 points entre t=0 et t=50. 
# Plus on met de points plus la résolution sera précise
temps = np.linspace(0, 50,1000)

# L'équation différentielle sous forme de fonction :
def equation(Y,temps):
    return a*Y

#On résout notre équation différentielle et on récupère la liste des résultats
Y=odeint(equation, [10], temps)

#On affiche le résultat des Y en fonction du temps
plt.plot(temps,Y)
# On montre le résultat
plt.show()
