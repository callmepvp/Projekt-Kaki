import pygame
import win32gui
import win32con
from Kujundid import RistkülikAknas
from Tekstikujundid import PäevaRuut, SündmuseRida, PäevaRuudustik
from Programmiolek import ProgrammiOlek
from Kuupäev import Kuupäev
from Sündmused import Sündmus
from Tekst import Tekst, EraldaSobivaPikkusegaTekst
import os
from Päev import Päev

  

#See on klass, mis luuakse main functionis. Kuna sellel klassil on ainult üks funktsioon, siis tehniliselt see klass võiks ka samahästi mitte klass olla, vaid lihtsalt see funktsioon olla
class Programm:
    def __init__(self, olek):
        self.olek = olek


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

        clock = pygame.time.Clock()
        

        kp1 = Kuupäev(8, 11, 2023)
        s1 = Sündmus("Emadepäeva kontsert", kp1)
        s1.MääraLõppKell(15, 34)
        s2 = Sündmus("MMP Moodle'i testi tähtaeg", kp1)
        s2.MääraLõppKell(21,0)
        p1 = Päev(kp1, [s1, s2])

        kp2 = Kuupäev(12, 11, 2023)
        s3 = Sündmus("Rong läheb Rakverre", kp2)
        s3.MääraLõppKell(13, 0)
        s4 = Sündmus("Pakk kaob pakiautomaadist ära", kp2)
        s4.MääraLõppKell(23,0)
        p2 = Päev(kp2, [s3, s4])


        ruudustik = PäevaRuudustik(self.olek, ekraan, [p1, p2])


        def JoonistaAsjad():
            ekraan.fill((255, 255, 255, 255))
            
            """rk1Asuk = (0.1, 0.1)
            rk1.MääraAsukoht(rk1Asuk[0], rk1Asuk[1])
            rk1.MääraSuurus(0.8,0.8)
            rk1.Joonista()

            tek.MääraAsukoht(rk1.VõtaAsukoht())
            tek.Joonista()

            laius = rk1.VõtaSuurus()[0]
            sürAsuk = rk1.VõtaAsukoht()
            sür.MääraAsukoht((sürAsuk[0], sürAsuk[1] + 30))
            sür.MääraLaius(laius)
            sür.Joonista()

            tek2.MääraAsukoht((sürAsuk[0], sürAsuk[1] + 80))
            sobTek = EraldaSobivaPikkusegaTekst(algtekst, laius, font)
            tek2.MääraTekst(sobTek[0])
            tek2.Joonista()

            ekrLaius = ekraan.get_width()
            ekrKõrgus = ekraan.get_height()

            ruut.MääraAsukoht(ekrLaius*0.1, ekrKõrgus*0.1)
            ruut.MääraSuurus(ekrLaius*0.8, ekrKõrgus*0.8)
            ruut.Joonista()"""

            
            ekrLai = ekraan.get_width()
            ekrKõrg = ekraan.get_height()
            ruudAsukx = ekrLai * 0.1
            ruudAsuky = ekrKõrg * 0.1
            ruudustik.MääraAsukoht((ruudAsukx, ruudAsuky))
            ruudustik.MääraLaius(ekrLai*0.8)
            ruudustik.Joonista()

            pygame.draw.rect(ekraan, (0,0,0,255), (300,50,100,100))
            
            pygame.display.flip()
    

        # See rida teeb nii, et asjad joonistuks ka akna suuruse muutumise ajal 
        oldWndProc = win32gui.SetWindowLong(win32gui.GetForegroundWindow(), win32con.GWL_WNDPROC, lambda *args: wndProc(oldWndProc, JoonistaAsjad, *args))


        # Main loop
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            JoonistaAsjad()

            clock.tick(60)  # limits FPS to 60
        pygame.quit()

        return self.olek
    # Programmi käimasolemise funktsiooni lõpp. 




