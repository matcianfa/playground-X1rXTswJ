#Ne pas oublier de changer le module à importer
from Palindrome import mon_programme
import sys
import io


#liste des couples input/output
input_output=[\
("lol","PALINDROME",""),\
("mathématiques","PAS PALINDROME",""),\
("selles","PALINDROME",""),\
("cosinus","PAS PALINDROME",""),\
("Laval","PALINDROME","Attention aux majuscules !"),\
("rions noir","PALINDROME","Attention aux espaces !"),\
("La la La","PAS PALINDROME","")\
]

input_output2=[\
("Eh ! ca va la vache ?","PALINDROME", "Attention à la ponctuation !"),\
("Tu l'as trop écrasé César ce Port-Salut","PALINDROME", "Attention aux accents !"),\
("azer tyé_-(-7ào n4öô cb 1? nv ,sgfgq?!","PAS PALINDROME", "Si vous trouvez que ceci est un palindrome, c'est que vore programme a vraiment un probleme !"),\
("Trace l'inégal palindrome. Neige. Bagatelle, dira Hercule. Le brut repentir, cet écrit né Perec. L'arc lu pèse trop, lis à vice-versa. Perte. Cerise d'une vérité banale, le Malstrom, Alep, mort édulcoré, crêpe porté de ce désir brisé d'un iota. Livre si aboli, tes sacres ont éreinté, cor cruel, nos albatros. Être las, autel bâti, miette vice-versa du jeu que fit, nacré, médical, le sélénite relaps, ellipsoïdal. Ivre il bat, la turbine bat, l'isolé me ravale : le verre si obéi du Pernod -- eh, port su ! -- obsédante sonate teintée d'ivresse. Ce rêve se mit -- peste ! -- à blaguer. Beh ! L'art sec n'a si peu qu'algèbre s'élabore de l'or évalué. Idiome étiré, hésite, bâtard replié, l'os nu. Si, à la gêne secrète verbe nul à l'instar de cinq occis--, rets amincis, drailles inégales, il, avatar espacé, caresse ce noir Belzebuth, ô il offensé, tire ! L'écho fit (à désert) : Salut, sang, robe et été.Fièvres. Adam, rauque; il écrit : Abrupt ogre, eh, cercueil, l'avenir tu, effilé, génial à la rue (murmure sud eu ne tire vaseline séparée; l'épeire gelée rode : Hep, mortel ?) lia ta balafre native. Litige. Regagner (et ne m'…). Ressac. Il frémit, se sape, na ! Eh, cavale! Timide, il nia ce sursaut. Hasard repu, tel, le magicien à morte me lit. Un ignare le rapsode, lacs ému, mixa, mêla : Hep, Oceano Nox, ô, béchamel azur ! Éjaculer ! Topaze ! Le cèdre, malabar faible, Arsinoë le macule, mante ivre, glauque, pis, l'air atone (sic). Art sournois : si, médicinale, l'autre glace (Melba ?) l'un ? N'alertai ni pollen (retêter : gercé, repu, denté…) ni tobacco. Tu, désir, brio rimé, eh, prolixe nécrophore, tu ferres l'avenir velu, ocre, cromant-né ? Rage, l'ara. Veuglaire. Sedan, tes elzévirs t'obsèdent. Romain ? Exact. Et Nemrod selle ses Samson ! Et nier téocalli ? Cave canem (car ce nu trop minois -- rembuscade d'éruptives à babil -- admonesta, fil accru, Têtebleu ! qu'Ariane évitât net. Attention, ébénier factice, ressorti du réel. Ci-gît. Alpaga, gnôme, le héros se lamente, trompé, chocolat : ce laid totem, ord, nil aplati, rituel biscornu; ce sacré bédeau (quel bât ce Jésus!). Palace piégé, Torpédo drue si à fellah tôt ne peut ni le Big à ruer bezef. L'eugéniste en rut consuma d'art son épi d'éolienne ici rot (eh… rut ?). Toi, d'idem gin, élèvera, élu, bifocal, l'ithos et notre pathos à la hauteur de sec salamalec ? Élucider. Ion éclaté : Elle ? Tenu. Etna but (item mal famé), degré vide, julep : macédoine d'axiomes, sac semé d'École, véniel, ah, le verbe enivré (ne sucer ni arrêter, eh ça jamais !) lu n'abolira le hasard ? Nu, ottoman à écho, l'art su, oh, tara zéro, belle Deborah, ô, sacre ! Pute, vertubleu, qualité si vertu à la part tarifé (décalitres ?) et nul n'a lu trop s'il séria de ce basilic Iseut. Il a prié bonzes, Samaritain, Tora, vilains monstres (idolâtre DNA en sus) rêvés, évaporés : Arbalète (bètes) en noce du Tell ivre-mort, émeri tu : O, trapu à elfe, il lie l'os, il lia jérémiade lucide. Petard! Rate ta reinette, bigleur cruel, non à ce lot ! Si, farcis-toi dito le coeur ! Lied à monstre velu, ange ni bête, sec à pseudo délire : Tsarine (sellée, là), Cid, Arétin, abruti de Ninive, Déjanire.. Le Phenix, eve de sables, écarté, ne peut égarer racines radiales en mana : l'Oubli, fétiche en argile. Foudre. Prix : Ile de la Gorgone en roc, et, ô, Licorne écartelée, Sirène, rumb à bannir à ma (Red n'osa) niére de mimosa : Paysage d'Ourcq ocre sous ive d'écale; Volcan. Roc : tarot célé du Père. Livres. Silène bavard, replié sur sa nullité (nu à je) belge : ipséité banale. L' (eh, ça !) hydromel à ri, psaltérion. Errée Lorelei… Fi ! Marmelade déviré d'Aladine. D'or, Noël : crèche (l'an ici taverne gelée dès bol…) à santon givré, fi !, culé de l'âne vairon. Lapalisse élu, gnoses sans orgueil (écru, sale, sec). Saluts : angiome. T'es si crâneur ! Rue. Narcisse ! Témoignas-tu ! l'ascèse, là, sur ce lieu gros, nasses ongulées… S'il a pal, noria vénale de Lucifer, vignot nasal (obsédée, le genre vaticinal), eh, Cercle, on rode, nid à la dérive, Dédale (M.. !) ramifié ? Le rôle erre, noir, et la spirale mord, y hache l'élan abêti : Espiègle (béjaune) Till : un as rusé. Il perdra. Va bene.Lis, servile repu d'électorat, cornac, Lovelace. De visu, oser ? Coq cru, ô, Degas, y'a pas, ô mime, de rein à sonder : à marin nabab, murène risée. Le trace en roc, ilote cornéen.O, grog, ale d'elixir perdu, ô, feligrane! Eh, cité, fil bu ! ô ! l'anamnèse, lai d'arsenic, arrérage tué, pénétra ce sel-base de Vexin. Eh, pèlerin à (Je : devin inédit) urbanité radicale (elle s'en ira…), stérile, dodu. Espaces (été biné ? gnaule ?) verts. Nomade, il rue, ocelot. Idiot-sic rafistolé : canon ! Leur cruel gibet te niera, têtard raté, pédicule d'aimé rejailli. Soleil lie, fléau, partout ire (Métro, Mer, Ville…) tu déconnes. Été : bètel à brasero. Pavese versus Neandertal ! O, diserts noms ni à Livarot ni à Tir ! Amassez. N'obéir. Pali, tu es ici : lis abécédaires, lis portulan : l'un te sert-il ? à ce défi rattrapa l'autre ? Vise-t-il auquel but rêvé tu perças ? Oh, arobe d'ellébore, Zarathoustra! L'ohcéan à mot (Toundra ? Sahel ?) à ri : Lob à nul si à ma jachère, terrain récusé, nervi, née brève l'haleine véloce de mes casse-moix à (Déni, ô !) décampé. Lu, je diverge de ma flamme titubante : une telle (étal, ce noir édicule cela mal) ascèse drue tua, ha, l'As.Oh, taper ! Tontes ! Oh, tillac, ô, fibule à rêve l'Énigme (d'idiot tu) rhétoricienne. Il, Oedipe, Nostradamus nocturne et, si né Guelfe, zébreur à Gibelin tué (pentothal ?), le faiseur d'ode protège. Ipéca… : lapsus. Eject à bleu qu'aède berça sec. Un roc si bleu ! Tir. ital. : palindrome tôt dialectal. Oc ? Oh, cep mort et né, mal essoré, hélé. Mon gag aplati gicle. Érudit rosse-récit, ça freine, benoit, net. Ta tentative en air auquel bète, turc, califat se (nom d'Ali-Baba !) sévit, pure de -- d'ac ? -- submersion importune, crac, menace, vacilla, co-étreinte… Nos masses, elles dorment ? Etc… Axé ni à mort-né des bots. Rivez ! Les Etna de Serial-Guevara l'égarent. N'amorcer coulevrine. Valser. Refuter. Oh, porc en exil (Orphée), miroir brisé du toc cabotin et né du Perec : Regret éternel. L'opiniâtre. L'annulable. Mec, Alger tua l'élan ici démission. Ru ostracisé, notarial, si peu qu'Alger, Viet-Nam (élu caméléon !), Israël, Biafra, bal à merde : celez, apôtre Luc à Jéruzalem, ah ce boxon! On à écopé, ha, le maximum ! Escale d'os, pare le rang inutile. Métromane ici gamelle, tu perdras. Ah, tu as rusé! Cain! Lied imité la vache (à ne pas estimer) (flic assermenté, rengagé) régit.Il évita, nerf à la bataille trompé. Hé, dorée, l'Égérie pelée rape, sénile, sa vérité nue du sérum : rumeur à la laine, gel, if, feutrine, val, lieu-créche, ergot, pur, Bâtir ce lieu qu'Armada serve : if étété, éborgnas-tu l'astre sédatif ? Oh, célérités ! Nef ! Foli ! Oh, tubez ! Le brio ne cessera, ce cap sera ta valise; l'âge : ni sel-liard (sic) ni master-(sic)-coq, ni cédrats, ni la lune brève. Tercé, sénégalais, un soleil perdra ta bétise héritée (Moi-Dieu, la vérole!) Déroba le serbe glauque, pis, ancestral, hébreu (Galba et Septime-Sévère). Cesser, vidé et nié. Tetanos. Etna dès boustrophédon répudié. Boiser. Révèle l'avare mélo, s'il t'a béni, brutal tablier vil. Adios. Pilles, pale rétine, le sel, l'acide mercanti. Feu que Judas rêve, civette imitable, tu as alerté, sort à blason, leur croc. Et nier et n'oser. Casse-t-il, ô, baiser vil ? à toi, nu désir brisé, décédé, trope percé, roc lu. Détrompe la. Morts : l'Ame, l'Élan abêti, revenu. Désire ce trépas rêvé : Ci va ! S'il porte, sépulcral, ce repentir, cet écrit ne perturbe le lucre : Haridelle, ta gabegie ne mord ni la plage ni l'écart.","PALINDROME", "")\
]


#message d'aide si besoin
#help="Attention aux majuscules, espaces, ponctuations et accents, ils ne doivent pas être pris en compte."



def send_msg(channel, msg):
    print("TECHIO> message --channel \"{}\" \"{}\"".format(channel, msg))


def success():
    send_msg("Tests validés","Bravo !")
    print("TECHIO> success true")


def fail():
    print("TECHIO> success false")
    

def test():
    succes=False
    try:
      for inp,outp,h in input_output:
        sauvegarde_stdout=sys.stdout
        sys.stdout=io.StringIO()
        mon_programme(inp)
        count1 = sys.stdout.getvalue()[:-1]
        sys.stdout=sauvegarde_stdout
        assert str(count1) == str(outp), "En testant les valeurs {} le résultat obtenu est {} au lieu de {}".format(str(inp),str(count1),str(outp))
        send_msg("Tests validés","En testant les valeurs {} le résultat obtenu est bien {}".format(str(inp),str(count1)))
      succes=True
      for inp,outp,h in input_output2:
        sauvegarde_stdout=sys.stdout
        sys.stdout=io.StringIO()
        mon_programme(inp)
        count1 = sys.stdout.getvalue()[:-1]
        sys.stdout=sauvegarde_stdout
        assert str(count1) == str(outp), "En testant les valeurs {} le résultat obtenu est {} au lieu de {}".format(str(inp),str(count1),str(outp))
        send_msg("Tests validés","En testant les valeurs {} le résultat obtenu est bien {}".format(str(inp),str(count1)))
      send_msg("Tests validés","Ce dernier test était un palindrome de 1247 mots !")
      success()
    except AssertionError as e:
      if succes:
        send_msg("Oops! ", "C'est un bon début mais tu peux encore améliorer ton programme !")
        success()
      else :
        fail()
        send_msg("Oops! ", e)
      if help:
        send_msg("Aide 💡", h)


if __name__ == "__main__": test()
