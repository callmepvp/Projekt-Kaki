import pygame
from Klassid.ObjektiAlus import ObjektiAlus



# Klass, mille mõte on joonsitada ekraanile ristkülikut.
class Ristkülik(ObjektiAlus):
    def __init__(self, pind):
        super().__init__()
        self.pind = pind
        self.värv = (200, 200, 200, 255)
        self.raamiPaksus = 0
        self.nurgaRaadius = 0
    
    """
    # Funktsiooni saab panna ka None sisse kummagi väärtuse asemele, mis jätab suuruse samaks.
    def MääraSuurus(self, x, y):
        if x == None:
            self.suur = (self.suur[0], y)
        elif y == None:
            self.suur = (x, self.suur[1])
        self.suur = (x,y)
    
    def MääraAsukoht(self, x, y):
        self.asuk = (x,y)
    """

    def VõtaSuurus(self):
        return self.suurus

    def VõtaAsukoht(self):
        return self.asukoht

    def MääraRaamiPaksus(self, paksus):
        self.raamiPaksus = paksus
            
    def MääraNurgaRaadius(self, raadius):
        self.nurgaRaadius = raadius
        
    # Värv olgu tuple nagu (r,g,b,a).
    def MääraVärv(self, värv):
        self.värv = värv

    def Joonista(self):
        pygame.draw.rect(self.pind, self.värv, (self.VõtaAsukoht(), self.VõtaSuurus()),self.raamiPaksus, self.nurgaRaadius)