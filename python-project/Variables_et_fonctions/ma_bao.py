import sys



def tester(txt,glb=globals()):
    '''
    Permet de tester si le module n'a pas d'erreur de syntaxe ou d'indentation pour pouvoir les rattraper.
    '''
    nom_fichier=""
    if txt[:5]=="from " or txt[:7]=="import ":
        nom_fichier=txt.split()[1]+".py"
    try :
        return exec(txt,glb)
    except IndentationError as e:
        print("Attention il y a un problème d'indentation dans votre code à la ligne "+str(e.args[1][1]),file=sys.stderr)
        print("Vérifiez bien que vous avez correctement décalé votre code",file=sys.stderr)
        print("Après un if, else, elif, for, while ou la création d'une fonction, il faut ajouter un décalage.",file=sys.stderr)
        print('TECHIO> annotate --file '+ nom_fichier +' --position '+str(e.args[1][1])+' Erreur d\'indentation') 
        print("TECHIO> success false")
        sys.exit()
    except SyntaxError as e:
        print("Attention , il y a un problème de syntaxe dans votre code à la ligne "+str(e.args[1][1]),file=sys.stderr)
        print("Vérifiez que vous n'avez pas oublié des deux points ':' en fin de ligne par exemple.",file=sys.stderr)
        print("Cela peut provenir d'une parenthèse mal fermée ou une virgule mal placée.",file=sys.stderr)
        print('TECHIO> annotate --file '+ nom_fichier +' --position '+str(e.args[1][1])+' Erreur de syntaxe') 
        print("TECHIO> success false")
        sys.exit()
    except NameError as e:
        print("Attention , vous utilisez le nom '"+str(e.args[0].split("'")[1])+"' alors qu'il n'est pas défini",file=sys.stderr)
        print("En général, c'est soit une erreur de frappe soit que vous n'avez pas créé votre variable ou fonction avant de l'utiliser.",file=sys.stderr)
        print("TECHIO> success false")
        sys.exit()

#Afficher la correction
def afficher_correction(module):
    """
    Affiche la correction si elle existe
    """
    try:
        with open(module+"_Correction.py", "r") as correction :
            ligne="Voici un ou des exemples de corrections possibles"
            send_msg("Exemple(s) de correction", ligne)
            ligne="-------------------------------------------------"
            send_msg("Exemple(s) de correction", ligne)
            lignes=correction.read().split("\n")
            for ligne in lignes:
                send_msg("Exemple(s) de correction", ligne)
    except:
        pass

def cheat(module):
    """
    Permet d'afficher la correction avec le mot de passe
    """
    try:
        if str(mdp)=="0112358":
            afficher_correction(module)
    except:
        pass

    
    
