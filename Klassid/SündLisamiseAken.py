from Klassid.Kujundid import Ristkülik
from Klassid.Kuupäev import Kuupäev
from Klassid.Tekst import MitmeReaTekst
from Programmiolek import ProgrammiOlek
import pygame
from Klassid.Nupp import NupuAlus
from Klassid.Tekstikast import SelgitavTekstikast
from typing import List
from Klassid.Sündmus import Sündmus
from Funktsioonid.UtilityFunktsioonid import GenereeriID





class SündmuseLisamiseAken:
    def __init__(self, olek:"ProgrammiOlek", pind:pygame.surface.Surface):
        self.olek = olek
        self.pind = pind
        self.asukoht = (0,0)
        self.suurus = (400,400)
        
        # Tausta ristküliku koostamine
        raad = self.olek.sündmuseLisamiseNurgaRaadius
        värv = self.olek.sündmuseLisamiseTaustaVärv
        self.taust = Ristkülik(self.pind)
        self.taust.MääraNurgaRaadius(raad)
        self.taust.MääraVärv(värv)
        
        värv2 = self.olek.sündmuseLisamiseHeledamaTaustaVärv
        self.taust2 = Ristkülik(self.pind)
        self.taust2.MääraVärv(värv2)
        
        # Nime küsimise tekstikast
        self.nimeKast = SelgitavTekstikast(olek, pind)
        self.nimeKast.MääraSõnum("Uue sündmuse kirjeldus:")
        
        # Päeva küsimise tekstikast
        self.päevaKast = SelgitavTekstikast(olek, pind)
        self.päevaKast.MääraSõnum("Päev:")
        self.päevaKast.MääraKeskeleJoondus(True)
        def veaf(tekst):
            try:
                int(tekst)
                return True
            except:
                return False
        self.päevaKast.MääraVeaKontrolliFunktsioon(veaf)
        
        # Kuu küsimise tekstikast
        self.kuuKast = SelgitavTekstikast(olek, pind)
        self.kuuKast.MääraSõnum("Kuu:")
        self.kuuKast.MääraKeskeleJoondus(True)
        
        # Aasta küsimise tekstikast
        self.aastaKast = SelgitavTekstikast(olek, pind)
        self.aastaKast.MääraSõnum("Aasta:")
        self.aastaKast.MääraKeskeleJoondus(True)

        # Veateade
        font = self.olek.sündmuseLisamiseInfoKirjaFont
        self.veateade = MitmeReaTekst(olek, pind, "", font)
        self.veateade.MääraVärv((255, 25, 34, 255))
        self.veateade.MääraReavahe(10)

        # Tausta nupp
        nupud:List[SelgitavTekstikast] = [self.nimeKast, self.päevaKast, self.kuuKast, self.aastaKast]
        def f1():
            if self.olek.tegevuseNäitamine == True: print("Kastidesse kirjutamine lõppes.")
            for i in nupud:
                i.MääraKirjutamine(False)
        for i in nupud:
            i.kast.lõpetaKõigiKirjutamine = f1
            
        prio = self.olek.nuppudePrioriteedid["sündmuse lisamise aken"]
        self.nupp = NupuAlus(self.olek, prio, f1)
        
        # Loo sündmuse nupp:
        prio = olek.nuppudePrioriteedid["sündmuse loomise nupp"]
        def f1():
            nimi = self.nimeKast.VõtaTekst()
            päev = int(self.päevaKast.VõtaTekst())
            kuu = int(self.kuuKast.VõtaTekst())
            aasta = int(self.aastaKast.VõtaTekst())
            kuup = Kuupäev(päev, kuu, aasta)
            uusSündmus = Sündmus(nimi,kuup,GenereeriID(self.olek))
            self.olek.sündmusteNimekiri.append(uusSündmus)
            
        self.looSündmusNupp = NupuAlus(olek, prio, f1)
        

    def Joonista(self):
        self.nupp.TegeleNupuga()
        
        
        # Taust
        asuk = self.asukoht
        suur = self.suurus
        self.taust.MääraAsukoht(asuk[0], asuk[1])
        self.taust.MääraSuurus(suur[0], suur[1])
        self.taust.Joonista()
        
        vahe = self.olek.sündmuseLisamiseHeledamaTaustaVahe
        raad = self.taust.nurgaRaadius
        raad2 = raad-vahe
        self.taust2.MääraNurgaRaadius(raad2)
        asuk = (self.asukoht[0] + vahe, self.asukoht[1] + vahe)
        suur = (self.suurus[0] - 2* vahe, self.suurus[1] - 2*vahe)
        self.taust2.MääraAsukoht(asuk[0], asuk[1])
        self.taust2.MääraSuurus(suur[0], suur[1])
        self.taust2.Joonista()

        
        # Tekstikast
        servadest = self.suurus[0]*0.1
        suurx = self.suurus[0]-2*servadest
        asukx = self.asukoht[0] + self.suurus[0]*0.1
        asuky = self.asukoht[1] + 20
        self.nimeKast.MääraAsukoht((asukx, asuky))
        self.nimeKast.MääraSuurus((suurx, 69))
        self.nimeKast.Joonista()
        
        # Päeva kast
        asuky = asuky + self.nimeKast.VõtaSuurus()[1] + 20
        asukx1 = self.asukoht[0] + self.suurus[0]/2 - self.suurus[0]*0.3
        asukx2 = self.asukoht[0] + self.suurus[0]/2
        asukx3 = self.asukoht[0] + self.suurus[0]/2 + self.suurus[0]*0.3
        laiused = self.suurus[0] * 0.2
        self.päevaKast.MääraAsukoht((asukx1,asuky))
        self.päevaKast.MääraSuurus((laiused, None))
        self.päevaKast.Joonista()
        
        if self.päevaKast.VõtaVeaTeade() == False:
            print("Asi ei sobi kuupäevaks.")
        else:
            print("saab teha numbriks")
        
        
            
        self.kuuKast.MääraAsukoht((asukx2,asuky))
        self.kuuKast.MääraSuurus((laiused, None))
        self.kuuKast.Joonista()
        
        self.aastaKast.MääraAsukoht((asukx3,asuky))
        self.aastaKast.MääraSuurus((laiused, None))
        self.aastaKast.Joonista()
        
        asukx = self.nimeKast.asukoht[0]
        asuky = self.päevaKast.asukoht[1] + max(self.päevaKast.VõtaSuurus()[1], self.kuuKast.VõtaSuurus()[1], self.aastaKast.VõtaSuurus()[1]) + 10

        self.veateade.MääraLaius(self.suurus[0])
        self.veateade.MääraAsukoht((asukx, asuky))
        self.veateade.MääraTekst("")
        self.veateade.MääraLaius(self.nimeKast.VõtaSuurus()[0])
        if self.päevaKast.VõtaVeaTeade() == False:
            self.veateade.tekst += "Päevakasti kirja ei saa numbriks teha."
        self.veateade.Joonista()
        
        suurx = self.suurus[0] * 0.3
        suury = self.suurus[1] * 0.1
        asukx = self.asukoht[0] + self.suurus[0]/2 - suurx /2
        asuky = self.asukoht[1] + self.suurus[1]- suury*1.2
        self.looSündmusNupp.MääraAsukoht((asukx, asuky))
        self.looSündmusNupp.MääraSuurus((suurx, suury))
        self.looSündmusNupp.Joonista(self.pind)


    def MääraAsukoht(self, asukoht):
        self.asukoht = asukoht
        self.nupp.MääraAsukoht(asukoht)
        
    def MääraSuurus(self, suurus):
        self.suurus = suurus
        self.nupp.MääraSuurus(suurus)



    
