from typing import List
from Sündmus import Sündmus
from Kuupäev import Kuupäev
from Päev import Päev


def VõtaKindlalKuupäeval(nimekiri:"List[Sündmus]", kuupäev:"Kuupäev"):
	sobivad = []
	for i in nimekiri:
		if i.KasOnPäeval(Kuupäev) == True:
			sobivad.append(i)
	return sobivad


# Selle funktsiooni mõte on tagastada kõikidest päevadest, mis on hiljem kui algus, ainult indel kogus, mitte kõik.
def VõtaMituPäevaAlates(nimekiri:"List[Sündmus]", algus, kogus):
	pass



# Funktsiooni mõte on võtta nimekiri päevadest ja üks kuupäev. KOntrollib kaks saadud kuupäev on mõnel nimekirjas olevatest päevadest. Kui on returnib selle päeva indeksi nimekirjas. Kui pole, returnib -1.
def KasOnKuupäevagaPäeva(päevad: List[Päev], kuupäev: Kuupäev):
	counter = 0
	for i in päevad:
		if i.kuupäev.KasOnSama(kuupäev):
			return counter
		counter += 1
	return -1




# Tagastab ainult need päevad, mis on mõne sündmuse alguspäevaks. Ainult need sündmused on vastava päeva nimekirjas, millel on algus sellel samal kuupäeval.
def VõtaKõikAlgusPäevad(nimekiri: "List[Sündmus]"):
	päevad: List[Päev] = []
	
	for sündmus in nimekiri:
		index = KasOnKuupäevagaPäeva(päevad, sündmus.alguskuupäev)
		if index == -1:
			uusPäev = Päev(sündmus.alguskuupäev, [sündmus])
			päevad.append(uusPäev)
		else:
			päevad[index].sündmusteNimekiri.append(sündmus)

	return päevad