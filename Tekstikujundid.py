import pygame
from Kujundid import *
from Tekst import *
from Sündmused import *
from math import floor, pi
from typing import List
from Programmiolek import ProgrammiOlek

# SündmuseRida
class SündmuseRida:
    # Oke, mu jaoks on see süntaks uus, aga pmst see on ainus viis pythonis märkida, et sisestatud parameeter peab olema mingi kindla klassi esindaja ja kui pole, ss ei tohiks joosta. Süntaks järgmine: parameeter: "klassiNimi". Klassinimi justkui oleks tekst, aga tegelt pole.
    def __init__(self, olek:"ProgrammiOlek", pind, sündmus: "Sündmus"):
        self.olek = olek
        self.sündmus = sündmus
        self.pind = pind
        self.asukoht = (0,0)
        self.laius = 100

    def Joonista(self):
        värv = self.olek.ruuduTekstiVärv

        # Täpp
        täpiAsukx, asuky = self.asukoht[0], self.asukoht[1]
        raadius = self.olek.sündmuseReaTäpiRaadius
        pygame.draw.circle(self.pind, värv, (täpiAsukx, asuky), raadius)

        # Kellaaeg
        kellaLaius = 0
        kellaFont = self.olek.sündmuseReaAjaFont
        if self.sündmus.lõppKell.KasOnKell() == True:
            kellaTekst = self.sündmus.lõppKell.VõtaStringina()
            kellaLaius = kellaFont.size(kellaTekst)[0]
            kellaAsukx = täpiAsukx + self.laius - kellaLaius
            kell = Tekst(self.pind, kellaTekst, kellaFont, värv, (kellaAsukx, asuky))
            kell.Joonista()
        
        # Pealkiri
        täpivahe = self.olek.sündmuseReaTäpiVahe
        pealkAsukx = täpiAsukx + täpivahe
        pealkRuum = self.laius - täpivahe - kellaLaius
        pealkTekst = self.sündmus.VõtaNimi()
        pealkFont = self.olek.sündmuseReaKirjaFont
        pealkTekst = EraldaSobivaPikkusegaTekst(pealkTekst, pealkRuum, pealkFont)[0]
        pealk = Tekst(self.pind, pealkTekst, pealkFont, värv, (pealkAsukx, asuky))
        pealk.Joonista()
            


    def MääraLaius(self, laius):
        self.laius = laius

    def MääraAsukoht(self, asukoht):
        self.asukoht = asukoht

    def VõtaSuurus(self):
        suurus = self.olek.sündmuseReaKirjaFont.size(self.sündmus.VõtaNimi())
        return suurus





# PäevaPealkiri
class PäevaPealkiri:
    def __init__(self, olek:"ProgrammiOlek", pind, kuupäev:"Kuupäev"):
        self.kpFont = olek.päevaruuduPealkKpPygFont
        self.aFont = olek.päevaruuduPealkAastaPygFont
        self.kuupäev = kuupäev
        self.asukoht = (0,0)
        self.pind = pind
        self.värv = olek.ruuduTekstiVärv
        self.päevaAastaVahe = olek.päevaruuduPealkPäevaAastaVahe

    def MääraAsukoht(self, x, y):
        self.asukoht = (x,y)

    def Joonista(self):
        pk = self.kuupäev.VõtaPäevKuuTekstina()
        a = self.kuupäev.VõtaAastaTekstina()

        päevKuuTekst = Tekst(self.pind, pk, self.kpFont, self.värv, self.asukoht)
        päevKuuTekst.Joonista()
        
        aAsuk = (self.asukoht[0] + self.kpFont.size(pk)[0] + 10, self.asukoht[1])
        aastaTekst = Tekst(self.pind, a, self.aFont, self.värv,aAsuk)
        aastaTekst.Joonista()

    def VõtaLaius(self):
        pk = self.kuupäev.VõtaPäevKuuTekstina()
        a = self.kuupäev.VõtaAastaTekstina()

        laius = self.kpFont.size(pk)[0] + self.päevaAastaVahe + self.aFont.size(a)[0]
        return laius



# PäevaRuut
class PäevaRuut:
    def __init__(self, olek:"ProgrammiOlek", pind, sündmused:"List[Sündmus]"):
        self.kuupäev = sündmused[0].algusKuupäev
        self.suurus = (10,10)
        self.asuk = (10,10)
        self.pealkiri = PäevaPealkiri(olek, pind, self.kuupäev)
        self.olek = olek
        self.taust = Ristkülik(pind, self.asuk, self.suurus)
        self.taust.MääraVärv(olek.päevaruuduVärv)
        self.pind = pind
        self.sündmused = sündmused
        
    def MääraAsukoht(self, x, y):
        self.asuk = (x,y)

    def MääraSuurus(self, x, y):
        self.suurus = (x,y)

    def Joonista(self):
        self.taust.MääraAsukoht(self.asuk[0], self.asuk[1])
        self.taust.MääraSuurus(self.suurus[0], self.suurus[1])
        self.taust.Joonista()

        pealkAsukx = self.asuk[0] + self.olek.päevaruuduPealkKaugusVasakult
        pealkAsuky = self.asuk[1] + self.olek.päevaruuduPealkKaugusÜlaservast
        self.pealkiri.MääraAsukoht(pealkAsukx, pealkAsuky)
        self.pealkiri.Joonista()

        counter = 0
        for i in self.sündmused:
            # Sündmuserea asukx
            vasakult = self.olek.sündmuseRidaVasakult
            asukx = self.asuk[0] + vasakult
            pealkirjast = self.olek.sündmuseReadKuupäevast
            asuky = pealkAsuky + pealkirjast

            
            asuky = pealkAsuky + 40
            uusRida = SündmuseRida(self.olek, self.pind, i)
            reaVahe = self.olek.sündmuseRidadeVahe
            uusRida.MääraAsukoht((asukx, asuky+counter*reaVahe))
            laius = self.suurus[0] - self.olek.sündmuseRidaVasakult - self.olek.sündmuseRidaParemalt
            uusRida.MääraLaius(laius)
            uusRida.Joonista()
            counter += 1
        






        





class PäevaRuudustik:
    def __init__(self, pind, kujuRistkülik:"Ristkülik", minLaius, kõrgus, vahesuurus, äärevahe, ruutudeArv):
        self.minLaius = minLaius
        self.kõrgus = kõrgus
        self.vahe = vahesuurus
        self.ruudud: List[Ristkülik] = []
        self.taust = kujuRistkülik
        for i in range(ruutudeArv):
            uusRuut = Ristkülik(pind, (0,0),(0,0))
            self.ruudud.append(uusRuut)
        self.äärevahe = äärevahe
        self.ridadeArv = 0


    def Paiguta(self):
        taustaLaius = self.taust.VõtaSuurus()[0]
        mituReas = floor(taustaLaius/self.minLaius)
        if mituReas == 0: mituReas = 1
        vahesidKokku = 2*self.äärevahe + (mituReas-1)*self.vahe
        ruudulaius = (taustaLaius - vahesidKokku)/mituReas

        counter = 0
        vasakServ = self.taust.VõtaAsukoht()[0]
        ülemServ = self.taust.VõtaAsukoht()[1]
        for i in self.ruudud:

            
            mitmesTulp = counter % mituReas
            mitmesRida = floor(counter/mituReas)
            ridadeArv = mitmesRida


            asukx = vasakServ + self.äärevahe + mitmesTulp*(ruudulaius + self.vahe)
            asuky = ülemServ + self.äärevahe + mitmesRida*(self.minLaius + self.vahe)

            i.MääraAsukoht(asukx, asuky)
            i.MääraSuurus(ruudulaius, self.minLaius)

            counter += 1


    # Seda meetodit kutsuda ainult pärast seda, kui on kasutatud Paiguta meetodit, sest see tagab, et self.ridadeArv omab õiget väärtust. Väljastab kauguse ülemise ruudu ülemisest servast alumise ruudu alumise servani. Vajalik selleks, et väljaspool klassi saaks taustaks olev kujund enda suuruse õigeks panna.
    def VõtaRuutudeKõrgus(self):
        kõrgus = self.ridadeArv * kõrgus + (self.ridadeArv-1) * self.vahesuurus
        return kõrgus


    def Joonista(self):
        for i in self.ruudud:
            i.Joonista()