from Klassid.Kujundid import Ristkülik
import pygame
from Klassid.Nupp import NupuAlus
from Programmiolek import ProgrammiOlek
from Klassid.Tekst import MitmeReaTekst


class Tekstikast:
    def __init__(self, olek:"ProgrammiOlek", pind):
        # Tüüpilised omadused
        self.olek = olek
        self.pind = pind
        self.asukoht = (0,0)
        self.suurus = (200,200)

        # Eriomadused
        self.keskeleJoondus = False
        self.valmisTekst = ""
        self.kasKirjutamine = False

        # Nupp tajumaks, kas hakata kirjutama
        prio = olek.nuppudePrioriteedid["tekstikast"]
        def f1(): self.kasKirjutamine = True
        self.nupp = NupuAlus(olek, prio, f1)

        # Tekstikasti raam
        self.raam = Ristkülik(pind)
        self.raam.MääraRaamiPaksus(olek.tekstikastiRaamiLaius)
        
        # Tekst tekstikasti sees
        font = olek.sündmuseReaKirjaFont
        self.tekst = MitmeReaTekst(olek, pind, "", font)
        reavahe = olek.tekstikastiReavahe
        self.tekst.MääraReavahe(reavahe)
    
    def MääraKeskeleJoondus(self,väärtus:"bool"):
        self.keskeleJoondus = väärtus
        if väärtus == True: self.tekst.MääraKeskeleJoondus(True)
        else: self.tekst.MääraKeskeleJoondus()

    def TegeleTekstivõtuga(self):
        for event in self.olek.pygameEvents:
            if event.type == pygame.KEYDOWN:
                if self.kasKirjutamine == True:
                    if event.key == pygame.K_RETURN:
                        lõppTekst = self.tekst.tekst
                        self.tekst.MääraTekst("")
                        self.valmisTekst = lõppTekst
                    elif event.key == pygame.K_BACKSPACE:
                        self.tekst.tekst = self.tekst.tekst[:-1]
                    else:
                        self.tekst.tekst += event.unicode
    
    def VõtaSuurus(self):
        ülemineVahe = self.olek.tekstikastiÜlemineServTekstist
        alumineVahe = self.olek.tekstikastiAlumineServTekstist
        
        suurx = self.suurus[0]
        tekstiLaius = suurx - 2 * self.olek.tekstikastiKüljedTekstist
        self.tekst.MääraLaius(tekstiLaius)
        suury = self.tekst.KuiPaljuRuumiOnVaja() + ülemineVahe + alumineVahe
        return (suurx, suury)
    
    def Joonista(self):
        # Raami ja nupu suurused ja asukoht
        suurx, suury = self.VõtaSuurus()
        asukx, asuky = self.asukoht
        if self.keskeleJoondus == True:
            asukx = self.asukoht[0] - suurx/2
            
        # Nupu paigutus ja tegelemine
        self.nupp.MääraAsukoht((asukx, asuky))
        self.nupp.MääraSuurus((suurx, suury))
        self.nupp.TegeleNupuga()
        self.TegeleTekstivõtuga()      

        # Raami suurus ja paigutus
        self.raam.MääraAsukoht(asukx, asuky)
        self.raam.MääraSuurus(suurx, suury)
        self.raam.Joonista()
        
        # Teksti paigutus
        asuky = self.asukoht[1] + self.olek.tekstikastiÜlemineServTekstist
        asukx = self.asukoht[0] + self.olek.tekstikastiKüljedTekstist
        if self.keskeleJoondus == True: 
            asukx = self.asukoht[0] - self.tekst.VõtaLaius()/2
        self.tekst.MääraAsukoht((asukx, asuky))
        self.tekst.Joonista()
        

    def MääraAsukoht(self, asukoht):
        self.asukoht = asukoht
        
    def MääraSuurus(self, suurus):
        self.suurus = suurus




class SelgitavTekstikast:
    def __init__(self, olek:"ProgrammiOlek", pind:"pygame.Surface"):
        self.asukoht = (0,0)
        self.suurus = (100,100)
        self.keskeleJoondus = False
        
        # tekstikast
        font = olek.sündmuseReaKirjaFont
        self.tekstikast = Tekstikast(olek, pind)

        # Tekst
        font = olek.päevaruuduPealkAastaPygFont
        self.tekst = MitmeReaTekst(olek,pind,"Kasuta MääraTekst funktsiooni.",font)
        self.tekst.MääraReavahe(10)
        
    def MääraKeskeleJoondus(self, väärtus:"bool"):
        self.keskeleJoondus = väärtus
    
    def MääraAsukoht(self, asukoht):
        self.asukoht = asukoht
        
    def MääraSuurus(self, suurus):
        self.suurus = suurus
        
    def Joonista(self):
        if self.keskeleJoondus == False:
            asuky = self.asukoht[1]
            self.tekst.MääraLaius(self.suurus[0])
            self.tekst.MääraAsukoht(self.asukoht)
            self.tekst.Joonista()
        
            asuky = asuky + self.tekst.KuiPaljuRuumiOnVaja() + 10
            self.tekstikast.MääraAsukoht((self.asukoht[0], asuky))
            self.tekstikast.MääraMaxLaius(self.suurus[0])
            self.tekstikast.Joonista()
            
        else:
            self.tekst.MääraKeskeleJoondus(True)
                        
            self.tekst.MääraLaius(self.suurus[0])
            self.tekst.MääraAsukoht(self.asukoht)
            self.tekst.Joonista()
            
            asukx = self.asukoht[0] - self.tekstikast.VõtaRaamiSuurus()[0]/2
            asuky = self.asukoht[1]
            self.tekstikast.MääraAsukoht((asukx, asuky))
            self.tekstikast.MääraMaxLaius(self.suurus[0])
            self.tekstikast.Joonista()
        
    def MääraTekst(self, tekst):
        self.tekst.MääraTekst(tekst)