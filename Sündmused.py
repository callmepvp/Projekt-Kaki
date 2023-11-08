from Kuupäev import Kuupäev, Kellaaeg
from typing import List


#Panen siia praegu mingisuguse leet-code moodi asja, kuid enam-vähem see, mis sul mõttes oli.

class SündmusteNimekiri:
    
    def __init__(self, nimekiri):
        #Master sündmuste nimekiri
        self.nimekiri: List[Sündmus] = nimekiri

    def võtaSündmusedPäeval():
        pass

    def võtaSündmusedKuul():
        pass

    #def võtaSündmusedAastal():
        #pass (?)

    def võtaSündmusedPärastPäeva():
        pass

    def võtaSündmusedEnnePäeva():
        pass


    def võtaKestvusegaSündmus():
        pass

    def võtaNädalasedSündmused():
        pass

    def VõtaSündmustegaKuupäevad(self):
        kuupäevad = []
        for i in self.nimekiri:
            kp = i.VõtaKuupäev()
            if kp not in kuupäevad:
                kuupäevad.append(kp)

        return kuupäevad



# Sündmusel põhineb kõik selles programmis. See objekt peab olema piisavalt paindlik, et saada olla ühekordne Kuupäeva sündmus või olla igal kolmapäeval ja esmaspäeval kl 18 korduv sündmus või näiteks sündmus algusega kl 17 ja lõpuga kl 19.

# Kui objekti muutujal mingit väärtust ei ole, siis on selle väärtuseks None. Näiteks, kui pole alguskellaaega, ss on algusKella väärtus None.
class Sündmus:
    
    # Ürituse pealkiri on string ja kuupäev on Kuupäeva objekt.
    def __init__(self, nimi, kuupäev:Kuupäev):
        self.nimi = nimi

        self.algusKuupäev = kuupäev
        self.lõppKuupäev = Kuupäev(None, None, None)

        self.algusKell = Kellaaeg(None, None)
        self.lõppKell = Kellaaeg(None, None)



    def VõtaNimi(self):
        return self.nimi

    def VõtaKuupäev(self):
        return self.algusKuupäev.VõtaKuupäev()

    def MääraLõppKell(self, tund, minut):
        self.lõppKell = Kellaaeg(tund, minut)

