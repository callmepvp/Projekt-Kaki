import pygame
import os
from Kujundid import *
from Kuupäev import *
from Tekst import *
from Sündmused import *
from Tekstikujundid import *
from Programm import *

from Data import *
import win32gui
import win32con


#Pärisprogramm (võiks töötada)
def main():

    pygame.init()

    print(f"Programm käivitus kohast {indexDirectory}")
    peamineInfo = VõtaProgrammiInfo() #Kontrollib ja tagastab data

    #Assign program variables
    font = os.path.join(indexDirectory, f"Fondid/{peamineInfo['font']}")

    screen = pygame.display.set_mode((1280, 720), pygame.RESIZABLE)
    clock = pygame.time.Clock()

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

def testMain():
    
    programm = Programm()
    programm.JaaaaLäks()



#Käivitab vastava main() funktsiooni
if testingMode:
    testMain()
else:
    main()