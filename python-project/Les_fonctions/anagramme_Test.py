#Ne pas oublier de changer le module à importer
from anagramme import anagramme as f
import sys
import io


#liste des couples input/output
input_output=[\
("bac",['abc', 'acb', 'bac', 'bca', 'cab', 'cba']),\
("maths",['ahmst', 'ahmts', 'ahsmt', 'ahstm', 'ahtms', 'ahtsm', 'amhst', 'amhts', 'amsht', 'amsth', 'amths', 'amtsh', 'ashmt', 'ashtm', 'asmht', 'asmth', 'asthm', 'astmh', 'athms', 'athsm', 'atmhs', 'atmsh', 'atshm', 'atsmh', 'hamst', 'hamts', 'hasmt', 'hastm', 'hatms', 'hatsm', 'hmast', 'hmats', 'hmsat', 'hmsta', 'hmtas', 'hmtsa', 'hsamt', 'hsatm', 'hsmat', 'hsmta', 'hstam', 'hstma', 'htams', 'htasm', 'htmas', 'htmsa', 'htsam', 'htsma', 'mahst', 'mahts', 'masht', 'masth', 'maths', 'matsh', 'mhast', 'mhats', 'mhsat', 'mhsta', 'mhtas', 'mhtsa', 'msaht', 'msath', 'mshat', 'mshta', 'mstah', 'mstha', 'mtahs', 'mtash', 'mthas', 'mthsa', 'mtsah', 'mtsha', 'sahmt', 'sahtm', 'samht', 'samth', 'sathm', 'satmh', 'shamt', 'shatm', 'shmat', 'shmta', 'shtam', 'shtma', 'smaht', 'smath', 'smhat', 'smhta', 'smtah', 'smtha', 'stahm', 'stamh', 'stham', 'sthma', 'stmah', 'stmha', 'tahms', 'tahsm', 'tamhs', 'tamsh', 'tashm', 'tasmh', 'thams', 'thasm', 'thmas', 'thmsa', 'thsam', 'thsma', 'tmahs', 'tmash', 'tmhas', 'tmhsa', 'tmsah', 'tmsha', 'tsahm', 'tsamh', 'tsham', 'tshma', 'tsmah', 'tsmha']),\
("a",["a"])\
]



#message d'aide si besoin
help="N'oublie pas d'utiliser return pour afficher le resultat"



def send_msg(channel, msg):
    print("TECHIO> message --channel \"{}\" \"{}\"".format(channel, msg))


def success():
    send_msg("Tests validés","Bravo !")
    print("TECHIO> success true")


def fail():
    print("TECHIO> success false")
    

def test():
    try:
      for x,reponse in input_output:
        assert sorted(f(x)) == sorted(reponse), "En testant les valeurs {} le résultat obtenu est {} au lieu de {}".format(str(x),str(f(x)),str(reponse))
        send_msg("Tests validés","En testant les valeurs {} le résultat obtenu est bien {}".format(str(x),str(f(x))))
      success()
    except AssertionError as e:
      fail()
      send_msg("Oops! ", e)
      if help:
        send_msg("Aide 💡", help)


if __name__ == "__main__": test()
