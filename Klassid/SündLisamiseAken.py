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
from Klassid.KuupäevaKüsija import KuupäevaKüsija, KellaajaKüsija





class SündmuseLisamiseAken:
    def __init__(self, olek:"ProgrammiOlek", pind:pygame.surface.Surface):
        self.olek = olek
        self.pind = pind
        self.asukoht = (0,0)
        self.suurus = (400,400)
        
        # Mõlemad tausta ristkülikud
        raad = self.olek.sündmuseLisamiseNurgaRaadius
        värv = self.olek.sündmuseLisamiseTaustaVärv
        self.taust = Ristkülik(self.pind)
        self.taust.MääraNurgaRaadius(raad)
        self.taust.MääraVärv(värv)
        
        värv2 = self.olek.sündmuseLisamiseHeledamaTaustaVärv
        self.taust2 = Ristkülik(self.pind)
        self.taust2.MääraVärv(värv2)
        vahe = self.olek.sündmuseLisamiseHeledamaTaustaVahe
        raad2 = raad-vahe
        self.taust2.MääraNurgaRaadius(raad2)
        
        # Nime kirjeldustekst
        font = olek.sündmuseLisamiseInfoKirjaFont
        self.nimeKirjeldus = MitmeReaTekst(self.olek, self.pind, "Uue sündmuse kirjeldus:", font)
        self.nimeKirjeldus.MääraReavahe(12)

        # Nime küsimise tekstikast
        self.nimeKast = SelgitavTekstikast(olek, pind)
        self.nimeKast.MääraSõnum("Sündmuse nimi:")
        self.nimeKast.MääraSelgitusKastiSees(True)
        self.nimeKast.MääraKeskeleJoondus(True)
        
        # Alguskuupäeva kirjeldustekst
        font = olek.sündmuseLisamiseInfoKirjaFont
        self.algKuupKirjeldus = MitmeReaTekst(self.olek, self.pind, "Sündmuse alguskuupäev:", font)
        self.algKuupKirjeldus.MääraReavahe(12)


        def intKontroll(tekst):
            try:
                int(tekst)
                return True
            except:
                return False
        
        self.algKuupKüsija = KuupäevaKüsija(self.olek, self.pind)


        # Päeva küsimise tekstikast
        self.päevaKast = SelgitavTekstikast(olek, pind)
        self.päevaKast.MääraSõnum("Päev:")
        self.päevaKast.MääraKeskeleJoondus(True)
        self.päevaKast.MääraVeaKontrolliFunktsioon(intKontroll)

        # Kuupäeva küsija
        self.kpKüsija = KuupäevaKüsija(self.olek, self.pind)
        
        # alguskellaja küsija kirjeldus
        self.algKellaKirjeldus = MitmeReaTekst(self.olek, self.pind, "Sündmuse alguskellaaeg:", font)
        self.algKellaKirjeldus.MääraReavahe(12)

        # alguskellaaja küsija
        self.algKellaKüsija = KellaajaKüsija(self.olek, self.pind)
        
        # Lõppkuuppäeva kirjeldus
        self.lõppKuupKirjeldus = MitmeReaTekst(self.olek, self.pind, "Sündmuse lõppkuupäev:", font)
        self.lõppKuupKirjeldus.MääraReavahe(12)

        # Lõppkuupäeva küsija
        self.lõppKpKüsija = KuupäevaKüsija(self.olek, self.pind)

        # Lõppkellaaja kirjeldus
        self.lõppKellaKirjeldus = MitmeReaTekst(self.olek, self.pind, "Sündmuse lõppkellaaeg:", font)
        self.lõppKellaKirjeldus.MääraReavahe(12)

        # alguskellaaja küsija
        self.lõppKellaKüsija = KellaajaKüsija(self.olek, self.pind)
        

        # Tausta nupp
        def f1(): pass
        prio = self.olek.nuppudePrioriteedid["sündmuse lisamise aken"]
        self.nupp = NupuAlus(self.olek, prio, f1)

        # Selle objekti asjade kirjutamise lõpetamise funktsioon. 
        self.nupp.funktsioon = self.LõpetaKirjutamine
        self.kpKüsija.LõpetaKõigiKirjutamine = self.LõpetaKirjutamine
        self.nimeKast.kast.LõpetaKõigiKirjutamine = self.LõpetaKirjutamine
        self.algKellaKüsija.LõpetaKõigiKirjutamine = self.LõpetaKirjutamine
        self.lõppKpKüsija.LõpetaKõigiKirjutamine = self.LõpetaKirjutamine
        self.lõppKellaKüsija.LõpetaKõigiKirjutamine = self.LõpetaKirjutamine
        



        
        # Sündmuse loomise nupp: 
        prio = olek.nuppudePrioriteedid["sündmuse loomise nupp"]
        # f1 on funktsioon, mille viib täide sündmuse loomise nupp. Pmst loeb igast kastist teksti, mis sinna on kirjutatud, teeb intiks siis teeb sündmuse ja lsiab selle nimekirja
        def f1():
            if self.nimeKast.VõtaTekst() == "" or self.kpKüsija.VõtaKuupäev() == None:
                return
            # Koostab sünmuse teades nime ja kuupäeva - kahe asjaga, mis on kindlsti olemas, sesst ilma nendeta ei töötaks sündmsue loomise nupp.
            # Kui sündmus on loodud, proovib veel lisada algkellaaega, lõppkuupäeva ja lõppkellaaega. Kui neid ei saa välja lugeda, ss jääb ilma nendeta.
            nimi = self.nimeKast.VõtaTekst()
            algusKuupäev = self.kpKüsija.VõtaKuupäev()
            uusSündmus = Sündmus(nimi,algusKuupäev,GenereeriID(self.olek))
            uusSündmus.ajaTüüp = 0
            
            algusKell = self.algKellaKüsija.VõtaKellaaeg()
            if algusKell != None:
                uusSündmus.algusaeg = algusKell
                uusSündmus.ajaTüüp = 1
                
            lõppKuupäev = self.lõppKpKüsija.VõtaKuupäev()
            if lõppKuupäev != None:
                uusSündmus.ajaTüüp += 2
                uusSündmus.lõppkuupäev = lõppKuupäev
            
            if uusSündmus.ajaTüüp > 1:
                pass
            else:
                lõppKell = self.lõppKellaKüsija.VõtaKellaaeg()
                if lõppKell != None:
                    uusSündmus.lõppaeg = lõppKell
                    uusSündmus.ajaTüüp += 2
                
            
            
            # Lõpus lisab loodud sünmduse olekus sündmuste nimekirja.
            self.olek.sündmusteNimekiri.append(uusSündmus)
        self.looSündmusNupp = NupuAlus(olek, prio, f1)
    

    def LõpetaKirjutamine(self):
        self.nimeKast.kast.LõpetaKirjutamine()
        self.kpKüsija.LõpetaKirjutamine()
        self.algKellaKüsija.LõpetaKirjutamine()
        self.lõppKpKüsija.LõpetaKirjutamine()
        self.lõppKellaKüsija.LõpetaKirjutamine()

    # Juhuks, kui on plaanis lisada kusagile tekstikaste väljaspool seda objekti nii, et selles objektis kirjutamise alustamine peaks lõpetama obj välise kitjuamise. Kui midagi sellist lisandub, ss seal, kus on selle objekti asjade kirjutamise lõpetamise funktsioon, tuleb määrata LõpetaKõigiKirjutamise funktsioon alamobjketide funktsiooniks. Lihtsalt 
    def LõpetaKõigiKirjutamine(self): pass

    def Joonista(self):
        self.PaneValmis()
        self.taust.Joonista()
        self.taust2.Joonista()
        self.nimeKirjeldus.Joonista()
        self.kpKüsija.Joonista()
        self.nimeKast.Joonista()
        self.algKuupKirjeldus.Joonista()
        self.algKellaKirjeldus.Joonista()
        self.algKellaKüsija.Joonista()
        self.lõppKuupKirjeldus.Joonista()
        self.lõppKpKüsija.Joonista()
        self.lõppKellaKirjeldus.Joonista()
        self.lõppKellaKüsija.Joonista()
        self.looSündmusNupp.Joonista(self.pind)
        
        

    def PaneValmis(self):
        self.nupp.TegeleNupuga()
        self.looSündmusNupp.MääraVäljaLülitatus(False)
        

        # Neid muutujaid hakkab kasutama mitu objekti.
        servadest = self.suurus[0]*0.1
        asukx = self.asukoht[0]+ servadest
        suurx = self.suurus[0] - 2*servadest

        # Nimekirjeldus
        asuky = self.asukoht[1] + 30
        self.nimeKirjeldus.MääraAsukoht((asukx, asuky))
        self.nimeKirjeldus.MääraLaius(suurx)
        
        asukx = self.asukoht[0] + self.suurus[0] * 0.1
        asuky = self.asukoht[1] + 300
        self.algKuupKüsija.MääraAsukoht((asukx, asuky))
        self.algKuupKüsija.MääraSuurus((300,100))
        self.algKuupKüsija.Joonista()
        
        
        # Tekstikast
        asuky = asuky + self.nimeKirjeldus.KuiPaljuRuumiOnVaja() + 15
        tkAsukx = self.asukoht[0] + self.suurus[0] / 2
        self.nimeKast.MääraAsukoht((tkAsukx, asuky))
        self.nimeKast.MääraSuurus((suurx, 69))
        
        # Alguskuupäeva kirjeldus
        asuky = asuky + self.nimeKast.VõtaSuurus()[1] + 20
        self.algKuupKirjeldus.MääraAsukoht((asukx, asuky))
        self.algKuupKirjeldus.MääraLaius(suurx)

        # algusKuupäevaküsija
        asuky = asuky + self.algKuupKirjeldus.KuiPaljuRuumiOnVaja() + 15
        self.kpKüsija.MääraAsukoht((asukx, asuky))
        self.kpKüsija.MääraSuurus((suurx, 100))
        self.kpKüsija.PaneValmis()
        
        # Alguskellaaja kirjeldus
        asuky = asuky + self.kpKüsija.VõtaSuurus()[1] + 20
        self.algKellaKirjeldus.MääraAsukoht((asukx, asuky))
        self.algKellaKirjeldus.MääraLaius(suurx)
        
        # Algkellaküsija
        asuky = asuky + self.algKellaKirjeldus.KuiPaljuRuumiOnVaja() + 15
        self.algKellaKüsija.MääraAsukoht((asukx, asuky))
        self.algKellaKüsija.MääraSuurus((suurx, 1000))
        self.algKellaKüsija.PaneValmis()
        
        # Lõppkuupäeva kirjeldus
        asuky = asuky + self.algKellaKüsija.VõtaSuurus()[1] + 20
        self.lõppKuupKirjeldus.MääraAsukoht((asukx, asuky))
        self.lõppKuupKirjeldus.MääraLaius(suurx)

        # Lõppkuupäevaküsija
        asuky = asuky + self.algKuupKirjeldus.KuiPaljuRuumiOnVaja() + 15
        self.lõppKpKüsija.MääraAsukoht((asukx, asuky))
        self.lõppKpKüsija.MääraSuurus((suurx, 100))
        self.lõppKpKüsija.PaneValmis()
        
        # Lõppkellaaja kirjeldus
        asuky = asuky + self.algKellaKüsija.VõtaSuurus()[1] + 20
        self.lõppKellaKirjeldus.MääraAsukoht((asukx, asuky))
        self.lõppKellaKirjeldus.MääraLaius(suurx)
        
        # Lõppkella küsija
        asuky = asuky + self.lõppKellaKirjeldus.KuiPaljuRuumiOnVaja() + 15
        self.lõppKellaKüsija.MääraAsukoht((asukx, asuky))
        self.lõppKellaKüsija.MääraSuurus((suurx, 1000))
        self.lõppKellaKüsija.PaneValmis()
        
        # SÜndmuse loomise nupp
        suurx = self.suurus[0] * 0.3
        suury = self.suurus[1] * 0.1
        asukx = self.asukoht[0] + self.suurus[0]/2 - suurx /2
        asuky = asuky + self.lõppKellaKüsija.VõtaSuurus()[1] + 20
        self.looSündmusNupp.MääraAsukoht((asukx, asuky))
        self.looSündmusNupp.MääraSuurus((suurx, suury))
        
        # Taustade suurused
        asuk = self.asukoht
        suurx = self.suurus[0]
        suury = asuky - self.asukoht[1] + self.lõppKellaKüsija.VõtaSuurus()[1] + 20
        self.taust.MääraAsukoht(asuk[0], asuk[1])
        self.taust.MääraSuurus(suurx, suury)
        
        vahe = self.olek.sündmuseLisamiseHeledamaTaustaVahe
        suurx = suurx - 2*vahe
        suury = suury - 2*vahe
        asuk = (self.asukoht[0] + vahe, self.asukoht[1] + vahe)
        self.taust2.MääraAsukoht(asuk[0], asuk[1])
        self.taust2.MääraSuurus(suurx, suury)


    def MääraAsukoht(self, asukoht):
        self.asukoht = asukoht
        self.nupp.MääraAsukoht(asukoht)
        
    def MääraSuurus(self, suurus):
        self.suurus = suurus
        self.nupp.MääraSuurus(suurus)
