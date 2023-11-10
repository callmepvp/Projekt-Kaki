import pygame
from Kujundid import Ristkülik
from Tekst import Tekst, EraldaSobivaPikkusegaTekst
from Sündmus import Sündmus
from math import floor
from typing import List
from Programmiolek import ProgrammiOlek
from Kuupäev import Kuupäev
from Päev import Päev
from SündNimekFunktsioonid import *

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
        
        # Pealkiri
        täpivahe = self.olek.sündmuseReaTäpiVahe
        pealkAsukx = täpiAsukx + täpivahe
        pealkRuum = self.laius - täpivahe
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
    def __init__(self, olek:"ProgrammiOlek", pind, päev:"Päev"):
        self.kuupäev = päev.kuupäev
        self.suurus = (10,10)
        self.asuk = (10,10)
        self.pealkiri = PäevaPealkiri(olek, pind, self.kuupäev)
        self.olek = olek
        self.taust = Ristkülik(pind, self.asuk, self.suurus)
        self.taust.MääraVärv(olek.päevaruuduVärv)
        self.pind = pind
        self.sündmused = päev.sündmusteNimekiri
        
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
            laius = self.suurus[0] - self.olek.sündmuseRidaVasakult# - self.olek.sündmuseRidaParemalt
            uusRida.MääraLaius(laius)
            uusRida.Joonista()
            counter += 1
        


class PäevaRuudustik:
    def __init__(self, olek:ProgrammiOlek, pind):
        self.olek = olek
        self.pind = pind
        self.laius = 400
        self.asukoht = (0,0)
        self.päevaRuudud: List[PäevaRuut] = []
        päevad = VõtaKõikAlgusPäevad(olek.sündmusteNimekiri)
        for i in päevad:
            print(olek.päevaruuduVärv)
            uusRuut = PäevaRuut(olek, pind, i)
            self.päevaRuudud.append(uusRuut)

    def MääraLaius(self, laius):
        self.laius = laius

    def MääraAsukoht(self, asukoht):
        self.asukoht = asukoht

    def Joonista(self):
        # Tausta kõrgus leitakse selle põhjal mitu rida ruute tuleb ja see arvutatakse hiljem.
        taustaAsukx = self.asukoht[0]
        taustaAsuky = self.asukoht[0]
        taustaLaius = self.laius

        # Mitu ruutu mahub ühte ritta.
        äärevahe = self.olek.päevaruutudeTaustaJaRuutudeVahe
        ruuduvahe = self.olek.päevaruutudeVahe
        minLaius = self.olek.päevaruuduMinLaius
        # Leiab, mitu ruutu mahub ühte ritta. Põhineb sellel, et vaatab kui palju ruutudevahe suurusid saab vahemikku panna nii, et ülejäänud vahemikku ühe võrra suurema kogusega jagades ei annaks tulemust alla min laiuse.
        mituReas = 0
        mituVahet = 0
        ruum = taustaLaius-2*äärevahe
        while True:
            if (ruum - mituVahet * ruuduvahe) / (mituVahet+1) < minLaius:
                mituReas = mituVahet
                break
            else:
                mituVahet += 1

        
        # Võib olla olukord, kus aken läheb nii kitsaks, et isegi, kui reas on ainult 1 ruut, on sellel ikkagi nii vähe ruumi, et reas peaks olema null ruutu. See kood parandab olukorra ja lic lepib sellega, et ruudu laius on väiksem, kui minlaius.
        if mituReas == 0: mituReas = 1
        
        # Arvutab, kui palju ruumi jääb vahede kõrvalt ruutudele. Mis peab ühe reasoleva ruudu laius olema. 
        vahesidKokku = 2*äärevahe + (mituReas-1)*ruuduvahe
        ruudulaius = (taustaLaius - vahesidKokku)/mituReas

        # Hakkab kõiki ruutusid paigutama.
        counter = 0
        ridadeArv = 0
        vasakServ = taustaAsukx
        ülemServ = taustaAsuky

        ruuduKõrgus = self.olek.päevaruuduKõrgus
        for i in self.päevaRuudud:

            mitmesTulp = counter % mituReas
            mitmesRida = floor(counter/mituReas)
            # Kui kõik ruudud on läbi käidud, ss on ridadeArv võrdne sellega, kui palju ridasid on ruudustikus. Seda väärtust kasutab taust, et oma kõrgus leida.
            ridadeArv = mitmesRida


            asukx = vasakServ + äärevahe + mitmesTulp*(ruudulaius + ruuduvahe)
            asuky = ülemServ + äärevahe + mitmesRida*(ruuduKõrgus + ruuduvahe)

            i.MääraAsukoht(asukx, asuky)
            i.MääraSuurus(ruudulaius, ruuduKõrgus)
            counter += 1

        taustaKõrgus = 2*äärevahe + (ridadeArv+1)*ruuduKõrgus + (ridadeArv)*ruuduvahe

        # PAIGUTAMINE LÕPPES

        # ALGAB JOONISTAMINE

        # Taust
        taustaVärv = self.olek.päevaruutudeTaustaVärv
        nurgaRaadius = self.olek.päevaruutudeTaustaNurgaÜmardus
        pygame.draw.rect(self.pind, taustaVärv, (taustaAsukx, taustaAsuky, taustaLaius, taustaKõrgus), border_radius=nurgaRaadius)

        # Ruudud
        for i in self.päevaRuudud:
            i.Joonista()
            


        



        





class PäevaRuudustikVana:
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