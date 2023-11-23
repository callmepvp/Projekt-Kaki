from Klassid.Kujundid import Ristkülik
import pygame
from Klassid.Nupp import NupuAlus
from Programmiolek import ProgrammiOlek
from Klassid.Tekst import MitmeReaTekst

class Tekstikast:
    def __init__(self, olek:"ProgrammiOlek", pind):
        self.olek = olek
        self.pind = pind
    
        self.asukoht = (0,0)
        self.maxLaius = 500
        
        def funk(): pass
        self.nupp = NupuAlus(olek, 10, funk)
        self.nupp.nurgaRaadius = 0
        
        self.helendav = (248,237,239, 255)
        self.allavajutatud = (158,139,135, 255)
        self.tavaline = (200,191,189,255)
        self.kasutatavVärv = self.tavaline
        
        self.kasKirjutamine = False
        
        self.tekstiPygFont = self.olek.sündmuseReaKirjaFont
        
        self.mitmeReaTekst = MitmeReaTekst(self.olek, self.pind, "", self.tekstiPygFont)
        
        self.raam = Ristkülik(self.pind)
        self.raam.MääraRaamiPaksus(5)
        self.raam.MääraNurgaRaadius(0)
        
        self.valmisTekst = ""
        

    
    def MääraAsukoht(self, asukoht):
        self.asukoht = asukoht
        self.nupp.MääraAsukoht(asukoht)
        

    """
    def MääraSuurus(self, suurus):
        if suurus[0] != None:
            self.suurus = (suurus[0], self.suurus[1])
            self.nupp.MääraSuurus((suurus[0], self.suurus[1]))
        if suurus[1] != None:
            self.suurus = (self.suurus[0], suurus[1])
            self.nupp.MääraSuurus((self.suurus[0], suurus[1]))
    """
    


    def MääraMaxLaius(self, maxLaius):
        self.maxLaius = maxLaius
        self.mitmeReaTekst.MääraLaius(maxLaius)
        

    def TegeleTekstiVõtuga(self):
        for event in self.olek.pygameEvents:
            if event.type == pygame.KEYDOWN:
                if self.kasKirjutamine == True:
                    if event.key == pygame.K_RETURN:
                        lõppTekst = self.mitmeReaTekst.tekst
                        self.mitmeReaTekst.MääraTekst("")
                        self.valmisTekst = lõppTekst
                    elif event.key == pygame.K_BACKSPACE:
                        self.mitmeReaTekst.tekst = self.mitmeReaTekst.tekst[:-1]
                    else:
                        self.mitmeReaTekst.tekst += event.unicode


    def Joonista(self):
        
        self.nupp.TegeleNupuga()

        if self.nupp.VõtaOlek() == 0:
            self.raam.MääraVärv(self.tavaline)
        elif self.nupp.VõtaOlek() == 1:
            self.raam.MääraVärv(self.helendav)
        elif self.nupp.VõtaOlek() == 2:
            self.raam.MääraVärv(self.allavajutatud)
            self.kasKirjutamine = True
            
        #self.nupp.Joonista(self.pind)
       
            

        self.TegeleTekstiVõtuga()
        

        raamiVaheX = 10
        raamiVaheY = 15
        
        # Joonistab ristküliku
        asukx = self.asukoht[0]
        asuky = self.asukoht[1]
        suurx = max(100, raamiVaheX + self.mitmeReaTekst.VõtaLaius() + raamiVaheX)
        suury = raamiVaheY + self.mitmeReaTekst.KuiPaljuRuumiOnVaja() + raamiVaheY
        
        self.raam.MääraAsukoht(asukx, asuky)
        self.raam.MääraSuurus(suurx, suury)
        self.raam.Joonista()
        
        # Määrab nupualuse suuruse
        self.nupp.MääraSuurus((suurx, suury))
        
        # Joonistab teksti
        asukx = self.asukoht[0]+raamiVaheX
        asuky = self.asukoht[1]+raamiVaheY
        
        self.mitmeReaTekst.MääraAsukoht((asukx, asuky))
        self.mitmeReaTekst.Joonista()
        

