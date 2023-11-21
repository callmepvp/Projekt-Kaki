from Päev import Päev
import pygame
import os
from Programmiolek import ProgrammiOlek
from Nupp import NupuAlus

class DetailsemVaade:
    def __init__(self, päevaObjekt: "Päev", pind:"pygame.Surface", olek:"ProgrammiOlek") -> None:
        self.päevaObjekt = päevaObjekt
        self.asukoht = (0, 0)
        self.suurus = (400, 200)
        self.pind = pind
        
        def tühiFn(): pass

        def KõrvaleVajutus():
            print("ter")
            self.olek.TäpsemaVaatePäev = None
            self.olek.scrollOffset = 0

        self.olek = olek
        self.nupp = NupuAlus(olek, tühiFn, KõrvaleVajutus)

        
        self.nupp.nurgaRaadius = 0

        self.ÜlemineVaheTekstiga = 10
        self.scrollOffset = olek.scrollOffset
        self.reaKõrgus = 40

        self.font = pygame.font.Font(os.path.join("Fondid", 'CORBEL.TTF'), 36)

    def MääraSuurus(self, suurus):
        self.suurus = suurus
        self.nupp.MääraSuurus(suurus)

    def MääraAsukoht(self, asukoht):
        self.asukoht = asukoht
        self.nupp.MääraAsukoht(asukoht)

    def Joonista(self):
        päevaObjekt = self.päevaObjekt

        rect = (self.asukoht, self.suurus)
        pygame.draw.rect(self.pind, (255, 123, 21), rect)

        sündmused = päevaObjekt.VõtaSündmused()

        startIndeks = self.scrollOffset
        lõpuIndeks = min(len(sündmused), startIndeks + (int(self.suurus[1]) // self.reaKõrgus))

        for i in range(startIndeks, lõpuIndeks):
            sündmus = sündmused[i]
            tekst = f"• {sündmus.nimi}"
            tekstiPind = self.font.render(tekst, True, (0, 0, 0))

            tekstiRect = tekstiPind.get_rect(topleft=(self.asukoht[0] + 10, self.asukoht[1] + self.ÜlemineVaheTekstiga + (i - startIndeks) * self.reaKõrgus - self.scrollOffset * self.reaKõrgus))

            if tekstiRect.bottom > self.asukoht[1] + self.ÜlemineVaheTekstiga:
                self.pind.blit(tekstiPind, tekstiRect)

    def SkrolliÜles(self):
        self.olek.scrollOffset = max(0, self.scrollOffset - 1)

    def SkrolliAlla(self):
        maxOffset = max(0, len(self.päevaObjekt.VõtaSündmused()) - (int(self.suurus[1] // self.reaKõrgus)))

        if self.scrollOffset < maxOffset:
            self.olek.scrollOffset = min(maxOffset, self.scrollOffset + 1)

    def KäsitleSündmusi(self):

        pygameEvents = self.olek.pygameEvents        
        for event in pygameEvents:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:
                    self.SkrolliÜles()
                elif event.button == 5:
                    self.SkrolliAlla()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.SkrolliÜles()
                elif event.key == pygame.K_DOWN:
                    self.SkrolliAlla()

        

