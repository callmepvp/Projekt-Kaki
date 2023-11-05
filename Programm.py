import pygame
import win32gui
import win32con
from Kujundid import *
from Tekstikujundid import *
import os


#Klass, mis hoiab neid väärtusi, mis loetakse failist ja kirjeldavad programmi välimust. Selles klassis olevad numbrid määravad eri kohtades olevate kirjade suurused, värvid, kaugused päevaruutude vahel, programmi taustaks oleva pildi, dropshadowi laiuse, rounded cornerite raadiused – kõikvõimaliku programmi kirjeldava. Iga objekti küsib luues programmiolekut parameetriks. See tundub mulle olevat ainus viis, kuidas mitte hard codeda asju.
class ProgrammiOlek:
    def __init__(self):
        pygame.init()
        
        # Päevaruutudel on taga taust, mis aitab ruute eraldada kõige taga olevast pildist. See mutuja kirjeldab selle tausta laiust aknas, kus 0 on olematu laius, 0.8 on 80% ekraani laiusest ja 1 on terve ekraani laius.
        self.ruutudeTaustaLaius = 0.8

        # Päevaruutude tausta ümardatud nurkade raadius pikslites. Hiljem vb teeb selle teguriks akna laiusest v kõrgusest v mõlemast, aga ei viitsi prg mõelda.
        self.ruutudeTaustaNurgaÜmardus = 10
        
        
        self.font = os.path.join("Fondid", "Gogh-ExtraBold.ttf")
        self.päevaruuduTekstiPygFont = pygame.font.Font(self.font, 20)
        self.päevaruuduPealkirjaPygFont = pygame.font.Font(self.font, 30)


        self.ruuduPealkirjaSuurus


    # Funktsioon, mis loeb faili ja selle põhjal määrab klassimuutujate väärtusi. 
    def VõtaOlekFailist():
        pass

    # Funktsioon, mis salvestab klassimuutujad faili, et neid sealt järgmine kord uuesti sisse lugeda.
    def SalvestaOlek(self):
        pass


        


#See on klass, mis luuakse main functionis. Kuna sellel klassil on ainult üks funktsioon, siis tehniliselt see klass võiks ka samahästi mitte klass olla, vaid lihtsalt see funktsioon olla
class Programm:
    def __init__(self):
        olek = ProgrammiOlek()


    


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

        r1 = Ruudustik(ekraan, taust, 200, 210, 15, 30, 8)


        def JoonistaAsjad():
            ekraan.fill((240, 240, 240))


            taust.Joonista()
            r1.Paiguta()
            r1.Joonista()
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




