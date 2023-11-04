import win32gui
import win32con



#See on klass, mis luuakse main functionis. Selle klassi muutujad tuleb salvestada faili ja failist see klass ka võtab oma muutujatele väärtused, kui on faili, kust neid võtta. 
class Programm:
    def __init__(self):
        self.sündmusteNimekiri = None
        self.font = None
        self.fondiSuurus = None
        self.päevaRuuduLaius = None
        self.päevaRuuduKõrgus = None


    # Funktsioon, mis loeb faili ja selle põhjal määrab klassimuutujate väärtusi. 
    def VõtaOlek():
        pass


    # Funktsioon, mis sisaldab peamist while-loopi. Selle funktsiooni sisu on see, mis ekraanil nähakse, kui programm töötab.
    def JaaaaLäks():

        def wndProc(oldWndProc, draw_callback, hWnd, message, wParam, lParam):
            if message == win32con.WM_SIZE:
                draw_callback()
                win32gui.RedrawWindow(hWnd, None, None, win32con.RDW_INVALIDATE | win32con.RDW_ERASE)
            return win32gui.CallWindowProc(oldWndProc, hWnd, message, wParam, lParam)

        pygame.init()
        ekraan = pygame.display.set_mode((640, 420), pygame.RESIZABLE)
    
        def JoonistaAsjad():
            ekraan.fill((240, 240, 240))

            taust.Joonista()
            r1.Paiguta()
            r1.Joonista()
            pygame.display.flip()
    
        oldWndProc = win32gui.SetWindowLong(win32gui.GetForegroundWindow(), win32con.GWL_WNDPROC, lambda *args: wndProc(oldWndProc, JoonistaAsjad, *args))




    

        taust = RistkülikAknas(ekraan, ekraan)
        taust.MääraAsukoht(0.1, 0.1)
        taust.MääraSuurus(0.8, 0.8)
        r1 = Ruudustik(ekraan, taust, 200, 210, 15, 30, 8)
            



        clock = pygame.time.Clock()

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            JoonistaAsjad()


            clock.tick(60)  # limits FPS to 60
        pygame.quit()
        



    # Funktsioon, mis salvestab klassimuutujad faili, et neid sealt järgmine kord uuesti sisse lugeda.
    def SalvestaOlek():
        pass




