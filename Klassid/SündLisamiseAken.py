from Klassid.Kujundid import Ristkülik
from Programmiolek import ProgrammiOlek
import pygame
from Klassid.Nupp import NupuAlus
from Klassid.Tekstikast import SelgitavTekstikast



        


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
        
        # Tausta nupp
        prio = self.olek.nuppudePrioriteedid["sündmuse lisamise aken"]
        self.nupp = NupuAlus(self.olek, prio)
        
        # Nime küsimise tekstikast
        self.nimeKast = SelgitavTekstikast(olek, pind)
        self.nimeKast.MääraSõnum("Uue sündmuse kirjeldus:")
        
        # Päeva küsimise tekstikast
        self.päevaKast = SelgitavTekstikast(olek, pind)
        self.päevaKast.MääraSõnum("Päev:")
        

    def Joonista(self):
        # Taust
        asuk = self.asukoht
        suur = self.suurus
        
        self.nupp.TegeleNupuga()
        
        self.taust.MääraAsukoht(asuk[0], asuk[1])
        self.taust.MääraSuurus(suur[0], suur[1])
        self.taust.Joonista()
        
        # Tekstikast
        servast = suur[0]*0.1
        asukx = self.asukoht[0] + servast
        asuky = self.asukoht[1] + 17
        suurx = self.suurus[0] - 2 * servast
        suury = self.suurus[1]
        
        self.nimeKast.MääraAsukoht((asukx, asuky))
        self.nimeKast.MääraSuurus((suurx, suury))
        self.nimeKast.Joonista()
        
        # Päeva kast
        self.päevaKast.MääraAsukoht(())
     

    def MääraAsukoht(self, asukoht):
        self.asukoht = asukoht
        self.nupp.MääraAsukoht(asukoht)
        
    def MääraSuurus(self, suurus):
        self.suurus = suurus
        self.nupp.MääraSuurus(suurus)



    
