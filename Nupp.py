import pygame
import 

class LisaSündmuseNupp:
    def __init__(self, olek, pind:"pygame.Surface"):
        self.pind = pind
        self.asukoht = (0,0)
        self.suurus = (200, 80)

        self.pildipind = pygame.image.load("pildid/pluss.png").convert_alpha()
        self.pildipind = pygame.transform.scale(self.pildipind, (45,45))

    def MääraSuurus(self, suurus):
        self.suurus = suurus

    def MääraAsukoht(self, asukoht):
        self.asukoht = asukoht
    
    def Joonista(self):
        pind = self.pind
        vasakVärv = (40,40,40,255)
        paremVärv = (158,240,26, 255)

        suhe = 0.2
        kiri = "Lisa sündmus"
        kõrgus = self.suurus[1]
        vasakLaius = self.suurus[0]*suhe
        paremLaius = self.suurus[0] - vasakLaius
        paremAsukx = self.asukoht[0] + vasakLaius
        nurgaÜmardus = 15

        vasakRect = (self.asukoht[0], self.asukoht[1], vasakLaius, kõrgus)
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
