from Päev import Päev
import pygame

class DetailsemVaade:
    def __init__(self, päevaObjekt: "Päev", pind:"pygame.Surface") -> None:
        self.päevaObjekt = päevaObjekt
        self.asukoht = (0, 0)
        self.suurus = (400, 200)
        self.pind = pind

    def MääraSuurus(self, suurus):
        self.suurus = suurus

    def MääraAsukoht(self, asukoht):
        self.asukoht = asukoht

    def Joonista(self):
        pass
        #pygame.draw.rect(self.pind, (255, 123, 21), )