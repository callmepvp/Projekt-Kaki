from Kujundid import Ristkülik
from Programmiolek import ProgrammiOlek
import pygame
from Sündmus import Sündmus
from Nupp import NupuAlus

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
        
        # Tausta aluse nupu koostamine. Nuppu läheb vaja, et tajuda, kui on taustalt eemale klikitud.
        def f2(): 
            print("Sündmuste lisamise lõpp.")
            self.olek.SündmuseLisamine = False
        self.nupp = NupuAlus(self.olek, None , f2)
        

    def Joonista(self):
        # Tausta ja nupu suurus ja asukoht
        asuk = self.asukoht
        suur = self.suurus
        
        self.nupp.TegeleNupuga()
        # Joonistab tausta
        self.taust.MääraAsukoht(asuk[0], asuk[1])
        self.taust.MääraSuurus(suur[0], suur[1])
        self.taust.Joonista()
        
        self.nupp.Joonista(self.pind)
        print(self.nupp.välineOlek)
     

    def MääraAsukoht(self, asukoht):
        self.asukoht = asukoht
        self.nupp.MääraAsukoht(asukoht)
        
    def MääraSuurus(self, suurus):
        self.suurus = suurus
        self.nupp.MääraSuurus(suurus)
        