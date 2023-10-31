from Kuupäev import *


#Panen siia praegu mingisuguse leet-code moodi asja, kuid enam-vähem see, mis sul mõttes oli.

class SündmusteNimekiri:

    def __init__(self, nimekiri):
        self.nimekiri = nimekiri #Master sündmuste nimekiri (?)

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



# Sündmusel põhineb kõik selles programmis. See objekt peab olema piisavalt paindlik, et saada olla ühekordne Kuupäeva sündmus või olla igal kolmapäeval ja esmaspäeval kl 18 korduv sündmus või näiteks sündmus algusega kl 17 ja lõpuga kl 19.

# Kui objekti muutujal mingit väärtust ei ole, siis on selle väärtuseks None. Näiteks, kui pole alguskellaaega, ss on algusKella väärtus None.
class Sündmus:
    
    #Kuupäeva käsitletakse kolmese tuplina, kus on (p, k, a).
    def __init__(self, nimi, kuupäev):
        self.nimi = nimi

        self.algusKuupäev = Kuupäev(kuupäev[0], kuupäev[1], kuupäev[2])
        self.lõppKuupäev = Kuupäev(None, None, None)

        self.algusKell = Kellaaeg(None, None)
        self.lõppKell = Kellaaeg(None, None)



    def VõtaNimi(self):
        return self.nimi

    def VõtaKuupäev(self):
        return self.algusKuupäev.VõtaKuupäev()

    def MääraLõppKell(self, tund, minut):
        self.lõppKell = Kellaaeg(tund, minut)

