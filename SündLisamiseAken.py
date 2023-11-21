from Programmiolek import ProgrammiOlek
import pygame

class SündmuseLisamiseAken:
    def __init__(self, olek:"ProgrammiOlek", pind:pygame.surface.Surface):
        self.olek = olek
        self.pind = pind
        self.asukoht = (0,0)
        self.suurus = (400,400)
    

    def Joonista(self):
        # Joonistab tausta
        pind = self.pind
        värv = self.olek.sündmuseLisamiseTaustaVärv
        raad = self.olek.sündmuseLisamiseNurgaRaadius
        asuk = self.asukoht
        suur = self.suurus
        pygame.draw.rect(pind, värv, (asuk, suur), border_radius=raad)
     
    def MääraAsukoht(self, asukoht):
        self.asukoht = asukoht
       
    def MääraSuurus(self, suurus):
        self.suurus = suurus
        