import pygame
import win32gui
import win32con
from Kujundid import RistkülikAknas
from Tekstikujundid import PäevaRuut, SündmuseRida
from Programmiolek import ProgrammiOlek
from Kuupäev import Kuupäev
from Sündmused import Sündmus
from Tekst import Tekst, EraldaSobivaPikkusegaTekst
import os

  

#See on klass, mis luuakse main functionis. Kuna sellel klassil on ainult üks funktsioon, siis tehniliselt see klass võiks ka samahästi mitte klass olla, vaid lihtsalt see funktsioon olla
class Programm:
    def __init__(self):
        self.olek = ProgrammiOlek()


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

        kp2 = Kuupäev(12, 11, 2023)
        s2 = Sündmus("MMP Moodle'i testi tähtaeg", kp2)
        s2.MääraLõppKell(21,0)

        sür = SündmuseRida(self.olek, ekraan, s1)
        rk1 = RistkülikAknas(ekraan, ekraan)
        font = self.olek.sündmuseReaKirjaFont
        värv = self.olek.ruuduTekstiVärv
        tek = Tekst(ekraan, "Tere", font, värv, (0,0))
        algtekst = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
        tek2 = Tekst(ekraan, algtekst, font, värv, (0,0))

        ruut = PäevaRuut(self.olek, ekraan, [s1,s2])

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
            tek2.Joonista()"""

            ekrLaius = ekraan.get_width()
            ekrKõrgus = ekraan.get_height()

            ruut.MääraAsukoht(ekrLaius*0.1, ekrKõrgus*0.1)
            ruut.MääraSuurus(ekrLaius*0.8, ekrKõrgus*0.8)
            ruut.Joonista()

            
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
    # Programmi käimasolemise funktsiooni lõpp. 




