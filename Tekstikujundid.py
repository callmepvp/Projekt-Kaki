import pygame
from Kujundid import *
from Tekst import *
from Sündmused import *
from math import floor
from typing import List
from Programm import ProgrammiOlek

class SündmuseRida:
    # Oke, mu jaoks on see süntaks uus, aga pmst see on ainus viis pythonis märkida, et sisestatud parameeter peab olema mingi kindla klassi esindaja ja kui pole, ss ei tohiks joosta. Süntaks järgmine: parameeter: "klassiNimi". Klassinimi justkui oleks tekst, aga tegelt pole.
    def __init__(self, pind, sündmus: "Sündmus", asukoht, laius):
        self.sündmus = sündmus
        self.pind = pind
        self.asukoht = asukoht
        self.nimePygFont = pygame.font.Font("Fondid/Gogh-ExtraBold.ttf", 40)
        self.ajaPygFont = pygame.font.Font("Fondid/Gogh-ExtraBold.ttf", 25)
        self.laius = laius
        self.täpiVahe = 20

    def Joonista(self):
        
        # Täpp teksti ees.
        pygame.draw.circle(self.pind, (10, 10, 10), self.asukoht, 8)

        #Pelkirja asukoht olgu täpist täpivahe px võrra edasi.
        pealkirjaAsuk = (self.asukoht[0] + self.täpiVahe, self.asukoht[1])

        # Kui on kellaaeg, siis leiab kellaaja laiuse ja joonistab kellaaja.
        ajaLaius = 0
        ajatekst = ""
        if self.sündmus.lõppKell.KasOnKell() is True:
            ajatekst = self.sündmus.lõppKell.VõtaStringina()
            ajaLaius = self.ajaPygFont.size(ajatekst)[0]
            ajaAsuk = (self.asukoht[0] + self.laius - ajaLaius, self.asukoht[1])
            kell = Tekst(self.pind, ajatekst, self.ajaPygFont, (10,10,10), ajaAsuk)
            kell.Joonista()

        # Leitakse, kui palju ruumi jääb pealkirjale täpi ja kellaaja kõrvalt.
        ruum = self.laius - self.täpiVahe - ajaLaius - 20

        # Pealkirjast valitakse osa, mis mahub leitud laiusesse.
        pealkTekst = self.sündmus.VõtaNimi()
        mahtuvTekst = EraldaSobivaPikkusegaTekst(pealkTekst, ruum, self.nimePygFont)[0]

        # Pealkirja joonistamine
        pealkiri = Tekst(self.pind, mahtuvTekst,self.nimePygFont, (10,10,10), pealkirjaAsuk)
        pealkiri.Joonista()

    def MuudaLaiust(self, laius):
        self.laius = laius


class PäevaRuut:
    def __init__(self, olek:"ProgrammiOlek", sündmused):
        self.kuupäev = sündmused[0].VõtaKuupäev()
        self.suurus = (10,10)
        self.asuk = (10,10)
        

    def MääraAsukoht(self, x, y):
        self.asuk = (x,y)

    def MääraSuurus(self, x, y):
        self.suurus = (x,y)
        
    
        



class PäevaPealkiri:
    def __init__(self, olek:"ProgrammiOlek", kuupäev:"Kuupäev"):
        self.font = fontObject
        self.kuupäev = kuupäev
        self.päevKuuTekst = Tekst(pind,kuupäev.VõtaPäevKuuTekstina(), fontObject, 

    def Paiguta(x, y):
        
        



class Ristkülik:
    def __init__(self, pind, asukoht, suurus):
        self.asuk = asukoht
        self.suur = suurus
        self.pind = pind
        self.värv = (200, 200, 200)

    # Funktsiooni saab panna ka None sisse kummagi väärtuse asemele, mis jätab suuruse samaks.
    def MääraSuurus(self, x, y):
        if x == None:
            self.suur = (self.suur[0], y)
        elif y == None:
            self.suur = (x, self.suur[1])
        self.suur = (x,y)
    
    def MääraAsukoht(self, x, y):
        self.asuk = (x,y)

    def VõtaSuurus(self):
        return self.suur

    def VõtaAsukoht(self):
        return self.asuk

    def Joonista(self):
        pygame.draw.rect(self.pind, self.värv, (self.VõtaAsukoht(), self.VõtaSuurus()), border_radius=5)


ruut = PäevaRuut()
päevaRuudud = []  

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