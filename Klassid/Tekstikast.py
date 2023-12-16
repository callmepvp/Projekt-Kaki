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
        
        #def tühiF(): pass

        def f1(): 
            self.kasKirjutamine = True
            if self.olek.tegevuseNäitamine == True: print("Ühte tekstikasti kirjutamine algas.")
                
        self.nupp = NupuAlus(olek, prio, f1)

        # Tekstikasti raam
        self.raam = Ristkülik(pind)
        self.raam.MääraRaamiPaksus(olek.tekstikastiRaamiLaius)
        
        # Tekst tekstikasti sees
        font = olek.sündmuseReaKirjaFont
        self.tekst = MitmeReaTekst(olek, pind, "", font)
        reavahe = olek.tekstikastiReavahe
        self.tekst.MääraReavahe(reavahe)
    
    def AlustaKirjutamist(self):
        self.kasKirjutamine = True
        
    def LõpetaKirjutamine(self):
        self.kasKirjutamine = False

    def MääraKeskeleJoondus(self,väärtus:"bool"):
        self.keskeleJoondus = väärtus
        if väärtus == True: self.tekst.MääraKeskeleJoondus(True)
        else: self.tekst.MääraKeskeleJoondus(False)

    def TegeleTekstivõtuga(self):
        for event in self.olek.pygameEvents:
            if event.type == pygame.KEYDOWN:
                if self.kasKirjutamine == True:
                    if event.key == pygame.K_RETURN:
                        self.valmisTekst = self.tekst.tekst
                        self.tekst.MääraTekst("")
                    elif event.key == pygame.K_BACKSPACE:
                        self.tekst.tekst = self.tekst.tekst[:-1]
                        self.valmisTekst = self.tekst.tekst
                    else:
                        self.tekst.tekst += event.unicode
                        self.valmisTekst = self.tekst.tekst
    
    def VõtaSuurus(self):
        ülemineVahe = self.olek.tekstikastiÜlemineServTekstist
        alumineVahe = self.olek.tekstikastiAlumineServTekstist
        
        suurx = self.suurus[0]
        tekstiLaius = suurx - 2 * self.olek.tekstikastiKüljedTekstist
        self.tekst.MääraLaius(tekstiLaius)
        suury = self.tekst.KuiPaljuRuumiOnVaja() + ülemineVahe + alumineVahe
        return (suurx, suury)
    
    def Joonista(self):
        
        self.TegeleTekstivõtuga()      
        
        # Raami ja nupu suurused ja asukoht
        suurx, suury = self.VõtaSuurus()
        asukx, asuky = self.asukoht
        if self.keskeleJoondus == True:
            asukx = self.asukoht[0] - suurx/2
            
        # Nupu paigutus ja tegelemine
        self.nupp.MääraAsukoht((asukx, asuky))
        self.nupp.MääraSuurus((suurx, suury))
        self.nupp.TegeleNupuga()
        olek = self.nupp.VõtaOlek()

        # Raami suurus ja paigutus
        if olek == 0: self.raam.MääraVärv(self.olek.tekstikastiTavalineVärv)
        if olek == 1: self.raam.MääraVärv(self.olek.tekstikastiHelendavVärv)
        if olek == 2: self.raam.MääraVärv(self.olek.tekstikastiVajutatudVärv)
        self.raam.MääraAsukoht(asukx, asuky)
        self.raam.MääraSuurus(suurx, suury)
        self.raam.Joonista()
        
        # Teksti paigutus
        asuky = self.asukoht[1] + self.olek.tekstikastiÜlemineServTekstist
        asukx = self.asukoht[0] + self.olek.tekstikastiKüljedTekstist
        if self.keskeleJoondus == True: 
            asukx = self.asukoht[0]
        self.tekst.MääraAsukoht((asukx, asuky))
        self.tekst.Joonista()
        

    def MääraAsukoht(self, asukoht):
        self.asukoht = asukoht
        
    def MääraSuurus(self, suurus):
        self.suurus = suurus



class SelgitavTekstikast:
    def __init__(self, olek:"ProgrammiOlek", pind:"pygame.Surface"):
        # Tüüpilised omadused:
        self.olek = olek
        self.pind = pind
        self.suurus = (100,100)
        self.asukoht = (0,0)
        
        # Eriomadused:
        self.keskeleJoondus = False
        self.kasSelgitusKastiSees = False
        
        # Pealkirja tekst
        font = olek.sündmuseLisamiseInfoKirjaFont
        self.tekst = MitmeReaTekst(olek, pind, "trolololo", font)
        reavahe = olek.tekstikastiSelgituseReavahe
        self.tekst.MääraReavahe(reavahe)
        
        # Tekstikast
        self.veakontrolliFunktsioon = 0
        self.kast = Tekstikast(olek, pind)
    
    def MääraNupuF(self, funktsioon):
        self.kast.nupp.funktsioon = funktsioon

    def MääraVeaKontrolliFunktsioon(self, f1):
        self.veakontrolliFunktsioon = f1

    def VõtaVeaTeade(self):
        return self.veakontrolliFunktsioon(self.kast.valmisTekst)

    def MääraSõnum(self, tekst):
        self.tekst.MääraTekst(tekst)

    def MääraKeskeleJoondus(self, väärtus):
        self.keskeleJoondus = väärtus
        self.tekst.MääraKeskeleJoondus(väärtus)
        self.kast.MääraKeskeleJoondus(väärtus)

    def VõtaSuurus(self):
        suurx = self.suurus[0]
        suury = self.tekst.KuiPaljuRuumiOnVaja() + self.olek.tekstikastiSelgitusKastist + self.kast.VõtaSuurus()[1]
        return (suurx,suury)

    def Joonista(self):
        # Teksti asukoht
        # Teksti laius
        laius = self.suurus[0]
        if self.kasSelgitusKastiSees == True:
            laius = self.suurus[0]*0.9
        # Teksti y asukoht
        asuky = self.asukoht[1]
        if self.kasSelgitusKastiSees == True:
            asuky = self.asukoht[1] + 15
        # Teksti x asukoht
        asukx = self.asukoht[0]
        if self.keskeleJoondus == True:
            asukx = self.asukoht[0]
        # Objketile asukoha andmine
        self.tekst.MääraLaius(laius)
        self.tekst.MääraAsukoht((asukx, asuky))
        # Ei joonista selgitust ss kui see on tekstikasti sees ja kasutaja on midagi kirjutanud tekstikasti sisse.
        if self.kasSelgitusKastiSees == True and self.kast.valmisTekst != "":
            pass
        else:
            self.tekst.Joonista()
        
        # Kasti asukoht
        # Kasti x asukoht
        asukx = self.asukoht[0]
        # Kasti y asukoht
        asuky = self.asukoht[1] + self.tekst.KuiPaljuRuumiOnVaja() + self.olek.tekstikastiSelgitusKastist
        if self.kasSelgitusKastiSees:
            asuky = self.asukoht[1]
        # Tekstikasti laius
        suurx = self.suurus[0]
        self.kast.MääraAsukoht((asukx, asuky))
        self.kast.MääraSuurus((suurx, 200))
        self.kast.Joonista()
        
    def MääraSelgitusKastiSees(self,väärtus):
        # Teeb selgitava teksti heledamaks, kui see peab olema kasti sees. Nii on ilusam.
        if väärtus == True:
            self.tekst.MääraVärv((100,100,100,255))
        else:
            self.tekst.MääraVärv((0,0,0,255))
        self.kasSelgitusKastiSees = väärtus
        
    def MääraAsukoht(self, asukoht):
        self.asukoht = asukoht
        
    def MääraSuurus(self, suurus):
        self.suurus = suurus
        
    def MääraKirjutamine(self,väärtus:"bool"):
        self.kast.kasKirjutamine = väärtus
        
    def VõtaTekst(self):
        return self.kast.valmisTekst
    

