from Prise_en_main_Exo_1 import mon_programme

#liste des couples input/output
input_output=[\
((3,4),7),\
((0,0),0),\
((-1,4),3),\
((2.4,-3.1),-0.7)\
]


#message d'aide si besoin
help="N'oublie pas d'afficher avec print"



def send_msg(channel, msg):
    print("TECHIO> message --channel \"{}\" \"{}\"".format(channel, msg))


def success():
    print("TECHIO> success true")


def fail():
    print("TECHIO> success false")
    

def test():
    try:
      for inp,outp in input_output:
        count1 = mon_programme(*inp)
        assert count1 == outp, "En testant les valeurs {} le résultat obtenu est {} au lieu de {}".format(str(inp),str(count1),str(outp))
      success()
    except AssertionError as e:
      fail()
      send_msg("Oops! ", e)
      if help:
        send_msg("Aide 💡", help)


if __name__ == "__main__":
	test()
