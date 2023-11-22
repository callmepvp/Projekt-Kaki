from Kujundid import Ristkülik
import pygame
from Nupp import NupuAlus
from Programmiolek import ProgrammiOlek
from Tekst import MitmeReaTekst

class Tekstikast:
    def __init__(self, olek:"ProgrammiOlek", pind):
        self.olek = olek
        self.pind = pind
    
        self.asukoht = (0,0)
        self.maxLaius = 500
        
        def funk(): pass
        self.nupp = NupuAlus(olek, funk)
        self.nupp.nurgaRaadius = 0
        
        self.helendav = (50,50,238, 255)
        self.allavajutatud = (10,10,123, 255)
        self.tavaline = (30,30,178,255)
        self.kasutatavVärv = self.tavaline
        
        self.kasKirjutamine = False
        
        self.tekstiPygFont = self.olek.sündmuseReaKirjaFont
        
        self.mitmeReaTekst = MitmeReaTekst(self.olek, self.pind, "", self.tekstiPygFont)
        
        self.raam = Ristkülik(self.pind)
        self.raam.MääraRaamiPaksus(5)
        

    
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
                        return lõppTekst
                    elif event.key == pygame.K_BACKSPACE:
                        self.mitmeReaTekst.tekst = self.mitmeReaTekst.tekst[:-1]
                    else:
                        self.mitmeReaTekst.tekst += event.unicode


    def Joonista(self):
        
        self.nupp.TegeleNupuga()
        pind = self.pind
        print(self.nupp.suurus)

        if self.nupp.VõtaOlek() == 0:
            self.kasutatavVärv = self.tavaline
        elif self.nupp.VõtaOlek() == 1:
            self.kasutatavVärv = self.helendav
        elif self.nupp.VõtaOlek() == 2:
            self.kasutatavVärv = self.allavajutatud
            self.kasKirjutamine = True
            
        self.nupp.Joonista(self.pind)
       
            

        self.TegeleTekstiVõtuga()
        

        raamiVaheX = 5
        raamiVaheY = 10
        
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
        

