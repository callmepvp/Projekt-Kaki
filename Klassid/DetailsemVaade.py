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

        self.olek = olek
        prio = self.olek.nuppudePrioriteedid["detailsem vaade"]
        self.nupp = NupuAlus(olek, prio)

        self.detailsemaVaateTaustaVärv = self.olek.detailsemaVaateTaustaVärv
        self.nupp.nurgaRaadius = 0

        self.ÜlemineVaheTekstiga = 10
        self.scrollOffset = 0
        self.reaKõrgus = 40

        self.font = pygame.font.Font(os.path.join("Fondid", 'CORBEL.TTF'), 36)

        # Tausta ristküliku koostamine
        self.tagumineTaust = Ristkülik(self.pind)
        self.tagumineTaust.MääraNurgaRaadius(self.olek.sündmuseLisamiseNurgaRaadius)
        self.tagumineTaust.MääraVärv(self.olek.DetailsemaVaateHeledamVärv)

        self.taust = Ristkülik(self.pind)
        self.taust.MääraNurgaRaadius(20)
        self.taust.MääraVärv(self.olek.detailsemaVaateTaustaVärv)

    def MääraPäev(self, päev:"Päev"):
        self.päevaObjekt = päev

    def MääraSuurus(self, suurus):
        self.suurus = suurus
        
    def MääraNupuSuurus(self, suurus):
        self.nupp.MääraSuurus(suurus)

    def MääraNupuAsukoht(self, asukoht):
        self.nupp.MääraAsukoht(asukoht)

    def MääraAsukoht(self, asukoht):
        self.asukoht = asukoht
        self.nupp.MääraAsukoht(asukoht)

    def Joonista(self):
        self.nupp.TegeleNupuga()
        self.KäsitleSündmusi()
    
        if not võrdleObjektiParameetreid(self.eelminePäevaObjekt, self.päevaObjekt):
            self.scrollOffset = 0
        
        taustaÄäreLaius = self.olek.DetailsemaVaateVälistaustaLaius
        tagumiseTaustaX = self.asukoht[0] - taustaÄäreLaius
        tagumiseTaustaY = self.asukoht[1] - taustaÄäreLaius
        tagumiseSuurusX = self.suurus[0] + 2*taustaÄäreLaius
        tagumiseSuurusY = self.suurus[1] + 2*taustaÄäreLaius
        self.tagumineTaust.MääraAsukoht(tagumiseTaustaX, tagumiseTaustaY)
        self.tagumineTaust.MääraSuurus(tagumiseSuurusX, tagumiseSuurusY)
        self.tagumineTaust.Joonista()

        self.taust.MääraAsukoht(self.asukoht[0], self.asukoht[1])
        self.taust.MääraSuurus(self.suurus[0], self.suurus[1])
        self.taust.Joonista()


        sündmused = self.päevaObjekt.VõtaSündmused()
        järgmiseAsukoht = 0
        for i in sündmused:
            detailsemSündmus = DetailsemaVaateSündmus(self.pind, self.olek, i)

            ülemiseSündmuseKaugusÜlaServast = 20
            SündmuseKaugusVasakServast = 20
            uusAsukohtX = self.asukoht[0] + SündmuseKaugusVasakServast
            uusAsukohtY = self.asukoht[1] + ülemiseSündmuseKaugusÜlaServast + järgmiseAsukoht
            
            detailsemSündmus.MääraAsukoht((uusAsukohtX, uusAsukohtY))

            kastiSuurus = (self.suurus[0] - 40, self.suurus[1])
            
            detailsemSündmus.MääraSuurus(kastiSuurus)
            detailsemSündmus.Joonista()
            järgmiseAsukoht += detailsemSündmus.võtaVajalikRuum()
            järgmiseAsukoht += self.olek.kaheSündmusKastiVahe

        """
        startIndeks = self.scrollOffset
        lõpuIndeks = min(len(sündmused), -1 + startIndeks + (int(self.suurus[1]) // self.reaKõrgus))
        järgmiseAsukoht = 0
        for i in range(startIndeks, lõpuIndeks):
            sündmus = sündmused[i]

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
            järgmiseAsukoht += self.olek.kaheSündmusKastiVahe
            """

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
        self.font = self.olek.päevaruuduPealkKpPygFont
        self.tekst = self.sündmus.nimi
        
        # Pealkiri
        self.pealkiri = MitmeReaTekst(self.olek, self.pind, self.tekst, self.font)
        self.pealkiri.MääraReavahe(20)
        

        # Tekstiväljad
        self.algkuupäev = DetailsemaVaateInfoväli(self.pind, self.olek, "Algkuupäev", sündmus.alguskuupäev.VõtaTekstina())
        self.lõppkuupäev = DetailsemaVaateInfoväli(self.pind, self.olek, "Lõppkuupäev", sündmus.lõppkuupäev.VõtaTekstina())
        self.algkell = DetailsemaVaateInfoväli(self.pind, self.olek, "Algkell", sündmus.algusaeg.VõtaStringina())
        self.lõppkell = DetailsemaVaateInfoväli(self.pind, self.olek, "Lõppkell", sündmus.lõppaeg.VõtaStringina())

    def MääraSuurus(self, suurus):
        self.suurus = suurus

    def MääraAsukoht(self, asukoht):
        self.asukoht = asukoht

    def Joonista(self):
        VäliPealkirjast = self.olek.DetailsemaVaateVäliPealkirjast
        kaheVäljaVahe = 0.1*self.suurus[1]
        väljadÄärest = 0.1*self.suurus[0]
        väljadeLaius = (self.suurus[0] - 2*väljadÄärest - kaheVäljaVahe)/2
        
        # Pealkiri
        self.pealkiri.MääraLaius(self.suurus[0])
        self.pealkiri.MääraAsukoht(self.asukoht)
        self.pealkiri.Joonista()
        
        # algkuupäev
        asukx = self.asukoht[0] + väljadÄärest + (väljadeLaius/2)
        asuky = self.asukoht[1] + self.pealkiri.KuiPaljuRuumiOnVaja() + VäliPealkirjast
        self.algkuupäev.MääraAsukoht((asukx, asuky))
        self.algkuupäev.MääraSuurus((väljadeLaius, 0))
        self.algkuupäev.Joonista()
        
        # lõppkuupäev      
        asukx = self.asukoht[0] + väljadÄärest + (väljadeLaius/2)
        asuky = self.asukoht[1] + self.pealkiri.KuiPaljuRuumiOnVaja() + VäliPealkirjast + kaheVäljaVahe + self.algkuupäev.VõtaSuurus()[1]
        self.lõppkuupäev.MääraAsukoht((asukx, asuky))
        self.lõppkuupäev.MääraSuurus((väljadeLaius, 0))
        self.lõppkuupäev.Joonista()

        # algkell      
        asukx = self.asukoht[0] + väljadÄärest + (väljadeLaius/2) + väljadeLaius + kaheVäljaVahe
        asuky = self.asukoht[1] + self.pealkiri.KuiPaljuRuumiOnVaja() + VäliPealkirjast
        self.algkell.MääraAsukoht((asukx, asuky))
        self.algkell.MääraSuurus((väljadeLaius, 0))
        self.algkell.Joonista()

        # lõppkell    
        asukx = self.asukoht[0] + väljadÄärest + (väljadeLaius/2) + väljadeLaius + kaheVäljaVahe
        asuky = self.asukoht[1] + self.pealkiri.KuiPaljuRuumiOnVaja() + VäliPealkirjast + kaheVäljaVahe + self.algkuupäev.VõtaSuurus()[1]
        self.lõppkell.MääraAsukoht((asukx, asuky))
        self.lõppkell.MääraSuurus((väljadeLaius, 0))
        self.lõppkell.Joonista()

    def võtaVajalikRuum(self):
        väliPealkirjast = self.olek.DetailsemaVaateVäliPealkirjast
        suurimVajaminevRuum = max(self.algkuupäev.VõtaSuurus()[1] + self.lõppkuupäev.VõtaSuurus()[1], self.algkell.VõtaSuurus()[1] + self.lõppkell.VõtaSuurus()[1])
        return väliPealkirjast + 0.1*self.suurus[1] + self.pealkiri.KuiPaljuRuumiOnVaja() + suurimVajaminevRuum

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


