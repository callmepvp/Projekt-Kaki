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
from Klassid.KuupäevaKüsija import KellaajaKüsija, KuupäevaKüsija



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
        self.nimeKirjeldus.MääraReavahe(10)

        # Nime küsimise tekstikast
        self.nimeKast = SelgitavTekstikast(olek, pind)
        self.nimeKast.MääraSõnum("Sündmuse nimi:")
        self.nimeKast.MääraSelgitusKastiSees(True)
        self.nimeKast.MääraKeskeleJoondus(True)
        
        # Alguskuupäeva kirjeldustekst
        font = olek.sündmuseLisamiseInfoKirjaFont
        self.algKuupKirjeldus = MitmeReaTekst(self.olek, self.pind, "Sündmuse alguskuupäev:", font)

        # Kuupäeva küsija
        self.kpKüsija = KuupäevaKüsija(self.olek, self.pind)
        
        # alguskellaja küsija kirjeldus
        self.algKellaKirjeldus = MitmeReaTekst(self.olek, self.pind, "Sündmuse alguskellaaeg:", font)

        # alguskellaaja küsija
        self.algKellaKüsija = KellaajaKüsija(self.olek, self.pind)
        

        # Tausta nupp
        def f1(): pass
        prio = self.olek.nuppudePrioriteedid["sündmuse lisamise aken"]
        self.nupp = NupuAlus(self.olek, prio, f1)

        # Selle objekti asjade kirjutamise lõpetamise funktsioon. 
        self.nupp.funktsioon = self.LõpetaKirjutamine
        self.kpKüsija.LõpetaKõigiKirjutamine = self.LõpetaKirjutamine
        self.nimeKast.kast.LõpetaKõigiKirjutamine = self.LõpetaKirjutamine
        self.algKellaKüsija.LõpetaKõigiKirjutamine = self.LõpetaKirjutamine



        
        # Sündmuse loomise nupp: 
        prio = olek.nuppudePrioriteedid["sündmuse loomise nupp"]
        # f1 on funktsioon, mille viib täide sündmuse loomise nupp. Pmst loeb igast kastist teksti, mis sinna on kirjutatud, teeb intiks siis teeb sündmuse ja lsiab selle nimekirja
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
    

    def LõpetaKirjutamine(self):
        self.kpKüsija.LõpetaKirjutamine()
        self.nimeKast.kast.LõpetaKirjutamine()
        self.algKellaKüsija.LõpetaKirjutamine()

    # Juhuks, kui on plaanis lisada kusagile tekstikaste väljaspool seda objekti nii, et selles objektis kirjutamise alustamine peaks lõpetama obj välise kitjuamise. Kui midagi sellist lisandub, ss seal, kus on selle objekti asjade kirjutamise lõpetamise funktsioon, tuleb määrata LõpetaKõigiKirjutamise funktsioon alamobjketide funktsiooniks. Lihtsalt 
    def LõpetaKõigiKirjutamine(self): pass

    def Joonista(self):
        self.nupp.TegeleNupuga()
        self.looSündmusNupp.MääraVäljaLülitatus(False)
        
        
        # Mõlemad taustad
        asuk = self.asukoht
        suur = self.suurus
        self.taust.MääraAsukoht(asuk[0], asuk[1])
        self.taust.MääraSuurus(suur[0], suur[1])
        self.taust.Joonista()
        
        vahe = self.olek.sündmuseLisamiseHeledamaTaustaVahe
        asuk = (self.asukoht[0] + vahe, self.asukoht[1] + vahe)
        suur = (self.suurus[0] - 2* vahe, self.suurus[1] - 2*vahe)
        self.taust2.MääraAsukoht(asuk[0], asuk[1])
        self.taust2.MääraSuurus(suur[0], suur[1])
        self.taust2.Joonista()

        # Neid muutujaid hakkab kasutama mitu objekti.
        servadest = self.suurus[0]*0.1
        asukx = self.asukoht[0]+ servadest
        suurx = self.suurus[0] - 2*servadest

        # Nimekirjeldus
        asuky = self.asukoht[1] + 20
        self.nimeKirjeldus.MääraAsukoht((asukx, asuky))
        self.nimeKirjeldus.MääraLaius(suurx)
        self.nimeKirjeldus.Joonista()
        
        # Tekstikast
        asuky = asuky + self.nimeKirjeldus.KuiPaljuRuumiOnVaja() + 20
        tkAsukx = self.asukoht[0] + self.suurus[0] / 2
        self.nimeKast.MääraAsukoht((tkAsukx, asuky))
        self.nimeKast.MääraSuurus((suurx, 69))
        self.nimeKast.Joonista()
        
        # Alguskuupäeva kirjeldus
        asuky = asuky + self.nimeKast.VõtaSuurus()[1] + 20
        self.algKuupKirjeldus.MääraAsukoht((asukx, asuky))
        self.algKuupKirjeldus.MääraLaius(suurx)
        self.algKuupKirjeldus.Joonista()

        # Kuupäevaküsija
        asuky = asuky + self.algKuupKirjeldus.KuiPaljuRuumiOnVaja() + 20
        self.kpKüsija.MääraAsukoht((asukx, asuky))
        self.kpKüsija.MääraSuurus((suurx, 100))
        self.kpKüsija.PaneValmis()
        self.kpKüsija.Joonista()
        
        # Kellaaja kirjeldus
        asuky = asuky + self.kpKüsija.VõtaSuurus()[1] + 20
        self.algKellaKirjeldus.MääraAsukoht((asukx, asuky))
        self.algKellaKirjeldus.MääraLaius(suurx)
        self.algKellaKirjeldus.Joonista()
        
        # Algkellaküsija
        asuky = asuky + self.algKellaKirjeldus.KuiPaljuRuumiOnVaja() + 20
        self.algKellaKüsija.MääraAsukoht((asukx, asuky))
        self.algKellaKüsija.MääraSuurus((suurx, 1000))
        self.algKellaKüsija.PaneValmis()
        self.algKellaKüsija.Joonista()
        


        

        
      
        
        
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
