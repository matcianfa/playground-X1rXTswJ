#Ne pas oublier de changer le module à importer
from Codage_cesar import mon_programme
import sys
import io


#liste des couples input/output
input_output=[\
((2, "MATHS"),"OCVJU"),\
((-2, "OCVJU"),"MATHS"),\
((3, "ZERO"),"CHUR"),\
((24,"GAZ"),"EYX"),\
((3,"VENEZ VITE"),"YHQHC YLWH"),\
((18,"WXMZIBQWV KWZVML-JMMN !"),"OPERATION CORNED-BEEF !"),\
((18,"YCM R’IQUM I NIQZM KWVVIQBZM KM VWUJZM CBQTM ICF AIOMA ! QUUWZBMT IZKPQUMLM, IZBQABM, QVOMVQMCZ, YCQ LM BWV RCOMUMVB XMCB XZQAMZ TI DITMCZ ? XWCZ UWQ BWV XZWJTMUM MCB LM XIZMQTA IDIVBIOMA. RILQA, UGABMZQMCF, CV XZWJTMUM JTWYCIQB BWCB T’ILUQZIJTM XZWKMLM, T’ŒCDZM OZIVLQWAM YCM XGBPIOWZM LÉKWCDZQB ICF IVKQMVA OZMKA. W YCILZIBCZM ! DQMCF BWCZUMVB LC XPQTWAWXPM QVAWTCJTM ZWVLMCZ, BZWX TWVOBMUXA DWCA IDMH LMNQM XGBPIOWZM MB AMA QUQBIBMCZA. KWUUMVB QVBMOZMZ T’MAXIKM XTIV KQZKCTIQZM ? NWZUMZ CV BZQIVOTM ICYCMT QT ÉYCQDICLZI ? VWCDMTTM QVDMVBQWV : IZKPQUMLM QVAKZQZI LMLIVA CV PMFIOWVM ; IXXZMKQMZI AWV IQZM NWVKBQWV LC ZIGWV. XIA BZWX VM A’G BQMVLZI : LMLWCJTMZI KPIYCM MTMUMVB IVBMZQMCZ ; BWCRWCZA LM T’WZJM KITKCTMM IXXZWKPMZI ; LMNQVQZI TQUQBM ; MVNQV, T’IZK, TM TQUQBMCZ LM KMB QVYCQMBIVB KMZKTM, MVVMUQ BZWX ZMJMTTM XZWNMAAMCZ, MVAMQOVMH AWV XZWJTMUM IDMK HMTM"),"QUE J’AIME A FAIRE CONNAITRE CE NOMBRE UTILE AUX SAGES ! IMMORTEL ARCHIMEDE, ARTISTE, INGENIEUR, QUI DE TON JUGEMENT PEUT PRISER LA VALEUR ? POUR MOI TON PROBLEME EUT DE PAREILS AVANTAGES. JADIS, MYSTERIEUX, UN PROBLEME BLOQUAIT TOUT L’ADMIRABLE PROCEDE, L’ŒUVRE GRANDIOSE QUE PYTHAGORE DÉCOUVRIT AUX ANCIENS GRECS. O QUADRATURE ! VIEUX TOURMENT DU PHILOSOPHE INSOLUBLE RONDEUR, TROP LONGTEMPS VOUS AVEZ DEFIE PYTHAGORE ET SES IMITATEURS. COMMENT INTEGRER L’ESPACE PLAN CIRCULAIRE ? FORMER UN TRIANGLE AUQUEL IL ÉQUIVAUDRA ? NOUVELLE INVENTION : ARCHIMEDE INSCRIRA DEDANS UN HEXAGONE ; APPRECIERA SON AIRE FONCTION DU RAYON. PAS TROP NE S’Y TIENDRA : DEDOUBLERA CHAQUE ELEMENT ANTERIEUR ; TOUJOURS DE L’ORBE CALCULEE APPROCHERA ; DEFINIRA LIMITE ; ENFIN, L’ARC, LE LIMITEUR DE CET INQUIETANT CERCLE, ENNEMI TROP REBELLE PROFESSEUR, ENSEIGNEZ SON PROBLEME AVEC ZELE")\
]


#message d'aide si besoin
help=""



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
