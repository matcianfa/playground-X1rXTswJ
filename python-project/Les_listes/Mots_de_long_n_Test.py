#Ne pas oublier de changer le module à importer
from Mots_de_long_n import mon_programme
import sys
import io


#liste des couples input/output
input_output=[\
((5,["Cosinus","Sinus","Mathématiques", "Info", "Python", "Tests", "Angle", "Produit scalaire", "Polynome","Carré", "Losange", "Isocele", "Rectangle","Equilateral","Alterne interne", "Cercle","Aire","Perimètre", "Disque","Cone","Cube","Parallèle","Orthogonale", "Dodécaèdre","Icosaèdre","Tetraèdre","Fractale"]),['Sinus', 'Tests', 'Angle', 'Carré']),\
((7,["Cosinus","Sinus","Mathématiques", "Info", "Python", "Tests", "Angle", "Produit scalaire", "Polynome","Carré", "Losange", "Isocele", "Rectangle","Equilateral","Alterne interne", "Cercle","Aire","Perimètre", "Disque","Cone","Cube","Parallèle","Orthogonale", "Dodécaèdre","Icosaèdre","Tetraèdre","Fractale"]),['Cosinus', 'Losange', 'Isocele']),\
((4,["Cosinus","Sinus","Mathématiques", "Info", "Python", "Tests", "Angle", "Produit scalaire", "Polynome","Carré", "Losange", "Isocele", "Rectangle","Equilateral","Alterne interne", "Cercle","Aire","Perimètre", "Disque","Cone","Cube","Parallèle","Orthogonale", "Dodécaèdre","Icosaèdre","Tetraèdre","Fractale"]),['Info', 'Aire', 'Cone', 'Cube']),\
((2,["Cosinus","Sinus","Mathématiques", "Info", "Python", "Tests", "Angle", "Produit scalaire", "Polynome","Carré", "Losange", "Isocele", "Rectangle","Equilateral","Alterne interne", "Cercle","Aire","Perimètre", "Disque","Cone","Cube","Parallèle","Orthogonale", "Dodécaèdre","Icosaèdre","Tetraèdre","Fractale"]),[])\
]


#message d'aide si besoin
help="N'oublie pas d'utiliser print pour afficher le resultat"



def send_msg(channel, msg):
    print("TECHIO> message --channel \"{}\" \"{}\"".format(channel, msg))


def success():
    send_msg("Tests validés","Bravo !")
    print("TECHIO> success true")


def fail():
    print("TECHIO> success false")
    

def test():
    try:
      for inp,outp in input_output:
        sauvegarde_stdout=sys.stdout
        sys.stdout=io.StringIO()
        mon_programme(*inp)
        count1 = sys.stdout.getvalue()[:-1]
        sys.stdout=sauvegarde_stdout
        assert str(count1) == str(outp), "En testant les valeurs {} le résultat obtenu est {} au lieu de {}".format(str(inp),str(count1),str(outp))
        send_msg("Tests validés","En testant les valeurs {} le résultat obtenu est bien {}".format(str(inp),str(count1)))
      success()
    except AssertionError as e:
      fail()
      send_msg("Oops! ", e)
      if help:
        send_msg("Aide 💡", help)


if __name__ == "__main__": test()
