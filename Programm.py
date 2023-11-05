import pygame
import win32gui
import win32con
from Kujundid import RistkülikAknas
from Tekstikujundid import PäevaPealkiri
from Programmiolek import ProgrammiOlek
from Kuupäev import Kuupäev
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
        clock = pygame.time.Clock()
    
        taust = RistkülikAknas(ekraan, ekraan)
        taust.MääraAsukoht(0.1, 0.1)
        taust.MääraSuurus(0.8, 0.8)
        kp = Kuupäev(5, 11, 2023)
        pk = PäevaPealkiri(self.olek, ekraan, kp)
        

        def JoonistaAsjad():
            ekraan.fill((240, 240, 240))

            taust.Joonista()
            asuk = taust.VõtaAsukoht()
            
            pk.MääraAsukoht(asuk[0], asuk[1])
            pk.Joonista()
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




