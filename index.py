import pygame
import os
from Kujundid import *
from Kuupäev import *
from Tekst import *
from Sündmused import *
from Tekstikujundid import *

from Data import *


#Pärisprogramm (võiks töötada)
def main():
    pygame.init()

    print(f"Programm käivitus kohast {indexDirectory}")
    peamineInfo = VõtaProgrammiInfo() #Kontrollib ja tagastab data

    #Assign program variables
    font = os.path.join(indexDirectory, f"Fondid/{peamineInfo['font']}")

    screen = pygame.display.set_mode((1280, 720), pygame.RESIZABLE)
    clock = pygame.time.Clock()

    pikktekst = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic"
    fontObject = pygame.font.Font(font, 20)
    tekst1 = Tekst(screen, "", font, (10,10,10), (0,100), 60)
    tekst2 = Tekst(screen, "", font, (10,10,10), (0,200), 60)
    kuupäev1 = Kuupäev(6, 11, 2023)
    print(kuupäev1.VõtaNädalaPäev())


    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                SalvestaFaili()

                running = False

        screen.fill("purple")
        
        hiireAsuk = pygame.mouse.get_pos()
        pygame.draw.circle(screen, "black", hiireAsuk, 10)
        tekstid = EraldaSobivaPikkusegaTekst(pikktekst, hiireAsuk[0], fontObject)
        #print(tekstid[0])
        tekst1.tekst = tekstid[0]
        tekst2.tekst = tekstid[1]
        
        tekst1.Joonista()
        tekst2.Joonista()


        pygame.display.flip()

        clock.tick(60)  # limits FPS to 60

    pygame.quit()




#Testimiseks (ei pea töötama)

def wndProc(oldWndProc, draw_callback, hWnd, message, wParam, lParam):
    if message == win32con.WM_SIZE:
        draw_callback()
        win32gui.RedrawWindow(hWnd, None, None, win32con.RDW_INVALIDATE | win32con.RDW_ERASE)
    return win32gui.CallWindowProc(oldWndProc, hWnd, message, wParam, lParam)

def testMain():
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




#Käivitab vastava main() funktsiooni
if testingMode:
    testMain()
else:
    main()