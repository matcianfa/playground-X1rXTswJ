#Ne pas oublier de changer le module à importer
from Cube_moins_carre import mon_programme
import sys
import io


#liste des couples input/output
input_output=[\
((0,10),[0, 0, 4, 18, 48, 100, 180, 294, 448, 648, 900]),\
((5,6),[100,180]),\
((1000,1100),[999000000, 1002001000, 1005008004, 1008021018, 1011040048, 1014065100, 1017096180, 1020133294, 1023176448, 1026225648, 1029280900, 1032342210, 1035409584, 1038483028, 1041562548, 1044648150, 1047739840, 1050837624, 1053941508, 1057051498, 1060167600, 1063289820, 1066418164, 1069552638, 1072693248, 1075840000, 1078992900, 1082151954, 1085317168, 1088488548, 1091666100, 1094849830, 1098039744, 1101235848, 1104438148, 1107646650, 1110861360, 1114082284, 1117309428, 1120542798, 1123782400, 1127028240, 1130280324, 1133538658, 1136803248, 1140074100, 1143351220, 1146634614, 1149924288, 1153220248, 1156522500, 1159831050, 1163145904, 1166467068, 1169794548, 1173128350, 1176468480, 1179814944, 1183167748, 1186526898, 1189892400, 1193264260, 1196642484, 1200027078, 1203418048, 1206815400, 1210219140, 1213629274, 1217045808, 1220468748, 1223898100, 1227333870, 1230776064, 1234224688, 1237679748, 1241141250, 1244609200, 1248083604, 1251564468, 1255051798, 1258545600, 1262045880, 1265552644, 1269065898, 1272585648, 1276111900, 1279644660, 1283183934, 1286729728, 1290282048, 1293840900, 1297406290, 1300978224, 1304556708, 1308141748, 1311733350, 1315331520, 1318936264, 1322547588, 1326165498, 1329790000])\
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
