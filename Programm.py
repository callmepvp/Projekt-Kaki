import os


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
        



    # Funktsioon, mis salvestab klassimuutujad faili, et neid sealt järgmine kord uuesti sisse lugeda.
    def SalvestaOlek():
        pass




