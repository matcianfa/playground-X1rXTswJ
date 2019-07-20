#Ne pas oublier de changer le module à importer
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt

fig=plt.figure()
import Newton_graphique
fig.savefig('output.png', dpi=fig.dpi)
print("TECHIO> open -s /project/target/ index_grossissant.html")
