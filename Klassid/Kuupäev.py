# Selle klassi mõte on hoida endas kuupäeva ning väljastada kuupäeva kohta käivat vajalikku infot nt mis nädalapäev vastab sellele kuupäevale, kas aasta on liigaasta, kas kuu, päeva ja aasta numbrid üldse vastavad päris kuupäevale jms.

# Kuupäeva objekt võib vabalt hoida endas selliseid numbreid, mis tegelikult kuupevaks ei kõlba, aga samas omab funktsionaalsust kontrollimaks, kas numbrid on võimalikud v mitte. Selle meetodi tagastuse True v False põhjal väljaspool objekti tegeleda vajaduse korral uue sisestuse võtmisega ja seejärel objekti meetoditega väärtuse muutmisega. Point on, et see klass ei tegele inputi võtmisega.
import math

class Kuupäev:
    def __init__(self, päev, kuu, aasta):
        self.kuu = kuu
        self.päev = päev
        self.aasta = aasta

    # Tagastab True v false vastavalt sellele, kas on liigaasta v mitte.
    def KasLiigaasta(self):
        if self.aasta % 4 == 0:
            if self.aasta % 100 == 0:
                if self.aasta % 400 == 0:
                    return True
                return False
            return True
        return False


    # Kontrollib, kas päeva, kuu ja aasta numbrid on sellised, et need vastaksid ka mõnele päris maailma kuupäevale. True, kui jah, False, kui ei vasta.
    def KasVõimalik(self):
        kuudePikkused = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        if self.aasta < 1800:
            return False
        if self.kuu < 1 or self.kuu > 12:
            return False
        if self.päev < 1:
            return False
        if self.kuu == 2 and self.KasLiigaasta() and self.päev > 29:
            return False
        if self.päev > kuudePikkused[self.kuu]:
            return False
        return True
        

    def VõtaKuupäevTuplina(self):
        return (self.päev, self.kuu, self.aasta)


    # See on crazy meetod. Väljastab numbri 1-7 vastavalt esmaspäevast pühapäevani
    def VõtaNädalaPäev(self):
        y = self.aasta
        m = self.kuu
        d = self.päev
        t = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
        if m < 3:
            y -= 1
        return math.floor((y + y/4 - y/100 + y/400 + t[m-1] + d-1) % 7)+1


    # Kasutada pigem seda funktsiooni selle asemel, et ükshaaval muutujaid nüsida.
    def MuudaKuupäeva(self, päev, kuu, aasta):
        if päev != None:
            self.päev = päev
        if kuu != None:
            self.kuu = kuu
        if aasta != None:
            self.aasta = aasta


    # Neid funktsioone kasutab päevaruudus Päevapealkirja objekt, mille ülesanne on paigutada õigesti päevaruudu ülaserva selle päeva kuupäev.
    def VõtaPäevKuuTekstina(self):
        return str(self.päev) + "." + str(self.kuu)

    def VõtaAastaTekstina(self):
        return str(self.aasta)


    # Tagastab True, kui käesolev kuupäev on rangelt enne parameetriks antud kuupäeva ja false siis, kui on võrdne antud kuupäevaga v hiljem.
    def KasOnEnne(self, kuupäev: "Kuupäev"):
        # Kontrollib aastat.
        if self.Aasta < kuupäev.aasta:
            return True
        if self.Aasta > kuupäev.aasta:
            return False

        # Kui sai aastakontrollist
        # 
        #  mööda, tähendab, et aastad on võrdsed. Hakkab kontrollima kuid.
        if self.Kuu < kuupäev.kuu:
            return True
        if self.kuu > kuupäev.kuu:
            return False

        # Kui kood jõuab siiani, on kuud ka võrdsed. Kontrollib päevi. Ja tagastab false, kui käesolev päev on pärast antud päeva v samal päeval.
        if self.päev < kuupäev.päev:
            return True
        else:
            return False


    def KasOnSama(self, kuupäev:"Kuupäev"):
        if self.aasta == kuupäev.aasta and \
           self.kuu   == kuupäev.kuu   and \
           self.päev  == kuupäev.päev: return True
        return False


class Kellaaeg:
    def __init__(self, tund=None, minut=None):
        self.tund = tund
        self.minut = minut

    def KasOnKell(self):
        if self.tund == None or self.minut == None:
            return False
        return True

    def VõtaStringina(self):
        minutitekst = str(self.minut)
        if self.minut < 10:
            minutitekst = "0" + minutitekst
        return(str(self.tund) + "." + minutitekst)

