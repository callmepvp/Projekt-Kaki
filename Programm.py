import os


#See on klass, mis luuakse main functionis. Selle klassi muutujad tuleb salvestada faili ja failist see klass ka v�tab oma muutujatele v��rtused, kui on faili, kust neid v�tta. 
class Programm:
    def __init__(self):
        self.s�ndmusteNimekiri = None
        self.font = None
        self.fondiSuurus = None
        self.p�evaRuuduLaius = None
        self.p�evaRuuduK�rgus = None


    # Funktsioon, mis loeb faili ja selle p�hjal m��rab klassimuutujate v��rtusi. 
    def V�taOlek():
        pass


    # Funktsioon, mis sisaldab peamist while-loopi. Selle funktsiooni sisu on see, mis ekraanil n�hakse, kui programm t��tab.
    def JaaaaL�ks():

        def wndProc(oldWndProc, draw_callback, hWnd, message, wParam, lParam):
            if message == win32con.WM_SIZE:
                draw_callback()
                win32gui.RedrawWindow(hWnd, None, None, win32con.RDW_INVALIDATE | win32con.RDW_ERASE)
            return win32gui.CallWindowProc(oldWndProc, hWnd, message, wParam, lParam)
        



    # Funktsioon, mis salvestab klassimuutujad faili, et neid sealt j�rgmine kord uuesti sisse lugeda.
    def SalvestaOlek():
        pass




