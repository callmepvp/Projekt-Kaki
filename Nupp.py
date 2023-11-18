import pygame
from PIL import Image, ImageFilter 
import PIL
from UtilityFunktsioonid import PILpiltPinnaks, KasAsukRingiSees
from Tekst import MitmeReaTekst, Tekst
from Programmiolek import ProgrammiOlek

class LisaSündmuseNupp:
    def __init__(self, olek:"ProgrammiOlek", pind:"pygame.Surface"):
        self.olek = olek
        self.pind = pind
        self.asukoht = (0,0)
        self.suurus = (200, 80)
        self.peamineVärv = olek.LisaSündmusNupuVärv
        self.sekundaarneVärv = olek.LisaSündmusNupuPlussiAluneVärv

        # Pluss
        Pp0 = Image.new(mode="RGBA", size=(64, 64), color=(0,0,0,0))
        Pp1 = Image.new(mode="RGBA", size=(64, 64), color=self.peamineVärv)
        Pmask = Image.open("Pildid/pluss2.png").convert('L')
        Pp3 = Image.composite(Pp1, Pp0, Pmask)

        # Dropshadow
        Dp0 = Image.new(mode="RGBA", size=(64, 64), color=(0,0,0,0))
        Dp1 = Image.new(mode="RGBA", size=(64, 64), color=(0,0,0,255))
        Dmask = Image.open("Pildid/pluss2.png").convert('L')
        Dmask = Dmask.filter(ImageFilter.GaussianBlur(3))
        Dp3 = Image.composite(Dp1, Dp0, Dmask)

        # Kokku
        valmis = Image.composite(Pp3, Dp3, Pp3)
        self.pildipind = PILpiltPinnaks(valmis)

    # See funktsioon muudab nupu värvi, kui hiir on selle kohal
    def HiireKontroll(self):
        asukx = self.asukoht[0]
        asuky = self.asukoht[1]
        suurx = self.suurus[0]
        suury = self.suurus[1]
        raad = self.olek.suureNupuNurgaRaadius
        hiireAsuk = pygame.mouse.get_pos()
        hiirx = hiireAsuk[0]
        hiiry = hiireAsuk[1]
        
        """if hiirx > asukx and hiirx < asukx + suurx or\
           hiiry > asuky and hiiry < asuky + suury or\
           KasAsukRingiSees(hiireAsuk, (asukx+raad,asuky+raad), raad) or\
           KasAsukRingiSees(hiireAsuk, (asukx+suurx-raad, asuky+raad), raad) or\
           KasAsukRingiSees(hiireAsuk, (asukx+raad, asuky+suury-raad), raad) or\
           KasAsukRingiSees(hiireAsuk, (asukx+suurx-raad, asuky+suury-raad), raad):
            self.peamineVärv = ()"""

    def MääraSuurus(self, suurus):
        self.suurus = suurus

    def MääraAsukoht(self, asukoht):
        self.asukoht = asukoht
    
    def Joonista(self):
        pind = self.pind
        vasakVärv = self.sekundaarneVärv
        paremVärv = self.peamineVärv

        suhe = 0.3
        
        kõrgus = self.suurus[1]
        vasakLaius = self.suurus[0]*suhe
        paremLaius = self.suurus[0] - vasakLaius
        paremAsukx = self.asukoht[0] + vasakLaius
        nurgaÜmardus = self.olek.suureNupuNurgaRaadius

        vasakRect = (self.asukoht[0], self.asukoht[1], vasakLaius*1.1, kõrgus)
        paremRect = (paremAsukx, self.asukoht[1], paremLaius, kõrgus)

        pildiAsukx = self.asukoht[0] + vasakLaius / 2 - self.pildipind.get_size()[0]/2
        pildiAsuky = self.asukoht[1] + kõrgus / 2 - self.pildipind.get_size()[1]/2

        pygame.draw.rect(pind, vasakVärv, vasakRect,
                         border_top_left_radius = nurgaÜmardus, 
                         border_bottom_left_radius = nurgaÜmardus)
        pygame.draw.rect(pind, paremVärv, paremRect,
                         border_top_right_radius = nurgaÜmardus, 
                         border_bottom_right_radius = nurgaÜmardus)
        
        
        self.pind.blit(self.pildipind, (pildiAsukx, pildiAsuky))
        
        
        nupuKiri = "Lisa sündmus"
        
        
        # Tekst nupu peale:
        nupuKirjaFont = self.olek.suureNupuTekstiPygFont
        
        kiri = MitmeReaTekst(self.olek, self.pind, nupuKiri, nupuKirjaFont)
        
        kiri.MääraRead(["Lisa", "sündmus"])
        kiri.MääraReavahe(self.olek.suureNupuTekstiSuurus * 1.1)
        ridadevahe = kiri.KuiPaljuRuumiOnVaja()
        
        asuky = self.asukoht[1] + self.suurus[1]/2 - ridadevahe/2
        asukx = paremAsukx + paremLaius/2
        kiri.MääraAsukoht((asukx, asuky))
        
        kiri.MääraKeskeleJoondus(True)
        
        kiri.Joonista()
        
        
