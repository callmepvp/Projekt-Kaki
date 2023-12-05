from Klassid.Päev import Päev
import pygame
import os
from Programmiolek import ProgrammiOlek
from Klassid.Nupp import NupuAlus
from Funktsioonid.UtilityFunktsioonid import võrdleObjektiParameetreid
from Klassid.Tekst import MitmeReaTekst, TekstRidadeks
from Klassid.Sündmus import Sündmus
from Klassid.Kujundid import Ristkülik

class DetailsemVaade:
    def __init__(self, pind:"pygame.Surface", olek:"ProgrammiOlek") -> None:
        self.päevaObjekt = None
        self.eelminePäevaObjekt = None
        self.asukoht = (0, 0)
        self.suurus = (400, 200)
        self.pind = pind
        
        def tühiFn(): pass

        def KõrvaleVajutus():
            self.olek.TäpsemaVaatePäev = None
            self.scrollOffset = 0

        self.olek = olek
        prio = self.olek.nuppudePrioriteedid["detailsem vaade"]
        self.nupp = NupuAlus(olek, prio)

        self.detailsemaVaateTaustaVärv = self.olek.detailsemaVaateTaustaVärv
        self.nupp.nurgaRaadius = 0

        self.ÜlemineVaheTekstiga = 10
        self.scrollOffset = 0
        self.reaKõrgus = 40

        self.font = pygame.font.Font(os.path.join("Fondid", 'CORBEL.TTF'), 36)

        self.taust = Ristkülik(self.pind)
        self.taust.MääraNurgaRaadius(20)
        self.taust.MääraVärv(self.olek.detailsemaVaateTaustaVärv)

    def MääraPäev(self, päev:"Päev"):
        self.päevaObjekt = päev

    def MääraSuurus(self, suurus):
        self.suurus = suurus
        self.nupp.MääraSuurus(suurus)

    def MääraAsukoht(self, asukoht):
        self.asukoht = asukoht
        self.nupp.MääraAsukoht(asukoht)

    def Joonista(self):
        self.nupp.TegeleNupuga()
        self.KäsitleSündmusi()
        
        päevaObjekt = self.päevaObjekt
        if not võrdleObjektiParameetreid(self.eelminePäevaObjekt, päevaObjekt):
            self.scrollOffset = 0
        """
        rect = (self.asukoht, self.suurus)
        pygame.draw.rect(self.pind, self.detailsemaVaateTaustaVärv, rect)"""

        self.taust.MääraAsukoht(self.asukoht[0], self.asukoht[1])
        self.taust.MääraSuurus(self.suurus[0], self.suurus[1])
        self.taust.Joonista()

        sündmused = päevaObjekt.VõtaSündmused()

        startIndeks = self.scrollOffset
        lõpuIndeks = min(len(sündmused), -1 + startIndeks + (int(self.suurus[1]) // self.reaKõrgus))
        järgmiseAsukoht = 0
        for i in range(startIndeks, lõpuIndeks):
            sündmus = sündmused[i]

            #tekst = f"{sündmus.nimi}"
            #tekst = MitmeReaTekst(self.olek, self.pind, sündmus.nimi, self.font)
            #tekst.Joonista()

            detailsemSündmus = DetailsemaVaateSündmus(self.pind, self.olek, sündmus)

            ülemiseSündmuseKaugusÜlaServast = 20
            SündmuseKaugusVasakServast = 20
            uusAsukohtX = self.asukoht[0] + SündmuseKaugusVasakServast
            uusAsukohtY = self.asukoht[1] + ülemiseSündmuseKaugusÜlaServast + järgmiseAsukoht
            
            detailsemSündmus.MääraAsukoht((uusAsukohtX, uusAsukohtY))

            kastiSuurus = (self.suurus[0] - 40, self.suurus[1])
            detailsemSündmus.MääraSuurus(kastiSuurus)
            detailsemSündmus.Joonista()
            järgmiseAsukoht += detailsemSündmus.võtaVajalikRuum()
            järgmiseAsukoht += 40 #vahe

            """
            tekstiPind = self.font.render(f"{sündmus.nimi}", True, (0, 0, 0))

            tekstiRect = tekstiPind.get_rect(topleft=(self.asukoht[0] + 10, self.asukoht[1] + self.ÜlemineVaheTekstiga + (i - startIndeks) * self.reaKõrgus - self.scrollOffset * self.reaKõrgus))

            if tekstiRect.bottom > self.asukoht[1] + self.ÜlemineVaheTekstiga:
                self.pind.blit(tekstiPind, tekstiRect)"""

        self.eelminePäevaObjekt = self.päevaObjekt

    def SkrolliÜles(self):
        self.scrollOffset = max(0, self.scrollOffset - 1)

    def SkrolliAlla(self):
        maxOffset = max(0, len(self.päevaObjekt.VõtaSündmused()) + 1 - (int(self.suurus[1] // self.reaKõrgus)))
        if self.scrollOffset < maxOffset:
            self.scrollOffset = min(maxOffset, self.scrollOffset + 1)

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



class DetailsemaVaateSündmus:
    def __init__(self, pind: "pygame.Surface", olek: "ProgrammiOlek", sündmus: "Sündmus") -> None:
        self.asukoht = (0, 0)
        self.suurus = (100, 100)
        self.sündmus = sündmus
        self.olek = olek
        self.pind = pind
        self.font = self.olek.sündmuseReaKirjaFont

        if self.sündmus.lõppaeg is not None:
            self.tekst = f"• {self.sündmus.algusaeg.tund}:{self.sündmus.algusaeg.minut} -{self.sündmus.lõppaeg.tund}:{self.sündmus.lõppaeg.minut} {self.sündmus.nimi}"
        else:
            self.tekst = f"• {self.sündmus.algusaeg.tund}:{self.sündmus.algusaeg.minut} {self.sündmus.nimi}"

        self.pealkiri = MitmeReaTekst(self.olek, self.pind, self.tekst, self.font)

        self.algkuupäev = DetailsemaVaateInfoväli(self.pind, self.olek, "Algkuupäev", sündmus.alguskuupäev.VõtaTekstina())
        self.lõppkuupäev = DetailsemaVaateInfoväli(self.pind, self.olek, "Lõppkuupäev", sündmus.lõppkuupäev.VõtaTekstina())
        self.algkell = DetailsemaVaateInfoväli(self.pind, self.olek, "Algkell", sündmus.algusaeg.VõtaStringina())
        self.lõppkell = DetailsemaVaateInfoväli(self.pind, self.olek, "Lõppkell", sündmus.lõppaeg.VõtaStringina())

    def MääraSuurus(self, suurus):
        self.suurus = suurus

    def MääraAsukoht(self, asukoht):
        self.asukoht = asukoht

    def Joonista(self):
        uusRida = MitmeReaTekst(self.olek, self.pind, self.tekst, self.font)
        uusRida.MääraRidadeArv(0) #lõpmatu
        uusRida.MääraReavahe(20)
        uusRida.MääraLaius(self.suurus[0])
        uusRida.MääraAsukoht(self.asukoht)

        uusRida.Joonista()

        kaheVäljaVahe = 30
        ääreVahe = 40
        väljaLaius = (self.suurus[0] - 2*ääreVahe - kaheVäljaVahe)/2

        asukX1 = self.asukoht[0] + ääreVahe + (väljaLaius/2) #raini kommentaar
        asukY1 = self.asukoht[1] + kaheVäljaVahe
        self.algkuupäev.MääraAsukoht((asukX1, asukY1))
        self.algkuupäev.MääraSuurus((väljaLaius, 0))

        asukX2 = asukX1 + väljaLaius + kaheVäljaVahe
        asukY2 = asukY1
        self.algkell.MääraAsukoht((asukX2, asukY2))
        self.algkell.MääraSuurus((väljaLaius, 0))

        kaheVäljaYVahe = 50
        #print(self.algkuupäev.VõtaSuurus()[1])
        self.lõppkuupäev.MääraAsukoht((asukX1, self.asukoht[1] + 30 + self.algkuupäev.VõtaSuurus()[1] + kaheVäljaYVahe))
        self.lõppkuupäev.MääraSuurus((väljaLaius, 0))

        self.algkuupäev.Joonista()
        self.algkell.Joonista()
        self.lõppkuupäev.Joonista()


    def võtaVajalikRuum(self):
        uusRida = MitmeReaTekst(self.olek, self.pind, self.sündmus.nimi, self.font)
        uusRida.MääraRidadeArv(3)
        uusRida.MääraReavahe(20)
        uusRida.MääraLaius(self.suurus[0])

        uusRida.tekst = self.tekst

        ruum = uusRida.KuiPaljuRuumiOnVaja()
        return ruum

class DetailsemaVaateInfoväli:
    def __init__(self, pind: "pygame.Surface", olek: "ProgrammiOlek", väljaPealkiri, väärtus) -> None:
        self.asukoht = (0, 0)
        self.suurus = (100, 100)

        self.olek = olek
        self.pind = pind
        self.font = self.olek.sündmuseReaKirjaFont

        self.väljaPealkiri = väljaPealkiri
        self.väärtuseTekst = väärtus

        self.nimi = MitmeReaTekst(self.olek, self.pind, väljaPealkiri, self.font)
        self.väärtus = MitmeReaTekst(self.olek, self.pind, väärtus, self.font)

        self.nimi.MääraKeskeleJoondus(True)
        self.väärtus.MääraKeskeleJoondus(True)
        self.nimi.MääraReavahe(15)
        self.väärtus.MääraReavahe(15)

    def MääraAsukoht(self, asukoht):
        self.asukoht = asukoht
    
    def MääraSuurus(self, suurus):
        self.suurus = suurus

    def Joonista(self):
        self.nimi.MääraAsukoht(self.asukoht)
        self.nimi.MääraLaius(self.suurus[0])
        self.nimi.Joonista()

        ruum = self.nimi.KuiPaljuRuumiOnVaja()
        self.väärtus.MääraAsukoht((self.nimi.asukoht[0], self.asukoht[1] + ruum + self.olek.InfoVäljadeReaVahe))
        self.väärtus.MääraLaius(self.suurus[0])
        self.väärtus.Joonista()

    def VõtaSuurus(self):
        r1 = self.nimi.KuiPaljuRuumiOnVaja()
        r2 = self.väärtus.KuiPaljuRuumiOnVaja()
        koguRuum = (self.suurus[0], self.olek.InfoVäljadeReaVahe + r1 + r2)
        return koguRuum


