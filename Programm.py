import pygame
import win32gui
import win32con
from Klassid.Kujundid import Ristkülik
from Klassid.Tekst import MitmeReaTekst
from Klassid.Tekstikast import SelgitavTekstikast
from Klassid.Tekstikujundid import PäevaRuudustik, SündmuseRida
from Programmiolek import ProgrammiOlek
from Klassid.Kuupäev import Kuupäev
from Klassid.Sündmus import Sündmus
from Klassid.Nupp import LisaSündmuseNupp, NupuAlus
from Funktsioonid.UtilityFunktsioonid import GenereeriID
from Klassid.DetailsemVaade import DetailsemVaade, DetailsemaVaateInfoväli, DetailsemaVaateSündmus
from Klassid.SündLisamiseAken import SündmuseLisamiseAken
import math
  

#See on klass, mis luuakse main functionis. Kuna sellel klassil on ainult üks funktsioon, siis tehniliselt see klass võiks ka samahästi mitte klass olla, vaid lihtsalt see funktsioon olla
class Programm:
    def __init__(self, olek:ProgrammiOlek):
        self.olek = olek
        #print(olek.päevaruuduVärv)
        
    # Funktsioon, mis sisaldab peamist while-loopi. Selle funktsiooni sisu on see, mis ekraanil nähakse, kui programm töötab.
    def JaaaaLäks(self):


        def wndProc(oldWndProc, draw_callback, hWnd, message, wParam, lParam):
            if message == win32con.WM_SIZE:
                draw_callback()
                win32gui.RedrawWindow(hWnd, None, None, win32con.RDW_INVALIDATE | win32con.RDW_ERASE)
            return win32gui.CallWindowProc(oldWndProc, hWnd, message, wParam, lParam)

        pygame.init()
        ekraan = pygame.display.set_mode((640, 420), pygame.RESIZABLE)
        pygame.display.set_caption('Indie kalender')


        pygameIkoon = pygame.image.load('Pildid/iconDesign.png')
        pygame.display.set_icon(pygameIkoon)

        clock = pygame.time.Clock()
        
        
        ruudustik = PäevaRuudustik(self.olek, ekraan)

        def f1():
            if self.olek.tegevuseNäitamine == True: print("Vajutati kõigist vajutatavatest asjadest mööda.")
            if self.olek.TäpsemaVaatePäev != None:
                self.olek.TäpsemaVaatePäev = None
                if self.olek.tegevuseNäitamine == True: print("Täpsema vaate aken pandi kinni.")
            if self.olek.SündmuseLisamine != False:
                self.olek.SündmuseLisamine = False
                if self.olek.tegevuseNäitamine == True: print("Sündmuse lisamise aken pandi kinni.")


        prio = self.olek.nuppudePrioriteedid["taust"]
        ekraaniNupualus = NupuAlus(self.olek, prio, f1)

        a = LisaSündmuseNupp(self.olek, ekraan)
        
        b = SündmuseLisamiseAken(self.olek, ekraan)

        
        vaade = DetailsemVaade(ekraan, self.olek)
        
        


        def JoonistaAsjad():
            for i in self.olek.pygameEvents:
                if i.type == pygame.MOUSEWHEEL:
                    if self.olek.SündmuseLisamine == True or self.olek.TäpsemaVaatePäev != None:
                        pass
                    else:
                        self.olek.kerimisKogus += i.y*10

            ekraan.fill((255, 255, 255, 255))
            

            aknaSuur = ekraan.get_size()
            
            ekraaniNupualus.MääraAsukoht((0,0))
            ekraaniNupualus.MääraSuurus(aknaSuur)
            ekraaniNupualus.TegeleNupuga()
            

            if self.olek.kerimisKogus > 0:
                self.olek.kerimisKogus = 0
                
            ruudSuury = ruudustik.VõtaSuurus()[1]
            if self.olek.kerimisKogus < -ruudSuury:
                self.olek.kerimisKogus = -ruudSuury
            
            if len(self.olek.sündmusteNimekiri) != 0:
                ekrLai = aknaSuur[0]
                ruudAsukx = ekrLai * 0.1
                ruudAsuky = 30 + self.olek.kerimisKogus
                ruudustik.MääraAsukoht((ruudAsukx, ruudAsuky))
                ruudustik.MääraLaius(ekrLai*0.8)
                ruudustik.VärskendaRuute()
                ruudustik.Joonista()
            
            

            nupuAsukx = aknaSuur[0] * 0.3
            nupuAsuky = aknaSuur[1] * 0.75
            nupuSuurx = aknaSuur[0] - 2*nupuAsukx
            nupuSuury = aknaSuur[1] * 0.2
            a.MääraAsukoht((nupuAsukx, nupuAsuky))
            a.MääraSuurus((nupuSuurx, nupuSuury))
            a.Joonista()
            
            if self.olek.TäpsemaVaatePäev != None:
                taustaÄäreLaius = self.olek.DetailsemaVaateVälistaustaLaius
                vaade.MääraPäev(self.olek.TäpsemaVaatePäev)
                ekraaniW = aknaSuur[0]
                ekraaniH = aknaSuur[1]
                wProtsent, hProtsent = 0.6, 0.6
                # Määrab suuruse, asukoha, joonistab.
                vaadeSuurusX = 0.6 * ekraaniW
                vaadeSuurusY = 0.6 * ekraaniH
                vaadeAsukohtX = (ekraaniW - wProtsent * ekraaniW) / 2
                vaadeAsukohtY = (ekraaniH - hProtsent * ekraaniH) / 2
                vaade.MääraSuurus((vaadeSuurusX, vaadeSuurusY))
                vaade.MääraAsukoht((vaadeAsukohtX, vaadeAsukohtY))
                vaade.MääraNupuSuurus((vaadeSuurusX + 2*taustaÄäreLaius, vaadeSuurusY + 2*taustaÄäreLaius))
                vaade.MääraNupuAsukoht((vaadeAsukohtX - taustaÄäreLaius, vaadeAsukohtY - taustaÄäreLaius))
                vaade.Joonista()
                
            if self.olek.SündmuseLisamine != False:
                maxLaius = 700
                tegur = 600
                suurx = 2*maxLaius/math.pi * math.atan(aknaSuur[0]/tegur)
                suury = 300
                asukx = (aknaSuur[0]-suurx)/2
                asuky = 20
                b.MääraAsukoht((asukx, asuky))
                b.MääraSuurus((suurx, suury))
                b.Joonista()
                
            u = MitmeReaTekst(self.olek, ekraan, "Esimene ridaLoo\ndetavastiTeine rida", self.olek.sündmuseReaKirjaFont)
            u.MääraAsukoht((10,10))
            u.Joonista()
            pygame.display.flip()

            

            kõrgeimPrio = 0
            parimNupp = 0
            #print(self.olek.aktiivsedNupud)
            for i in self.olek.aktiivsedNupud:
                if i.prioriteet >= kõrgeimPrio:
                    kõrgeimPrio = i.prioriteet
                    parimNupp = i
                    
                    
            if parimNupp != 0:
                for i in self.olek.pygameEvents:
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        parimNupp.KutsuFunktsioon()
                        


        # See rida teeb nii, et asjad joonistuks ka akna suuruse muutumise ajal 
        oldWndProc = win32gui.SetWindowLong(win32gui.GetForegroundWindow(), win32con.GWL_WNDPROC, lambda *args: wndProc(oldWndProc, JoonistaAsjad, *args))


        # Main loop
        running = True
        while running:
            self.olek.pygameEvents = pygame.event.get()
            for event in self.olek.pygameEvents:
                if event.type == pygame.QUIT:
                    running = False
            

            JoonistaAsjad()
            

            clock.tick(60)  # limits FPS to 60
        pygame.quit()

        return self.olek
    # Programmi käimasolemise funktsiooni lõpp. 




