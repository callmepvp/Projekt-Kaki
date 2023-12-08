from Klassid.Kujundid import Ristkülik
from Klassid.Kuupäev import Kellaaeg, Kuupäev
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
        

        def intKontroll(tekst):
            try:
                int(tekst)
                return True
            except:
                return False
            

        # Päeva küsimise tekstikast
        self.päevaKast = SelgitavTekstikast(olek, pind)
        self.päevaKast.MääraSõnum("Päev:")
        self.päevaKast.MääraKeskeleJoondus(True)
        self.päevaKast.MääraVeaKontrolliFunktsioon(intKontroll)
        
        # Kuu küsimise tekstikast
        self.kuuKast = SelgitavTekstikast(olek, pind)
        self.kuuKast.MääraSõnum("Kuu:")
        self.kuuKast.MääraKeskeleJoondus(True)
        self.kuuKast.MääraVeaKontrolliFunktsioon(intKontroll)
        
        # Aasta küsimise tekstikast
        self.aastaKast = SelgitavTekstikast(olek, pind)
        self.aastaKast.MääraSõnum("Aasta:")
        self.aastaKast.MääraKeskeleJoondus(True)
        self.aastaKast.MääraVeaKontrolliFunktsioon(intKontroll)

        # Algusaja tunni kast
        self.algTunniKast = SelgitavTekstikast(olek, pind)
        self.algTunniKast.MääraSõnum("Tund:")
        self.algTunniKast.MääraKeskeleJoondus(True)
        self.algTunniKast.MääraVeaKontrolliFunktsioon(intKontroll)
        
        # Algusaja minuti
        self.algMinutiKast = SelgitavTekstikast(olek, pind)
        self.algMinutiKast.MääraSõnum("Minut:")
        self.algMinutiKast.MääraKeskeleJoondus(True)
        self.algMinutiKast.MääraVeaKontrolliFunktsioon(intKontroll)

        # Veateade
        font = self.olek.sündmuseLisamiseInfoKirjaFont
        self.veateade = MitmeReaTekst(olek, pind, "", font)
        self.veateade.MääraVärv((255, 25, 34, 255))
        self.veateade.MääraReavahe(15)
        self.veateade.MääraRidadeArv(0)
        

        # Tausta nupp
        nupud:List[SelgitavTekstikast] = [self.nimeKast, self.päevaKast, self.kuuKast, self.aastaKast, self.algTunniKast, self.algMinutiKast]
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
        # See on funktsioon, mis antakse sündmuse loomise nupule. Pmst loeb igast kastist teksti, mis sinna on kirjutatud, teeb intiks siis teeb sündmuse ja lsiab selle nimekirja
        def f1():
            # Koostab sünmuse teades nime ja kuupäeva - kahe asjaga, mis on kindlsti olemas, sesst ilma nendeta ei töötaks sündmsue loomise nupp.
            nimi = self.nimeKast.VõtaTekst()
            päev = int(self.päevaKast.VõtaTekst())
            kuu = int(self.kuuKast.VõtaTekst())
            aasta = int(self.aastaKast.VõtaTekst())
            kuup = Kuupäev(päev, kuu, aasta)
            uusSündmus = Sündmus(nimi,kuup,GenereeriID(self.olek))
            uusSündmus.ajaTüüp = 0
            
            # Kui sündmus on loodud, kontrollib veel tunni ja minuti kasti, võimalusel teeb kellaaja objekti ja lisab selle sündmusele, aga kui ei saa, ss ei tee midagi.
            t = self.algTunniKast.VõtaTekst()
            m = self.algMinutiKast.VõtaTekst()
            try: 
                t = int(t)
                m = int(m)
                kell = Kellaaeg(t, m)
                uusSündmus.algusaeg = kell
                uusSündmus.ajaTüüp = 1
            except:
                pass
            
            # Lõpus lisab loodud sünmduse olekus sündmuste nimekirja.
            self.olek.sündmusteNimekiri.append(uusSündmus)
        self.looSündmusNupp = NupuAlus(olek, prio, f1)
        

    def Joonista(self):
        self.nupp.TegeleNupuga()
        self.looSündmusNupp.MääraVäljaLülitatus(False)
        
        
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
        
            
        self.kuuKast.MääraAsukoht((asukx2,asuky))
        self.kuuKast.MääraSuurus((laiused, None))
        self.kuuKast.Joonista()
        
        self.aastaKast.MääraAsukoht((asukx3,asuky))
        self.aastaKast.MääraSuurus((laiused, None))
        self.aastaKast.Joonista()
        

        # KELLAAJA KASTIDE PAIGUTAMINE
        # Üldised kellaaja kastide paigutamiseks vajalikud asukohad
        kuupäevaKastideAlServ = self.päevaKast.asukoht[1] + max(self.päevaKast.VõtaSuurus()[1], self.kuuKast.VõtaSuurus()[1], self.aastaKast.VõtaSuurus()[1])
        kuupäevastKellani = 30
        asuky = kuupäevaKastideAlServ + kuupäevastKellani
        
        # Tunnikast:
        asukx = (self.asukoht[0] + self.suurus[0] / 2) + self.suurus[0]*0.11
        self.algTunniKast.MääraAsukoht((asukx,asuky))
        self.algTunniKast.MääraSuurus((laiused, None))
        self.algTunniKast.Joonista()
        
        # Päevakast:
        asukx = (self.asukoht[0] + self.suurus[0] / 2) - self.suurus[0]*0.11
        self.algMinutiKast.MääraAsukoht((asukx, asuky))
        self.algMinutiKast.MääraSuurus((laiused, None))
        self.algMinutiKast.Joonista()
        
        

        # Veateate paigutamine ja jonistamine
        
        asukx = self.nimeKast.asukoht[0]
        asuky = self.päevaKast.asukoht[1] + max(self.päevaKast.VõtaSuurus()[1], self.kuuKast.VõtaSuurus()[1], self.aastaKast.VõtaSuurus()[1]) + 10

        self.veateade.MääraLaius(self.suurus[0])
        self.veateade.MääraAsukoht((asukx, asuky))
        self.veateade.MääraTekst("")
        self.veateade.MääraLaius(self.nimeKast.VõtaSuurus()[0])
        
        
        if self.nimeKast.VõtaTekst() == "" or self.päevaKast.VõtaTekst() == "" or self.kuuKast.VõtaTekst() == "" or self.aastaKast.VõtaTekst() == "":
            self.looSündmusNupp.MääraVäljaLülitatus(True)
        
        
            
        if self.päevaKast.VõtaVeaTeade() == False and self.päevaKast.VõtaTekst() != "":
            self.veateade.tekst += "Päevakasti kirja ei saa numbriks teha.\n"
            self.looSündmusNupp.MääraVäljaLülitatus(True)
        if self.kuuKast.VõtaVeaTeade() == False and self.kuuKast.VõtaTekst() != "":
            self.veateade.tekst += "Kuukasti kirja ei saa numbriks teha.\n"
            self.looSündmusNupp.MääraVäljaLülitatus(True)
        if self.aastaKast.VõtaVeaTeade() == False and self.aastaKast.VõtaTekst() != "":
            self.veateade.tekst += "Aastakasti kirja ei saa numbriks teha.\n"
            self.looSündmusNupp.MääraVäljaLülitatus(True)
            
        if self.päevaKast.VõtaTekst() != "" and self.kuuKast.VõtaTekst() != "" and self.aastaKast.VõtaTekst() != "" and self.veateade.tekst == "":
            a = Kuupäev(int(self.päevaKast.VõtaTekst()), int(self.kuuKast.VõtaTekst()), int(self.aastaKast.VõtaTekst()))
            if not a.KasVõimalik():
                self.looSündmusNupp.kasVäljaLülitatud = True
            else:
                self.veateade.tekst += "Saab teha kuupäevaks."
                

        
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



    
