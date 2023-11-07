import pygame
import win32gui
import win32con
from Kujundid import RistkülikAknas
from Tekstikujundid import PäevaRuut
from Programmiolek import ProgrammiOlek
from Kuupäev import Kuupäev
from Sündmused import Sündmus
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
        
        kp = Kuupäev(5, 11, 2023)
        s1 = Sündmus("EMadepäeva kontsert", kp)
        pr = PäevaRuut(self.olek, ekraan, [s1])
        pr.taust.MääraVärv((100, 100, 100, 255))
        

        def JoonistaAsjad():
            ekraan.fill((240, 240, 240))

            pr.MääraAsukoht(ekraan.get_width() * 0.5, ekraan.get_height()*0.1)
            pr.MääraSuurus(ekraan.get_width() * 0.5, ekraan.get_height()*0.5)
            pr.Joonista()
            
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




