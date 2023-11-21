import pygame
from Nupp import NupuAlus
from Programmiolek import ProgrammiOlek

class Tekstikast:
    def __init__(self, olek:"ProgrammiOlek", pind):
        self.olek = olek
        self.pind = pind
    
        self.asukoht = (0,0)
        self.suurus = (300, 40)
        
        def funk(): pass
        self.nupp = NupuAlus(olek, funk)
        self.nupp.nurgaRaadius = 0
        
        self.helendav = (50,50,238, 255)
        self.allavajutatud = (10,10,123, 255)
        self.tavaline = (30,30,178,255)
        self.kasutatavVärv = self.tavaline
        
        self.kasKirjutamine = False
        
        self.tekstiPygFont = self.olek.sündmuseReaKirjaFont
        self.tekst = ""


    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    print(self.text)
                    self.text = ''
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = FONT.render(self.text, True, self.color)


    def MääraAsukoht(self, asukoht):
        self.asukoht = asukoht
        self.nupp.MääraAsukoht(asukoht)
        

    def MääraSuurus(self, suurus):
        if suurus[0] != None:
            self.suurus = (suurus[0], self.suurus[1])
            self.nupp.MääraSuurus((suurus[0], self.suurus[1]))
        if suurus[1] != None:
            self.suurus = (self.suurus[0], suurus[1])
            self.nupp.MääraSuurus((self.suurus[0], suurus[1]))

    
    def TegeleTekstiVõtuga(self):
        for event in self.olek.pygameEvents:
            if event.type == pygame.KEYDOWN:
                if self.kasKirjutamine == True:
                    if event.key == pygame.K_RETURN:
                        self.tekst = ''
                        return(self.tekst)
                    elif event.key == pygame.K_BACKSPACE:
                        self.tekst = self.tekst[:-1]
                    else:
                        self.tekst += event.unicode


    def Joonista(self):
        pind = self.pind
        self.nupp.TegeleNupuga()
        
        if self.nupp.VõtaOlek() == 0:
            self.kasutatavVärv = self.tavaline
        elif self.nupp.VõtaOlek() == 1:
            self.kasutatavVärv = self.helendav
        elif self.nupp.VõtaOlek() == 2:
            self.kasutatavVärv = self.allavajutatud
            self.kasKirjutamine = True
            
        self.nupp.Joonista(self.pind)
            

        self.TegeleTekstiVõtuga()
        

        self.txt_surface = self.tekstiPygFont.render(self.tekst, True, self.kasutatavVärv)
        
        
        # Valib ristkülikule sobiva laiuse
        self.suurus = (max(200, self.txt_surface.get_width()+10), self.suurus[1])

        # Joonistab teksti
        pind.blit(self.txt_surface, (self.asukoht[0]+5, self.asukoht[1]+5))
        
        # Joonistab teksti ümber oleva ristküliku piirjoone
        pygame.draw.rect(pind, self.kasutatavVärv, (self.asukoht, self.suurus), 10)